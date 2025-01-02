from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta

class Category(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    image = models.ImageField(upload_to='books/images/', null=True, blank=True)
    pdf = models.FileField(upload_to='books/pdfs/', null=True, blank=True)
    categories = models.ManyToManyField(Category, related_name='books')
    page = models.IntegerField()

    def __str__(self):
        return self.name

    def is_english(self):
        return self.categories.filter(name='İngilizce').exists()

class WordNote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    english_word = models.CharField(max_length=100)
    turkish_meaning = models.CharField(max_length=200)
    page_number = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.english_word} - {self.turkish_meaning}"

