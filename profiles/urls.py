from django.urls import path

from .views import HelloAPIView

urlpatterns = [
    path('hello-api/', HelloAPIView.as_view(), name='hello'),
]
