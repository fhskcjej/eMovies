from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import *


class CustomUserForm(UserChangeForm):
    password = None  # отключаем поле пароля

    class Meta:
        model = User
        fields = ('username', 'email', 'avatar')

    def __init__(self, *args, **kwargs):
        super(CustomUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['avatar'].widget.attrs.update({'class': 'form-control'})


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ('card_number', 'expiration_date', 'CVV')

    def __init__(self, *args, **kwargs):
        super(CardForm, self).__init__(*args, **kwargs)
        self.fields['card_number'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Номер карты'})
        self.fields['expiration_date'].widget.attrs.update({'class': 'form-control', 'placeholder': 'MM/YY'})
        self.fields['CVV'].widget.attrs.update({'class': 'form-control', 'placeholder': 'CVV'})



class LoginForm(forms.Form):
    username = forms.CharField(
        label="Имя пользователя",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )