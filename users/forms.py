from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# we create our form which include e-mail fields
# we can use that form in the users/views instead UserCreationForm


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

