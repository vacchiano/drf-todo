from django.http import JsonResponse
from django.shortcuts import render

def test_view(request):
    data = {
        'name': "Dom",
        'age': 27
    }
    return JsonResponse(data)
