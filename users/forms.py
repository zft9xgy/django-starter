from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import AppUser
from django.forms import ModelForm


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