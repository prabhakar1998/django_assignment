from rest_framework import serializers

from service_area.models import ServiceArea, ServiceProvider


class ServiceProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceProvider
        fields = (
            "id",
            "name",
            "email",
            "phone_number",
            "language",
            "currency",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("created_at", "updated_at")


class ServiceAreaSerializer(serializers.ModelSerializer):

    provider_name = serializers.SerializerMethodField()

    def get_provider_name(self, obj):
        return str(obj.service_provider)

    class Meta:
        model = ServiceArea
        fields = (
            "id",
            "service_provider",
            "provider_name",
            "name",
            "price",
            "service_area",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("created_at", "updated_at", "provider_name")
