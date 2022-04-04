from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views.notifications import NotificationViewSet

router = DefaultRouter()

router.register('',NotificationViewSet)

urlpatterns = [
    path('', include(router.urls),name='notification'),
]

