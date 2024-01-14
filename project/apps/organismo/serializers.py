from rest_framework_json_api import serializers

from .models import Organismo


class OrganismoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organismo
        field = serializers.ALL_FIELDS
