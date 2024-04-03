from django.urls import path
from django.http import HttpResponse
from recipes.views import home

def my_view(request):
    return HttpResponse('UMA LINDA STRING')

urlpatterns = [
    path('', home),
]