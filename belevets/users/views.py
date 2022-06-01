from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.urls import reverse
import json
from django.core.exceptions import ObjectDoesNotExist

from users.forms import CustomUserCreationForm
from users.models import UserProfile, Order
from course.models import Course


def register(request):
    if request.method == 'GET':
        return render(
            request, 'users/register.html',
            {'form': CustomUserCreationForm}
        )
    elif request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.backend = "django.contrib.auth.backends.ModelBackend"
            user.save()
            user_profile = UserProfile.objects.create(user=user)
            user_profile.save()
            login(request, user)
            return redirect(reverse('users:dashboard'))
        else:
            return render(
                request, 'users/register.html',
                {'form': CustomUserCreationForm, 'errors': form.errors.values(), }
            )
    return redirect(reverse('users:register'))


def dashboard(request, *args, **kwargs):
    if request.user.is_authenticated:
        # Just users who passed registration formcan access (admin fromc reatesuperuser - cant)
        try:
            user = request.user.userprofile
        except ObjectDoesNotExist:
            return render(request, 'users/dashboard.html')

        courses = user.course.all()
        try:
            order = Order.objects.get(user=user, payment=False)
            ordered_courses = order.courses.all()
            amount = 0
            for course in ordered_courses:
                amount += course.price
        except (AttributeError, ObjectDoesNotExist):
            order = None
            ordered_courses = None
            amount = 0

        context = {
            'courses': courses,
            'ordered_courses': ordered_courses,
            'amount': amount,
        }
    else:
        # Template is_authenticated=False part will work
        context = None
    return render(request, 'users/dashboard.html', context)


def order(request, pk):  # TODO check with several courses in order
    if request.user.is_authenticated:
        user = UserProfile.objects.get(user=request.user)
        try:
            order = Order.objects.get(user=user, payment=False)
            order.courses.add(Course.objects.get(pk=pk))
        except (ObjectDoesNotExist, AttributeError):
            order = Order.objects.create(user=user)
            order.courses.set([Course.objects.get(pk=pk)])
            order.save()
    return dashboard(request)


def cancel_order(request):
    user = UserProfile.objects.get(user=request.user)
    try:
        order = Order.objects.get(user=user, payment=False)
        order.delete()
    except ObjectDoesNotExist:
        pass
    return dashboard(request)


# PayPal Payment
def checkout(request):
    if request.user.is_authenticated:
        user = request.user.userprofile
        courses = user.course.all()
        try:
            order = Order.objects.get(user=user, payment=False)
            amount = 0
            for obj in order.courses.all():
                amount += obj.price
            ordered_courses = order.courses.all()
            context = {
                'courses': courses,
                'ordered_courses': ordered_courses,
                'order': order,
                'amount': amount,
            }
        except ObjectDoesNotExist:
            context = {
                'courses': courses,
                'amount': 0,
            }
            return render(request, 'users/dashboard.html', context)
    else:
        # Template is_authenticated part will work
        context = None
    return render(request, 'users/checkout.html', context)


def payment_complete(request):
    body = json.loads(request.body)
    user = request.user.userprofile
    order = Order.objects.get(pk=body['orderID'])
    order.payment = True
    order.save()
    courses = order.courses.all()
    for course in courses:
        user.course.add(course)
    return dashboard(request)
