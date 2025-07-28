from django.shortcuts import render


def Home(request):       
    
    return render(request, 'home.html')

def Segunda(request):
    
    return render(request, 'segunda.html')