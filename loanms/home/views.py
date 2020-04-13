from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
# Create your views here.
def home(request):
    dict={'name':" ",'name1':" ",'name2':" "}
    return render(request,'home.html',context=dict)

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
def mdm(request):
    return render(request,'emp.html')