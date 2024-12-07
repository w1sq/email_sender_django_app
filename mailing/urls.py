from django.urls import path

from .views import SendMailingView

urlpatterns = [
    path("send/<int:pk>/", SendMailingView.as_view(), name="send-mailing"),
]
