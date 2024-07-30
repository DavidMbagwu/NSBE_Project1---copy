from rest_framework import serializers
from .models import Event, Member

class EventSerializer(serializers.ModelSerializer):
    attendees = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    start_time = serializers.DateTimeField(format="%a, %b %-d, %Y, %I: %M")
    end_time = serializers.DateTimeField(format="%I: %M  %p")
    is_member_registered = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = ["id", "title", "slug", "description", "location", "start_time", "end_time", "created_at", "updated_at", "attendees", "is_member_registered"]

    def get_is_member_registered(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.attendees.filter(id=request.user.id).exists()
        return False

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = [
            'id', 'username', 'email', 'mcneese_id', 'linkedin', 'pointsum',
            'major', 'class_standing', 'nationality', 'race', 'gender',
            'phone', 'birthdate', 'avatar', 
        ]