
from django.contrib import admin
from .models import Forum, Discussion
# Register your models here.
@admin.register(Forum)
class ForumAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'topic']
    list_filter = ['name']

@admin.register(Discussion)
class DiscussionAdmin(admin.ModelAdmin):
    list_display = ['forum']