from rest_framework_json_api import serializers

from .models import Usuario
from organismo.serializers import OrganismoSerializer


class UsuarioSerializer(serializers.ModelSerializer):
    user_permmisions = serializers.SerializerMethodField()

    class Meta:
        model = Usuario
        field = (
                 'username',
                 'first_name',
                 'last_name',
                 'email',
                 'organismo',
                 'es_boletin',
                 'permission',
                 )

    included_serializer = {
        'organismo': OrganismoSerializer,
    }

    @staticmethod
    def get_user_permissions(instance):
        return instance.user_permissions.all()


class UsuarioDetalleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        field = (
            'username',
            'first_name',
            'last_name',
            'es_boletin',
            )
