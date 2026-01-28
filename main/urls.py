from django.urls  import path 
from . import views
from .views import healthz

urlpatterns = [
    path("healthz",healthz),
    path("add/", views.AddProduct.as_view(), name="addproduct"),
    path("", views.Home.as_view(), name="home"),
    path("mening_elonlarim/", views.MyProducts.as_view(), name="mening_elonlarim"),
    path("CRUD/<int:pk>/", views.productCrud.as_view(), name="CRUD")
]
