from django.urls import path

from payment import views


urlpatterns = [
    path("cart/", views.index),
    path("purchase/", views.purchase),
    path("complete/", views.complete),
]