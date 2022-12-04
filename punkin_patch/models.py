from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=100, unique=True)

class PatchTemplate(models.Model):
    name = models.CharField(max_length=100, unique=True)

class Vote(models.Model):
    def validate_different_characters(self, c1, c2):
        if c1 == c2:
            raise ValidationError("{} is the same as {}".format(c1, c2))

    def validate_winner_exists(self, winner, c1, c2):
        if not (winner == c1 or winner == c2):
            raise ValidationError("Winner: {} is not {} or {}".format(winner, c1, c2))

    def clean(self):
        self.validate_different_characters(self.characterID1, self.characterID2)
        self.validate_winner_exists(self.winningCharacterID, self.characterID1, self.characterID2)

    characterID1 = models.ForeignKey(
        "Character", on_delete=models.CASCADE, related_name="character1"
    )
    characterID2 = models.ForeignKey(
        "Character", on_delete=models.CASCADE, related_name="character2"
    )
    winningCharacterID = models.ForeignKey(
        "Character", on_delete=models.CASCADE, related_name="winningCharacter"
    )

class CharacterPatch(models.Model):

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['characterID', 'patchID'], name='One instance of character per patch')
        ]

    characterID = models.ForeignKey(
        "Character", on_delete=models.CASCADE
    )
    patchID = models.ForeignKey(
        "PatchTemplate", on_delete=models.CASCADE
    )

class VotePatchResult(models.Model):

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['voteID', 'patchResultsID'], name='No duplicate votes in patch results')
        ]

    def validate_characters_in_patch(self, characters, patch):
        charactersInPatch = CharacterPatch.objects.filter(patchID=patch).only("characterID")
        for character in characters:
            if not character in charactersInPatch:
                raise ValidationError("Character: {} is not in Patch: {}".format(character, patch))

    def clean(self):
        vote = Vote.objects.get(pk=self.voteID)
        characters = [vote.characterID1, vote.characterID2]
        patch = PatchResults.objects.get(pk=self.patchResultsID).patchID
        self.validate_characters_in_patch(characters, patch)

    voteID = models.ForeignKey(
        "Vote", on_delete=models.CASCADE
    )
    patchResultsID = models.ForeignKey(
        "PatchResults", on_delete=models.CASCADE
    )

class PatchResults(models.Model):

    name = models.CharField(max_length=100, unique=True)
    patchID = models.ForeignKey(
        "PatchTemplate", on_delete=models.CASCADE
    )