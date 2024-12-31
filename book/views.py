from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'book/index.html')

def login(request):
    return render(request, 'book/login.html')

def register(request):
    return render(request, 'book/register.html')
