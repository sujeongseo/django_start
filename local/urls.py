from django.urls import path

from local import views

app_name = "local"
urlpatterns = [
    path("local-shops", views.index, name="home")
]
