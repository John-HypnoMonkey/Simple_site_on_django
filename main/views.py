from django.shortcuts import render

# Create your views here.
def home(request):
    """Renders a main page for the site"""
    return render(request, "main/home.html")


def tutorial(request):
    """Renders a tutorial page"""
    return render(request, "main/tutorial.html")


def about(request):
    """Renders an about page"""
    return render(request, "main/about.html")
