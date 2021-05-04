from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    return render(request,'index.html')


def login(request):
    return render(request,'login.html')

def home(request):
    return render(request,'home.html')

def registration(request):
    if request.method == 'POST':
         user_form=UserCreationForm()
         if user_form.is_valid():
             profile=user_form.save(commit=False)
             profile.user=request.user
             profile.save()
             return HttpResponse("<h1>Registration Successfully</h1>")
    else:
         user_form=UserCreationForm()
    return render(request,'registration.html',{'user_form':user_form})

