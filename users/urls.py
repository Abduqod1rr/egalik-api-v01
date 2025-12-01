from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.registerUser.as_view(), name="register")
    
]
