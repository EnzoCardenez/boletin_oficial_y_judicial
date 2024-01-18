from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Usuario
from .serializers import UsuarioSerializer, UsuarioDetalleSerializer
from core.permission import CustomModelPermissions
# Create your views here.


class UsuarioViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    lookup_field = 'id'
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == 'list':
            return UsuarioDetalleSerializer
        return self.serializer_class

    def get_object(self):
        usuario = self.request.user
        if self.kwargs.get('pk') != 'me' and usuario.is_superuser:
            usuario = super().get_object()
        return usuario

    def get_permission(self):
        permission_classes = self.permission_classes
        if self.action == 'list':
            permission_classes = [CustomModelPermissions]

        return [permission() for permission in permission_classes]
