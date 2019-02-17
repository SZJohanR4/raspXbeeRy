from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import loginForm

# Create your views here.
def loginUser(request):
    login_form=loginForm()
    if request.method=='POST':
        form = loginForm(request.POST)
        if form.is_valid():
            username=request.POST['user_name']
            password=request.POST['password']
            user = authenticate(request=request, username=username, password=password)
            if user is not None and user.is_active:
                request.session.set_expiry(86400)
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                fail="Datos Incorrectos"
                return render(request,'index.html',{"form":login_form, "fail":fail})
    return render(request,'index.html',{"form":login_form})

def logoutUser(request):
    logout(request)
    return HttpResponseRedirect('/')
