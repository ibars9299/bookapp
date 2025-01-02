from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Book, Category

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Form alanları için özel etiketler ve placeholder'lar
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Kullanıcı Adı'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'E-posta'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Şifre'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Şifre (Tekrar)'})

class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Kullanıcı Adı'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Şifre'
    }))

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'author', 'image', 'pdf', 'page']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Kitap Adı'
            }),
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Yazar'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'pdf': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'page': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Sayfa Sayısı'
            })
        }
