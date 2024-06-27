from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("dodaj/<str:name>/", views.dodaj, name="dodaj"),
    path("edytuj/<str:name>/<str:title>/", views.edytuj, name="edytuj")
]