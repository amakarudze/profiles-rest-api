from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import HelloAPIView, HelloViewSet

router = DefaultRouter()
router.register('hello-view', HelloViewSet, basename='hello-view')

urlpatterns = [
    path('hello-api/', HelloAPIView.as_view(), name='hello'),
    path('', include(router.urls))
]
