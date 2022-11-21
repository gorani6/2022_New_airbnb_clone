from rest_framework import serializers
from users.serializers import TinyUserSrializer
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):

    user = TinyUserSrializer(read_only=True)

    class Meta:
        model = Review
        fields = ("user", "payload", "rating",)