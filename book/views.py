from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserLoginForm, BookForm
from .models import Book, Category
from django.http import FileResponse, Http404
import os

def login_user(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                form.add_error(None, 'Kullanıcı adı veya şifre hatalı')
    else:
        form = UserLoginForm()
    return render(request, 'book/login.html', {'form': form})

def register_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserRegisterForm()
    return render(request, 'book/register.html', {'form': form})

@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save()
            # Seçilen kategorileri kaydet
            categories = request.POST.getlist('categories')
            book.categories.set(categories)
            return redirect('index')
    else:
        form = BookForm()
    
    # Form için tüm kategorileri gönder
    categories = Category.objects.all()
    return render(request, 'book/add_book.html', {
        'form': form,
        'categories': categories
    })

def logout_user(request):
    logout(request)
    return redirect('index')

def index(request):
    category_slug = request.GET.get('category')
    categories = Category.objects.all()
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        books = Book.objects.filter(categories=category)
    else:
        books = Book.objects.all()
    
    print("Kategoriler:", categories)
    
    return render(request, 'book/index.html', {
        'books': books,
        'categories': categories,
        'current_category': category_slug
    })

@login_required
def read_book(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
        if book.pdf:
            context = {
                'book': book,
                'user_id': request.user.id
            }
            return render(request, 'book/pdf_viewer.html', context)
        raise Http404("PDF bulunamadı")
    except Book.DoesNotExist:
        raise Http404("Kitap bulunamadı")
