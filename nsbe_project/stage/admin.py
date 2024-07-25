from django.contrib import admin
from .models import Event, Member, Post


# Register your models here.
admin.site.register(Event)
admin.site.register(Member)
admin.site.register(Post)