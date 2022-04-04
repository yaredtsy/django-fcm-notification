from django.db.models.signals import post_save
from .utils import firebase_fcm
from .models.notification import Notification
from django.dispatch import receiver

@receiver(post_save,sender=Notification)
def send_push_notification(sender,instance,created,**kwargs):
    if created:
        if instance.notication_type =='topic':
            firebase_fcm.send_push_notification_topic(instance)
        elif instance.notication_type == 'token':
            firebase_fcm.send_push_notification_token(instance)