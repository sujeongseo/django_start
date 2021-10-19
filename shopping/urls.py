from django.urls import path

from shopping import views


urlpatterns = [
    path("shop", views.index),
    path("admin", views.admin),
    path("item", views.item)
]