from django.urls import path
from .views import CoursesView, PublicCourseDetailView, PrivateCourseDetailView, CourseDetailView


app_name = 'course'
urlpatterns = [
    path('', CoursesView.as_view(), name='courses'),
    path('<int:pk>/', CourseDetailView.as_view(), name='course'),
]
