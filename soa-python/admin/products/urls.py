from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, UserAPIView

# Create the router and register viewsets
router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')

# Define URL patterns
urlpatterns = [
    path('user/', UserAPIView.as_view(), name='user_api'),
]

# Include router URLs
urlpatterns += router.urls
