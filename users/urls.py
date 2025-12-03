from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.registerUser.as_view(), name="register"),# bulardan ols=din auth/ bor
    path("login/", views.loginUser.as_view(), name="login"), 
    path("logout/", views.logoutUser.as_view(), name="logout")
    
]
