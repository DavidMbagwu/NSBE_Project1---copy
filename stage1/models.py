from django.contrib.auth.models import AbstractUser
from django.db import models
from . import choices
from django.core.exceptions import ValidationError


class Member(AbstractUser):
    mcneese_id = models.CharField(
        primary_key=True, unique=True, max_length=9, blank=False
    )
    linkedin = models.URLField(max_length=200, blank=True, null=True, unique=True)
    major = models.CharField(max_length=200, choices=choices.MAJOR_CHOICES)
    class_standing = models.CharField(
        max_length=100, choices=choices.CLASS_STANDING_CHOICES
    )
    nationality = models.CharField(
        max_length=100, blank=True, null=True, choices=choices.COUNTRY_CHOICES
    )
    race = models.CharField(max_length=100, choices=choices.RACE_CHOICES)
    gender = models.CharField(
        max_length=100, blank=True, null=True, choices=choices.GENDER_CHOICES
    )

    # Optional fields (for now)
    birthdate = models.DateField(null=True, blank=True)
    avatar = models.ImageField(
        null=True, blank=True, upload_to="images", verbose_name="Profile Picture"
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def clean(self):
        super().clean()
        # Ensure McNeese ID is 9 characters long
        if len(self.mcneese_id) != 9:
            raise ValidationError(
                {"mcneese_id": "McNeese ID must be exactly 9 characters long."}
            )

        # Ensure users sign up only with McNeese email
        if not self.email.endswith("@mcneese.edu"):
            raise ValidationError(
                {"email": "Please Sign up with your McNeese school email"}
            )

        # Ensure the input linkedin is valid
