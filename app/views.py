from django.shortcuts import redirect, render


def index(request):
    context= {}
    return render(request, 'index.html', context)