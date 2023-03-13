from django.urls import path
from .views import ApplicationApiView

# 127.0.0.1:8000/application/
urlpatterns = [
    path("application/", ApplicationApiView.as_view())
]