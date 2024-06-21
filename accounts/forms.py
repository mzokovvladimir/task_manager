from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'first_name', 'last_name', 'phone', 'avatar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].required = True
        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['phone'].required = True
        self.fields['avatar'].required = False

        self.fields['username'].widget.attrs.update({'placeholder': 'username'})
        self.fields['email'].widget.attrs.update({'placeholder': 'example@ex.com'})
        self.fields['first_name'].widget.attrs.update({'placeholder': 'Ivan'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Ivanov'})
        self.fields['phone'].widget.attrs.update({'placeholder': '+380XXXXXXXXX'})
        self.fields['avatar'].widget.attrs.update({'placeholder': 'Optional. Upload a profile picture'})


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'password')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'username', 'email', 'phone', 'avatar')
