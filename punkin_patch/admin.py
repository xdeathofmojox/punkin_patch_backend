from django.contrib import admin
from .models import Character, Vote, VotePatchResult, CharacterPatch, PatchResult, PatchTemplate

# Register your models here.
admin.site.register(Character)
admin.site.register(CharacterPatch)
admin.site.register(PatchResult)
admin.site.register(PatchTemplate)
admin.site.register(Vote)
admin.site.register(VotePatchResult)