from django.urls import path
from . import views

urlpatterns = [
    path('ws_test/', views.ws_test, name='ws_test'),
    path('all_projects/', views.all_projects, name='all_projects'),
    path('single_project/<int:in_proj_id>', views.single_project, name='single_project'),
]