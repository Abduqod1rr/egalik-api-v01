from django.urls  import path 
from . import views


urlpatterns = [
    path("productds/add/", views.AddProduct.as_view(), name="addproduct"),
    path("home/", views.Home.as_view(), name="home")
]
