from rest_framework import serializers
from .models import Event, Category, Venue
# from users.serializers import UserSerializer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category 
        fields = [
            'name',
        ]

class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = [
            'name',
            'venue_website',
        ]

class EventSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)
    venue = VenueSerializer(read_only=True)
    # host = UserSerializer(read_only=True)
    class Meta:
        model = Event
        fields = [
            'name', 
            'description', 
            'start_time', 
            'end_time', 
            'category', 
            'venue', 
            'attendees',]
