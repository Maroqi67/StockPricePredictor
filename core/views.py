from django.shortcuts import render

# Create your views here.

def equities(request):
    return render(request, 'equities.html')

def research(request):
    return render(request, 'research.html')

def about(request):
    return render(request, 'about.html')

def predictor(request):
    return render(request, 'predictor.html')