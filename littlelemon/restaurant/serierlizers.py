from django.contrib.auth.models import User
from .models import Menu, Booking
from rest_framework import serializers

class UserSerierlizer(serializers.Serializer):
    class Meta:
        model = User
        fields = ['id','username','email']

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id','title', 'price', 'inventory']
    
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['name','no_of_guest', 'booking_date' ]