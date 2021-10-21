from django.urls import path

from shopping import views

app_name = "shop"
urlpatterns = [
    path("shop", views.index, name="home"),
    path("admin", views.admin),
    path("item", views.item)
]