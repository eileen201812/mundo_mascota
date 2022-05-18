from django.shortcuts import render

def contacto_index(request):
    print('contacto_index')
    return render(request, 'contacto.html')