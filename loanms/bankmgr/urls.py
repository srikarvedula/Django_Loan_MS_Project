from django.urls import path
from . import views

urlpatterns = [
    path('first/loanmdm/', views.show),
    path('first/loanmdm/add_new_form', views.add_new_record),
    path('first/loanmdm/edit/<int:loan_mdm_lookup_id>', views.edit),
    path('first/loanmdm/update/', views.update),
    path('first/loanmdm/delete/<int:loan_mdm_lookup_id>', views.delete),

]