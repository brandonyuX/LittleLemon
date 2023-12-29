from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.generics import ListCreateAPIView,RetrieveAPIView,DestroyAPIView
from django.contrib.auth.models import User
from .models import Menu,Booking
from .serierlizers import UserSerierlizer, MenuSerializer,BookingSerializer

# Create your views here.
def index(request):
    return render(request,"index.html",{})

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerierlizer
    permission_classes = [permissions.IsAuthenticated] 

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

class MenuItemView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
class SingleMenuItemView (RetrieveAPIView, DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer