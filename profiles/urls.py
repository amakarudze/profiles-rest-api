from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import HelloAPIView, HelloViewSet, ProfileFeedViewSet, UserProfileViewSet, UserLoginAPIView

router = DefaultRouter()
router.register('hello', HelloViewSet, basename='hello-view')
router.register('profile', UserProfileViewSet)
router.register('feed', ProfileFeedViewSet)

urlpatterns = [
    path('hello-api/', HelloAPIView.as_view()),
    path('login/', UserLoginAPIView.as_view()),
    path('', include(router.urls))
]
