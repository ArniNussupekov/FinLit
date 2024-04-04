from django.shortcuts import render


def my_view(request):
    name = "йй"
    return render(request, 'index.html', {'name': name})
