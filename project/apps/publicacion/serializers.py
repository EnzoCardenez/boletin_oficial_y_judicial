from rest_framework_json_api import serializers

from .models import Fecha, Publicacion
from .count import palabra, copias

from usuario.serializers import UsuarioDetalleSerializer


class FechaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fecha
        fields = serializers.ALL_FIELDS


class PublicacionSerializer(serializers.ModelSerializer):
    fecha_publicacion = FechaSerializer(read_only=True, required=False, allow_null=True)

    class Meta:
        model = Publicacion
        fields = (
            'uuid',
            'estado',
            'cuerpo_publicacion',
            'palabras',
            'dias_de_publicacion',
            'sellos',
            'copias_requeridas',
            'cantidad_de_copias',
            'cuil',
            'archivo',
            'creado_por',
            'fecha_creacion',
            'fecha_modificacion',
            'fecha_publicacion',
            'modificado_por',

        )

    included_serializers = {
        'creado_por': UsuarioDetalleSerializer,
        'modificado_por': UsuarioDetalleSerializer,

    }

    def validate(self, data):
        request = self.context['request']
        if request.method == 'POST':
            data['creado_por'] = request.user
        data['modificado_por'] = request.user
        return data

    @staticmethod
    def create(validated_data):
        publicacion_data = {
            'cuerpo_publicacion': validated_data['cuerpo_publicacion'],
            'palabras': palabra(validated_data.get('cuerpo_publicacion', '')),
            'sellos': validated_data['sellos'],
            'archivo': validated_data['archivo'],
            'dias_de_publicacion': validated_data['dias_de_publicacion'],
            'copias_requeridas': validated_data['copias_requeridas'],
            'cantidad_de_copias': copias(
                validated_data.get('dias_de_publicacion', ''),
                validated_data.get('copias_requeridas', '')
                                         ),
            'creado_por': validated_data['creado_por'],
            'modificado_por': validated_data['modificado_por'],
        }
        publicacion = Publicacion.objects.create(**publicacion_data)

        return publicacion




