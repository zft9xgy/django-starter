from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from users.forms import AppUserPublicForm, AppUserPublicRegisterForm

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

    if request.user.is_authenticated:
        return redirect('home') 

    if request.method == "POST":
        form = AppUserPublicRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirige a la página de inicio u otra página después del registro
    else:
        form = AppUserPublicRegisterForm()
    
    context  = {
        'form' : form,
    }
    return render(request, 'users/users-register.html', context)

def userLogout(request):
    logout(request)
    return redirect('/')