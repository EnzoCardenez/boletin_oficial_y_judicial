from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from .models import Usuario
from .serializers import UsuarioSerializer, UsuarioDetalleSerializer
from .filters import UsuarioFilter
from core.permission import CustomModelPermissions
# Create your views here.


class UsuarioViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filter_class = UsuarioFilter
    ordering_fields = ('first_name', 'last_name',)
    ordering = ('last_name', )

    def get_object(self):
        usuario = self.request.user
        if self.kwargs.get('pk') != 'me' and usuario.is_superuser:
            usuario = super().get_object()
        return usuario

    def get_serializer_class(self):
        if self.action == 'list':
            return UsuarioDetalleSerializer
        return self.serializer_class

    def get_permission(self):
        permission_classes = self.permission_classes
        if self.action == 'list':
            permission_classes = [CustomModelPermissions]

        return [permission() for permission in permission_classes]
