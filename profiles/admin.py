from django.contrib import admin

from .models import ProfileFeedItem, UserProfile

admin.site.register(ProfileFeedItem)
admin.site.register(UserProfile)
