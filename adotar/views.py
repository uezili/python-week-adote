from django.shortcuts import render

# Create your views here.


def listar_pets(request):
    if request.method == 'GET':
        return render(request, 'listar_pets.html')
