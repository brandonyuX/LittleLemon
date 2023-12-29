from django.urls import path,include
from rest_framework import routers
from restaurant import views
from .views import MenuItemView, SingleMenuItemView

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'booking', views.BookingViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('',include(router.urls))
]