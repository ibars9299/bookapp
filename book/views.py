from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserLoginForm, BookForm
from .models import Book, Category, WordNote
from django.http import FileResponse, Http404, JsonResponse
import os
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import models

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
    search_query = request.GET.get('search')
    categories = Category.objects.all()
    
    books = Book.objects.all()
    
    # Arama filtrelemesi
    if search_query:
        books = books.filter(
            models.Q(name__icontains=search_query) |
            models.Q(author__icontains=search_query) |
            models.Q(categories__name__icontains=search_query)
        ).distinct()
    
    # Kategori filtrelemesi
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        books = books.filter(categories=category)
    
    # Sayfalama
    paginator = Paginator(books, 9)  # Her sayfada 9 kitap
    page = request.GET.get('page')
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)
    
    return render(request, 'book/index.html', {
        'books': books,
        'categories': categories,
        'current_category': category_slug,
        'search_query': search_query
    })

@login_required
def read_book(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
        if book.pdf:
            pdf_path = book.pdf.path
            if os.path.exists(pdf_path):
                response = FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')
                response['Content-Disposition'] = 'inline'
                # Cache kontrolü ekle
                response['Cache-Control'] = 'no-cache'
                response['X-Frame-Options'] = 'SAMEORIGIN'
                return response
            else:
                raise Http404("PDF dosyası bulunamadı")
        else:
            raise Http404("Bu kitap için PDF yok")
    except Book.DoesNotExist:
        raise Http404("Kitap bulunamadı")

@login_required
def book_notes(request, book_id):
    """Kelime notları için ayrı bir view"""
    try:
        book = Book.objects.get(id=book_id)
        word_notes = WordNote.objects.filter(
            user=request.user,
            book=book
        ).order_by('-created_at')
        
        return render(request, 'book/book_notes.html', {
            'book': book,
            'word_notes': word_notes
        })
    except Book.DoesNotExist:
        raise Http404("Kitap bulunamadı")

@login_required
def add_word_note(request):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        english_word = request.POST.get('english_word')
        turkish_meaning = request.POST.get('turkish_meaning')
        page_number = request.POST.get('page_number')
        
        note = WordNote.objects.create(
            user=request.user,
            book_id=book_id,
            english_word=english_word,
            turkish_meaning=turkish_meaning,
            page_number=page_number
        )
        
        return JsonResponse({'success': True, 'note_id': note.id})
    return JsonResponse({'success': False}, status=400)

@login_required
def delete_word_note(request, note_id):
    if request.method == 'DELETE':
        try:
            note = WordNote.objects.get(id=note_id, user=request.user)
            note.delete()
            return JsonResponse({'success': True})
        except WordNote.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Not bulunamadı'}, status=404)
    return JsonResponse({'success': False}, status=400)
