from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def novo_pet(request):
    if request.mothod == "GET":
        return render(request, 'novo_pet.html')
