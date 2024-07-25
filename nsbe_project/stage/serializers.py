from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    attendees = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Event
        field = ["id", "title", "location", "desription", "attendees", "is_upcoming", "start", "end"]