from django.db import models
from general.models.created_modified import CreatedModified


class Notification(CreatedModified):
    NOTIFICATION_TYPE=[ 
        ('topic','topic'),  
        ('token','token') 
    ]

    title = models.CharField(max_length=30)
    body = models.TextField(max_length=30)
    notication_type = models.CharField(max_length=15,choices=NOTIFICATION_TYPE)

    success = models.BooleanField(default=False)
    token = models.CharField(max_length=200)