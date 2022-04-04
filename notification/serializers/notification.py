from rest_framework import serializers
from notification.models.notification import Notification

class NotificationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ('id','title','body','notication_type','success','token','created_date')
        extra_kwargs = {'success': {'read_only': True},'created_date':{'read_only': True}}