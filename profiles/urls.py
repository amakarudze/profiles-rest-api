from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import HelloAPIView, HelloViewSet, UserProfileViewSet

router = DefaultRouter()
router.register('hello-viewset', HelloViewSet, basename='hello-view')
router.register('profile-viewset', UserProfileViewSet)

urlpatterns = [
    path('hello-api/', HelloAPIView.as_view(), name='hello'),
    path('', include(router.urls))
]
