from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Avatar


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='email', required=True)
    password1 = forms.CharField(label='Contraseña', max_length=30, required=True, widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la Contraseña', max_length=30, required=True, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k: "" for k in fields}

class edit_user(forms.ModelForm):
    username=forms.CharField(label='username', max_length=40, required=False)
    email = forms.EmailField(label='email', required=False)

    class Meta:
        model= User
        fields= ['username','email']

class edit_profile(forms.ModelForm):
    avatar = forms.ImageField(required=False,widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    description = forms.CharField(widget=forms.Textarea,  required=False)
    social1 = forms.URLField(required=False)
    social2 = forms.URLField(required=False)

    class Meta:
        model = Avatar
        fields = ['avatar', 'description', 'social1', 'social2']
