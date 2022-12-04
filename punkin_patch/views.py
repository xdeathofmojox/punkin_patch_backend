from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from punkin_patch.models import Character
from django.http import JsonResponse

def punkinpatch(request):
    return HttpResponse("Hello World")

# Create your views here.
class CharactersView(View):

    def get(self, request):
        all_characters = list(Character.objects.values())
        return JsonResponse(all_characters, safe=False)