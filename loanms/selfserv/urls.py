from django.urls import path
from . import views
urlpatterns = [

    path('first/',views.show),
    path('first/report', views.getReport),
]