from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from users.forms import AppUserPublicForm, AppUserPublicRegisterForm
from users.models import AppUser
from django.contrib import messages



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
            messages.warning(request, 'Wrong credentials.')

    return render(request,'users/users-login.html')


def userRegister(request):

    if request.user.is_authenticated:
        return redirect('home') 

    if request.method == "POST":
        form = AppUserPublicRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home') 
    else:
        form = AppUserPublicRegisterForm()
    
    context  = {
        'form' : form,
    }
    return render(request, 'users/users-register.html', context)

def userLogout(request):
    logout(request)
    return redirect('/')


@login_required(login_url='user-login')
def userAccount(request):
    user = get_object_or_404(AppUser,email=request.user.email)

    context = {
        'user':user,
    }
    return render(request, 'users/users-account.html', context)

@login_required(login_url='user-login')
def userDelete(request):
    user = get_object_or_404(AppUser,email=request.user.email)
    if request.method == 'GET':
        return render(request, 'users/users-delete-account-confirmation.html', {'user':user})

    if request.method == 'POST':
        user.delete()
        #todo send user confirmation by email after delete.
        return redirect('home')
    
