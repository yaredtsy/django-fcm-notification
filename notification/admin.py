from django.contrib import admin
from .models.notification import Notification

# Register your models here.

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'body','success','notication_type')
    list_filter = ('success', 'notication_type')

admin.site.register(Notification,NotificationAdmin)