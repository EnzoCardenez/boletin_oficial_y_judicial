from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

from .models import Usuario
from .serializers import UsuarioSerializer, UsuarioDetalleSerializer
# Create your views here.


class UsuarioViewset(viewsets.ReadOnlyModelViewSet):
        queryset = Usuario.objects.all()
        serializer_class = UsuarioSerializer
        lookup_field = 'id'
        permission_classes = [IsAuthenticated]

        @action(
                detail=False,
                methods=['get'],
                url_path='usuario-detalle',
                serializer_class=UsuarioDetalleSerializer
                )
        def detalle_usuario(self, request):
                user_id = request.query_params.get('id')
                if not user_id:
                        return Response({'error': 'Se requiere el parámetro "id" en la consulta.'},
                                        status=status.HTTP_400_BAD_REQUEST)
                try:
                        usuario = Usuario.objects.get(id=user_id)
                        serializer = UsuarioDetalleSerializer(usuario)
                        return Response(serializer.data, status=status.HTTP_200_OK)

                except Usuario.DoesNotExist:
                        return Response({'error': 'Usuario no encontrado.'}, status=status.HTTP_404_NOT_FOUND)
