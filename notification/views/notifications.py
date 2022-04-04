from rest_framework import generics,mixins,viewsets
from notification.serializers.notification import NotificationSerializers
from notification.models.notification import Notification

class NotificationViewSet(
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet
):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializers