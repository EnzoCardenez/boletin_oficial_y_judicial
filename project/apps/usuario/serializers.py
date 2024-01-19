from rest_framework_json_api import serializers


from .models import Usuario
from organismo.serializers import OrganismoSerializer


class UsuarioSerializer(serializers.ModelSerializer):

    user_permissions = serializers.SerializerMethodField()

    class Meta:
        model = Usuario
        fields = (
                 'first_name',
                 'last_name',
                 'email',
                 'organismo',
                 'es_boletin',
                 'user_permissions',
                 )

    included_serializer = {
        'organismo': OrganismoSerializer,
    }

    @staticmethod
    def get_user_permissions(instance):
        return instance.get_all_permissions()


class UsuarioDetalleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        fields = (
            'username',
            'first_name',
            'last_name',
            'es_boletin',
            )
