# your_app/urls.py

from django.urls import path
from .views import RegisterView, CustomTokenObtainPairView, UserListView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('userlist', UserListView.as_view(), name='userlist'),
]
