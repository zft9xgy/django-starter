from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from users.forms import AppUserPublicForm

# Create your views here.



def userLogin(request):

    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        # se comprueba que el usuario existe y si existe lo devuelve
        user = authenticate(email=request.POST['email'], password=request.POST['password'])
        if user is not None:
            # A backend authenticated the credentials
            login(request, user) 
            nextUrl = request.GET.get("next", "/")
            return redirect(nextUrl)
        else:
            # No backend authenticated the credentials
            # implement some type of warning here
            pass

    return render(request,'users/users-login.html')

def userRegister(request):
    return render(request,'users/users-register.html')


def userLogout(request):
    logout(request)
    return redirect('/')