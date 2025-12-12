from django.urls import path
from .views import RegisterView, ConfirmView, LoginView

urlpatterns = [
    path("register/", RegisterView.as_view()),
    path("confirm/", ConfirmView.as_view()),
    path("login/", LoginView.as_view()),
]
