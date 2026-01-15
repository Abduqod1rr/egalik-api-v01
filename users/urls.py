from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
<<<<<<< HEAD
    path("register/", views.registerUser.as_view(), name="register"),# bulardan ols=din auth/ bor
    path("login/", views.loginUser.as_view(), name="login"), 
    path("logout/", views.logoutUser.as_view(), name="logout")
=======
    path("register/", views.registerUser.as_view(), name="register"),
    
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
>>>>>>> dev
    
]
