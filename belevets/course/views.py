from django.views import generic, View

from .models import Course, Section, Lesson


class CoursesView(generic.ListView):
    model = Course
    template_name = 'course/courses.html'
    context_object_name = 'courses'


class PublicCourseDetailView(generic.DetailView):
    model = Course
    template_name = 'course/course_public.html'

    def get_context_data(self, *args, **kwargs):
        course = Course.objects.get(pk=int(kwargs['object'].pk))
        sections = Section.objects.filter(course=course)
        for section in sections:
            section.lessons = Lesson.objects.filter(section=section)
        context = {
            'course': course,
            'sections': sections
        }
        return context


class PrivateCourseDetailView(generic.DetailView):
    model = Course
    template_name = 'course/course_private.html'
    context_object_name = 'course'

    def get_context_data(self, *args, **kwargs):
        course = Course.objects.get(pk=int(kwargs['object'].pk))
        sections = Section.objects.filter(course=course)
        for section in sections:
            section.lessons = Lesson.objects.filter(section=section)
        context = {
            'course': course,
            'sections': sections
        }
        return context


class CourseDetailView(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            course = Course.objects.get(pk=self.kwargs['pk'])
            user_courses = request.user.userprofile.course.all()
            if course in user_courses:
                view = PrivateCourseDetailView.as_view()
                return view(request, *args, **kwargs)
        view = PublicCourseDetailView.as_view()
        return view(request, *args, **kwargs)
