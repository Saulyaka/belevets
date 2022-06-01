from django.urls import path
from . import views


app_name = 'pleinair'

urlpatterns = [
    path('', views.PleinairView.as_view(), name='pleinair'),
    path('<int:pk>/', views.DetailView.as_view(), name='details'),
]
