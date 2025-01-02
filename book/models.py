from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50)  # Font Awesome ikon class'ı için
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

