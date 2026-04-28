from django.urls import path

from . import views

app_name = "programs"

urlpatterns = [
    path("", views.program_list, name="list"),
]
