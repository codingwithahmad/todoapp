from django.urls import path
from . import views
# Set Urls here

urlpatterns = [
    path("", views.index, name="index"),
]