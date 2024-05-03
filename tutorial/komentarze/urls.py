from django.urls import path

from . import views

app_name = "komentarze"
urlpatterns = [
    path("", views.create_comment, name="create_comment"),
    path("<str:author_name>/thanks/", views.thanks, name="thanks"),
    path("<str:author_name>/<str:message>/thanks/", views.thanks, name="thanks")
    
]