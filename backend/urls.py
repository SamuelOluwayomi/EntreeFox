from django.urls import path
from .views import FeedView, PostListCreateView, TestAuthView, RegisterView, AllUsersView, ProfileView, FollowToggleView, LikeToggleView, PostDetailView, CommentListCreateView, CommentDetailView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('test-auth/', TestAuthView.as_view(), name='test_auth'),
    path('register/', RegisterView.as_view(), name='register'),
    path('all-users/', AllUsersView.as_view(), name='all-users'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('follow/<int:user_id>/', FollowToggleView.as_view(), name='follow-toggle'),
    path('posts/', PostListCreateView.as_view(), name='posts'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:post_id>/like/', LikeToggleView.as_view(), name='like-toggle'),
    path('posts/<int:post_id>/comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
    path('feed/', FeedView.as_view(), name='feed'),
]