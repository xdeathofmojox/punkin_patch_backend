from django.http import HttpResponse
from django.views import View
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from punkin_patch.models import Character
from django.http import JsonResponse

def punkinpatch(request):
    return HttpResponse("Hello World")

# Create your views here.
class CharactersView(View):
    def get(self, request):
        all_characters = list(Character.objects.values())
        return JsonResponse(all_characters, safe=False)

class CharacterCreateView(CreateView):
    model = Character
    template_name = "character_form.html"
    fields = ['name']
    success_url = "/characters"

class CharacterUpdateView(UpdateView):
    model = Character
    template_name = "character_form.html"
    fields = ['name']
    success_url = "/characters"

class CharacterDeleteView(DeleteView):
    model = Character
    template_name = "character_form.html"
    success_url = "/characters"