from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

__all__ = [
    "about_view",
    "api_example",
    "home_view",
    "test_view",
]


def test_view(request):
    return HttpResponse("View di prova con HttpResponse.")


def home_view(request):
    return render(request, "home.html")


def about_view(request):
    return render(request, "about.html")


def api_example(request):
    data = {
        "nome": "Alessandro",
        "email": "alessandro.grandi@pythec.it",
    }
    return JsonResponse(data)