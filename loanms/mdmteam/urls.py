from django.urls import path
from . import views
#app_name = "<bulkops>"
urlpatterns = [

    path('reports/', views.print_report,name='upload_csv'),
]