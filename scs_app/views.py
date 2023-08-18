from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')

def main(request):
    return render(request, 'main.html')

def reserves(request):
    return render(request, 'reserves.html')