from email.policy import default
from django.urls import reverse
from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, FormView, TemplateView
from django.views.generic.detail import SingleObjectMixin
from django import forms
from django.core.mail import send_mail
from django.conf import settings

from pleinair.models import PleinAir
from .models import Contact


class ContactForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    mobile = forms.CharField()
    message = forms.CharField(max_length=500, widget=forms.Textarea)


class ContactDetailView(TemplateView):
    model = Contact
    template_name = 'contact/contact_us.html'

    def get_context_data(self):
        context = {
            'form': ContactForm()
        }
        return context


class ContactFormView(SingleObjectMixin, FormView):
    model = Contact
    template_name = 'contatc/contact_us.html'
    form_class = ContactForm

    def get_success_url(self):
        return reverse('contact:thanks')

    def get_contact_object(self, form):
        try:
            contact = Contact.objects.create(
                name=form['name'].value(),
                email=form['email'].value(),
                tel=form['mobile'].value(),
                add_message=form['message'].value(),
            )
            contact.save()
        except ValueError:
            pass
        return contact

    def get_object(self):
        return None

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            contact = self.get_contact_object(form)
            send_mail(
                'From BELEVETS: Contact me',
                contact.get_data(),
                'verified_addres',
                ['verified_addres'],
                fail_silently=False,
            )
        else:
            return render(
                request, 'contact/contact_us.html',
                {'form': ContactForm, 'errors': form.errors.values()}
            )
        return super().post(request, *args, **kwargs)


class ContactView(View):

    def get(self, request, *args, **kwargs):
        view = ContactDetailView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = ContactFormView.as_view()
        return view(request, *args, **kwargs)


class PleinAirDetailView(ContactDetailView):

    def get_context_data(self, pk):
        pleinair = PleinAir.objects.get(pk=pk)
        form = forms.Form()
        name = forms.CharField(max_length=50)
        email = forms.EmailField()
        mobile = forms.CharField()
        message_text = f"I would like to participate in plein air {pleinair.title} on {pleinair.start}"
        _obj = forms.Textarea(attrs={"rows": 5, "cols": 30, 'placeholder': message_text})
        # _obj.initial= message_text

        message = forms.CharField(widget=_obj)
        fields = {
            'name': name,
            'email': email,
            'mobile': mobile,
            'message': message
        }
        setattr(form, 'fields', fields)
        context = {
            'form': form
        }
        return context


class PleinAirView(View):

    def get(self, request, *args, **kwargs):
        view = PleinAirDetailView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = ContactFormView.as_view()
        return view(request, *args, **kwargs)


def thanks(request):
    return render(request, 'contact/thanks.html')
