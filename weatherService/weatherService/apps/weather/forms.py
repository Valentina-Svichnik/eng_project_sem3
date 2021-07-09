from django import forms
from django.db.models import fields
from django.forms import widgets
from django.forms.models import ModelForm
from django.forms import TextInput, widgets
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

class AuthUserForm(AuthenticationForm, ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        
        widgets = {
            'username' : TextInput(attrs={
                'type' : 'text',
                'class' : 'form-control mb-3',
                'id' : 'login',
                'placeholder' : 'Логин',
            }),
            'password' : TextInput(attrs={
                '' : '',
                'type' : 'text',
                'class' : 'form-control mb-3',
                'id' : 'password',
                'placeholder' : 'Пароль',
            })
        }

class RegisterUserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

        widgets = {
            'username' : TextInput(attrs={
                'type' : 'text',
                'class' : 'form-control mb-3',
                'id' : 'login',
                'placeholder' : 'Логин',
            }),
            'password' : TextInput(attrs={
                '' : '',
                'type' : 'text',
                'class' : 'form-control mb-3',
                'id' : 'password',
                'placeholder' : 'Пароль',
            })
        }

    def save(self, commit = True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
        