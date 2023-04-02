from rest_framework import serializers
from .models import Application

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = [
            "full_name", "phone_number", "email",
            "service", "budget", "about_project",
        ]