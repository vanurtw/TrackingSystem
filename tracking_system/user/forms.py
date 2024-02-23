from django import forms
from .models import CustomUser


class SignUpUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,label='Логин',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    first_name = forms.CharField(max_length=100,label='Имя',
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=100,label='Фамилия',
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    email = forms.EmailField(max_length=100,label='Email',
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password = forms.CharField(max_length=100,label='Пароль',
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Passowrd'}))

    def __init__(self, *args, **kwargs):
        self.base_fields['building'].widget.attrs['class'] = 'form-control'
        self.base_fields['building'].required = True
        self.base_fields['building'].label = 'Здание'
        super(SignUpUserForm, self).__init__(*args, **kwargs)

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'building', 'email', 'password']


class LoginUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100, label='Логин',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(max_length=100,label='Пароль',
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Passowrd'}))

    class Meta:
        model = CustomUser
        fields = ['username', 'password']
