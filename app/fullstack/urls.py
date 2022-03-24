from django.urls import path

from . import views



urlpatterns = [

    path ("", views.index, name="index"),
    path ("schedule", views.schedule, name="schedule"),
    path ("speakers", views.speakers, name="speakers"),
    path ("about", views.about, name="about"),

]