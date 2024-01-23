from rest_framework_json_api import serializers

from .models import Fecha, Publicacion

from usuario.serializers import UsuarioDetalleSerializer


class FechaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fecha
        fields = serializers.ALL_FIELDS


class PublicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicacion
        fields = serializers.ALL_FIELDS

    included_serializers = {
        'creado_por': UsuarioDetalleSerializer,
        'modificado_por': UsuarioDetalleSerializer,

    }
