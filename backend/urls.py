from django.urls import path
from .views import FeedView, PostListCreateView, TestAuthView, RegisterView, AllUsersView, ProfileView, FollowToggleView, LikeToggleView, PostDetailView, CommentListCreateView, CommentDetailView, UserSearchView, NotificationListView, NotificationMarkReadView, NotificationUnreadCountView, ConversationListView, ConversationDetailView, ConversationCreateView, MessageCreateView, MessageMarkReadView
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
    path('search/users/', UserSearchView.as_view(), name='user-search'),
    path('notifications/', NotificationListView.as_view(), name='notifications'),
    path('notifications/<int:notification_id>/read/', NotificationMarkReadView.as_view(), name='notification-mark-read'),
    path('notifications/unread-count/', NotificationUnreadCountView.as_view(), name='notification-unread-count'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('follow/<int:user_id>/', FollowToggleView.as_view(), name='follow-toggle'),
    path('posts/', PostListCreateView.as_view(), name='posts'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:post_id>/like/', LikeToggleView.as_view(), name='like-toggle'),
    path('posts/<int:post_id>/comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('posts/<int:post_id>/comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
    path('feed/', FeedView.as_view(), name='feed'),
    path('conversations/', ConversationListView.as_view(), name='conversations'),
    path('conversations/create/', ConversationCreateView.as_view(), name='conversation-create'),
    path('conversations/<int:conversation_id>/', ConversationDetailView.as_view(), name='conversation-detail'),
    path('conversations/<int:conversation_id>/messages/', MessageCreateView.as_view(), name='message-create'),
    path('conversations/<int:conversation_id>/mark-read/', MessageMarkReadView.as_view(), name='message-mark-read'),
]