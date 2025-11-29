from django.urls  import path 
from . import views


urlpatterns = [
    path("/add/", views.AddProduct.as_view(), name="addproduct"),
    path("/", views.Home.as_view(), name="home")
]
