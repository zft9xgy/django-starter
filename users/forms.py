from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import AppUser
from django.forms import ModelForm
from django.contrib.auth.models import User


class AppUserCreationForm(UserCreationForm):

    class Meta:
        model = AppUser
        fields = ["email"]


class AppUserChangeForm(UserChangeForm):

    class Meta:
        model = AppUser
        fields = ["email"]


class AppUserPublicForm(ModelForm):
    class Meta:
        model = AppUser
        fields = ['email']

class AppUserPublicRegisterForm(UserCreationForm):

    class Meta:
        model = AppUser
        fields = ['email', 'password1', 'password2']
