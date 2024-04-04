from django.shortcuts import render


def my_view(request):
    name = "Arni"
    return render(request, 'index.html', {'name': name})
