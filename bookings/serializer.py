from django.utils import timezone
from rest_framework import serializers 
from .models import Booking

class CreateRoomBookingSerializer(serializers.ModelSerializer):

    check_in = serializers.DateField()
    check_out = serializers.DateField()

    class Meta:
        model = Booking
        fields = [
            "check_in",
            "check_out",
            "guests",
        ]

    def validate_check_in(self, value):
        now = timezone.localtime(timezone.now()).date()
        if now > value:
            raise serializers.ValidationError("Can't book in the past")
        return value

    def validate_check_out(self, value):
        now = timezone.localtime(timezone.now()).date()
        if now > value:
            raise serializers.ValidationError("Can't book in the past")
        return value

    def validate(self, data):
        if data['check_out'] <= data['chek_in']:
            raise serializers.ValidationError("OMG") 
    
        if Booking.objects.filter(
            check_in__lte=data["chek_out"],
            check_out__gte=data["check_in"],
        ).exists():
            raise serializers.ValidationError("dates are already taken")
        return data




class PublicBookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = (
            "pk",
            "check_in",
            "check_out",
            "experience_time",
            "guests",
        )

