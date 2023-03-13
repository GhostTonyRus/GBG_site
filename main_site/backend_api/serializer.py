from rest_framework import serializers
from .models import Application

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = [
            "full_name", "phone_number", "email",
            "landing_page", "business_card_website", "corporate_website", "whim",
            "less_than_five_hundred_thousand", "less_than_million", "more_than_million", "arbitrary_option",
            "about_project"
        ]