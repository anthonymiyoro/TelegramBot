from django.contrib import admin
from stories.models import Story

# Register your models here

class StoryAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'domain', 'moderator', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('title', 'moderator__username', 'moderator__first_name')

admin.site.register(Story, StoryAdmin)

