from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    path('', views.BlogView.as_view(), name='blog'),
    path('<int:pk>/', views.ArticleView.as_view(), name='article'),
]
