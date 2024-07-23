from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from . import choices
from django.core.exceptions import ValidationError

# Create your models here.

# Important Codes:
# python manage.py migrate --run-syncdb (for clearing and refreshin database changes which usually lead to 'Coloumn not found' errors)

class Member(AbstractUser):
    #first_name = models.CharField(max_length=64, blank=True, null=True)
    #last_name = models.CharField(max_length=64, blank=True, null=True)
    mcneese_id = models.CharField( max_length=9,editable=True, unique=True, blank=False)
    linkedin = models.URLField(max_length=50, default='http://www.linkedin.com')
    pointsum = models.IntegerField(blank = True, null=True)
    major = models.CharField(max_length=200, choices=choices.MAJOR_CHOICES)
    class_standing = models.CharField(
        max_length=100, choices=choices.CLASS_STANDING_CHOICES, default = 'Freshman'
    )
    nationality = models.CharField(
        max_length=100, blank=True, null=True, choices=choices.COUNTRY_CHOICES
    )
    race = models.CharField(max_length=100, choices=choices.RACE_CHOICES, default=None, null=True)
    gender = models.CharField(
        max_length=100, blank=True, null=True, choices=choices.GENDER_CHOICES
    )

    # Optional fields (for now)
    phone = models.IntegerField(blank = True, null=True)
    birthdate = models.DateField(null=True, blank=True)
    avatar = models.ImageField(
        null=True, blank=True, upload_to="images", verbose_name="Profile Picture"
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def clean(self):
        super().clean()

        # Ensure users sign up only with McNeese email
        if not self.email.endswith("@mcneese.edu"):
            raise ValidationError(
                {"email": "Please Sign up with your McNeese school email"}
            )

class Post(models.Model):
    member = models.ManyToManyField(Member, related_name= 'points')
    event = models.CharField(max_length = 100)
    description = models.TextField()
    points = models.IntegerField()
    date_event = models.DateField(default = timezone.now)


    def __str__(self):
        return self.event