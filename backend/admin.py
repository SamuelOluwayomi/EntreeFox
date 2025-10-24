from django.contrib import admin
from .models import Follow, User, Post

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'username',
        'email',
        'followers_count',
        'following_count',
        'is_staff',
        'is_superuser'
    )
    search_fields = ('username', 'email')
    list_filter = ('is_staff', 'is_superuser')

    def followers_count(self, obj):
        return obj.followers.count()

    def following_count(self, obj):
        return obj.following.count()

    followers_count.short_description = 'Followers'
    following_count.short_description = 'Following'

@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('id', 'follower', 'following', 'created_at')
    search_fields = ('follower__username', 'following__username')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'content', 'image', 'video', 'location', 'emojis', 'created_at')
    search_fields = ('author__username', 'content')
    list_filter = ('created_at',)