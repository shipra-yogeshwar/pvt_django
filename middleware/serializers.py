# Django Imports
from rest_framework import serializers

# My project Imports
from .models import Errorcode


class ErrorcodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Errorcode
        fields = ["id", "status_code", "message"]
