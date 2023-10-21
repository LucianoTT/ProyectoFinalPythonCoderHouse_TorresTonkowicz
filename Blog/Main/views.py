from django.shortcuts import render

#funcion simple para renderizar el index/pagina principal.
def index (request):
    return render(request, r"main/index.html")

#función simple para renderizar el about me.
def about (request):
    return render(request, r"main/about.html")
