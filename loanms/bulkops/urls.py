from django.urls import path
from . import views
app_name = "<bulkops>"
urlpatterns = [

    path('first/upload/', views.upload_csv,name='upload_csv'),
]