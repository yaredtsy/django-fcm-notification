from pydoc_data.topics import topics
from firebase_admin import messaging

def send_push_notification_token(notification):
    try:
        message = messaging.Message(
            notification=messaging.Notification(
                title=notification.title,
                body=notification.body
            ),
            token=notification.token
        )
        response = messaging.send(message)
        notification.success = True
        notification.save()
    except Exception as e:
        notification.success = False
        notification.save()

def send_push_notification_topic(notification):
    message = messaging.Message(
            notification=messaging.Notification(
                title=notification.title,
                body=notification.body
            ),
            topic=notification.token
    )
    reponse = messaging.send(message)
    notification.success = True
    notification.save()