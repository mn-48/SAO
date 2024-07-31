# your_app/views.py

from rest_framework import generics
from .models import User
from .serializers import UserSerializer, CustomTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.pagination import PageNumberPagination


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class UserListPagination(PageNumberPagination):
    page_size = 2  # Number of objects per page
    page_size_query_param = 'page_size'  # Allow client to set the page size via query parameters
    max_page_size = 100  # Maximum limit for page size set by the client


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = UserListPagination  # Specify the custom pagination class
 
