from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UsernameField, AuthenticationForm, UserCreationForm
from django.forms import ModelForm

from .models import Program, Profile


class LoginForm(AuthenticationForm):
    username = UsernameField(
        label='Имя пользователя',
        max_length=254,
        widget=forms.TextInput(attrs={'autofocus' : True, 'class': 'from-control'}))
    password = forms.CharField(
        label='Пароль',
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        label="Пароль",
        strip=False,
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
        label="Подтверждение пароля",
        widget=forms.PasswordInput,
        strip=False,
    )

    class Meta:
        model = Profile
        fields = ['username']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


class ProgramCreateForm(ModelForm):
    class Meta:
        model = Program
        exclude = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})