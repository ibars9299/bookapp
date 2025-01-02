import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookapp.settings')
django.setup()

from book.models import Category

# Önce mevcut kategorileri temizleyelim
Category.objects.all().delete()

# Yeni kategorileri ekleyelim
categories = [
    {'name': 'Roman', 'icon': 'fa-solid fa-book', 'slug': 'roman'},
    {'name': 'Edebiyat', 'icon': 'fa-solid fa-feather', 'slug': 'edebiyat'},
    {'name': 'Tarih', 'icon': 'fa-solid fa-landmark', 'slug': 'tarih'},
    {'name': 'Bilim', 'icon': 'fa-solid fa-flask', 'slug': 'bilim'},
    {'name': 'Felsefe', 'icon': 'fa-solid fa-brain', 'slug': 'felsefe'},
    {'name': 'Aşk', 'icon': 'fa-solid fa-heart', 'slug': 'ask'},
    {'name': 'Korku/Gerilim', 'icon': 'fa-solid fa-ghost', 'slug': 'korku-gerilim'},
    {'name': 'Bilim Kurgu', 'icon': 'fa-solid fa-rocket', 'slug': 'bilim-kurgu'},
    {'name': 'Fantastik', 'icon': 'fa-solid fa-hat-wizard', 'slug': 'fantastik'},
    {'name': 'Çocuk Kitapları', 'icon': 'fa-solid fa-child', 'slug': 'cocuk-kitaplari'},
    {'name': 'Eğitim', 'icon': 'fa-solid fa-graduation-cap', 'slug': 'egitim'},
    {'name': 'İş/Ekonomi', 'icon': 'fa-solid fa-chart-line', 'slug': 'is-ekonomi'},
    {'name': 'Din/Tasavvuf', 'icon': 'fa-solid fa-mosque', 'slug': 'din-tasavvuf'},
    {'name': 'Sanat', 'icon': 'fa-solid fa-palette', 'slug': 'sanat'},
    {'name': 'Sağlık', 'icon': 'fa-solid fa-heart-pulse', 'slug': 'saglik'},
    {'name': 'Kişisel Gelişim', 'icon': 'fa-solid fa-person-running', 'slug': 'kisisel-gelisim'},
    {'name': 'Psikoloji', 'icon': 'fa-solid fa-brain', 'slug': 'psikoloji'},
    {'name': 'Şiir', 'icon': 'fa-solid fa-feather-pointed', 'slug': 'siir'},
    {'name': 'Biyografi', 'icon': 'fa-solid fa-user-pen', 'slug': 'biyografi'},
    {'name': 'Yemek', 'icon': 'fa-solid fa-utensils', 'slug': 'yemek'},
]

for category in categories:
    Category.objects.create(**category)

print("Kategoriler başarıyla eklendi!") 