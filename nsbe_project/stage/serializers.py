from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    attendees = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    start_time = serializers.DateTimeField(format="%a, %b %-d, %Y, %I: %M")
    end_time = serializers.DateTimeField(format="%I: %M  %p")
    
    class Meta:
        model = Event
        fields = ["id", "title", "slug", "description", "location", "start_time", "end_time", "created_at", "updated_at", "attendees"]