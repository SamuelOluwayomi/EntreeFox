from django.urls import path
from .views import TestAuthView, RegisterView, AllUsersView, ProfileView, FollowToggleView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('test-auth/', TestAuthView.as_view(), name='test_auth'),
    path('register/', RegisterView.as_view(), name='register'),
    path('all-users/', AllUsersView.as_view(), name='all-users'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('follow/<int:user_id>/', FollowToggleView.as_view(), name='follow-toggle'),
]