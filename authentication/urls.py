from django.urls import path
from .views import LoginView, RegisterView

urlpatterns = [
    path('login/', LoginView.as_view(), name='api-login'),
    path('register/user/', RegisterView.as_view(), name='api-register'),
]