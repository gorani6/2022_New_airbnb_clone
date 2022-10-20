from django.contrib import admin
from .models import Room, Amenity

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = (
        "name", "price", "kind", "owner", "created_at",
        "updated_at",
    )

    list_filter = (
        "country",
        "city",
        "pet_frienddly",
        "kind",
        "amenities",
        "created_at",
        "updated_at",
        
    )
    verbose_name_plural = "Amenities" #admin name 변경

@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "description",
        "created_at",
        "updated_at",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )
