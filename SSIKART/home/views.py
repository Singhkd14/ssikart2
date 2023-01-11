from django.shortcuts import render, HttpResponse



def sec(request):
    return render(request, "home.html")

def about(request):
    return HttpResponse("<h1>E-commerce site by KD Singh<h1>")



