from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListCreateAPIView,RetrieveAPIView,DestroyAPIView
from .models import Menu,Booking
from .serierlizers import MenuSerializer,BookingSerializer

# Create your views here.
def index(request):
    return render(request,"index.html",{})


class MenuItemView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class SingleMenuItemView (RetrieveAPIView, DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer