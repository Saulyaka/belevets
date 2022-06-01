from django.urls import path
from .views import ContactView, PleinAirView, thanks


app_name = 'contact'

urlpatterns = [
    path('', ContactView.as_view(), name='contact'),
    path('thanks/', thanks, name='thanks'),
    path('<int:pk>/', PleinAirView.as_view(), name='pleinair'),
]
