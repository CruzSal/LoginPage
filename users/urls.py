from django.urls import path
from .views import home, RegistrationView

urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegistrationView.as_view(), name='users-register'),
]