from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('order/<int:pk>/', views.order, name='add_order'),
    path('cancel/', views.cancel_order, name='cancel'),
    path('checkout/', views.checkout, name='checkout'),
    path('complete/', views.payment_complete, name='complete'),
]
