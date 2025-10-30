from rest_framework import serializers
from .models import Post, User, Comment, Notification, Conversation, Message

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'bio', 'profile_pic']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
    
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'profile_pic', 'is_staff', 'is_superuser']

class UserProfileSerializer(serializers.ModelSerializer):

    followers_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'profile_pic', 'followers_count', 'following_count']
        read_only_fields = ['id', 'username', 'email']

    def get_followers_count(self, user):
        return user.followers.count()

    def get_following_count(self, user):
        return user.following.count()
    
class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    likes_count = serializers.SerializerMethodField()
    user_has_liked = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'id', 'author', 'content', 'image', 'video', 'location', 'emojis', 'created_at',
            'likes_count', 'user_has_liked'
        ]
        read_only_fields = ['id', 'author', 'created_at']

    def get_likes_count(self, post):
        return post.likes.count()

    def get_user_has_liked(self, post):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return post.likes.filter(user=request.user).exists()
        return False

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = ['id', 'author', 'content', 'created_at']
        read_only_fields = ['id', 'author', 'created_at']

class NotificationSerializer(serializers.ModelSerializer):
    actor = serializers.ReadOnlyField(source='actor.username')
    post_id = serializers.IntegerField(source='post.id', read_only=True)

    class Meta:
        model = Notification
        fields = ['id', 'actor', 'notification_type', 'post_id', 'is_read', 'created_at']
        read_only_fields = ['id', 'actor', 'post_id', 'created_at']

class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.ReadOnlyField(source='sender.username')

    class Meta:
        model = Message
        fields = ['id', 'sender', 'content', 'is_read', 'created_at']
        read_only_fields = ['id', 'sender', 'created_at']

class ConversationSerializer(serializers.ModelSerializer):
    participants = serializers.SerializerMethodField()
    last_message = serializers.SerializerMethodField()
    unread_count = serializers.SerializerMethodField()

    class Meta:
        model = Conversation
        fields = ['id', 'participants', 'last_message', 'unread_count', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def get_participants(self, conversation):
        return [{'id': user.id, 'username': user.username} for user in conversation.participants.all()]

    def get_last_message(self, conversation):
        last_msg = conversation.messages.last()
        if last_msg:
            return MessageSerializer(last_msg).data
        return None

    def get_unread_count(self, conversation):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return conversation.messages.filter(is_read=False).exclude(sender=request.user).count()
        return 0