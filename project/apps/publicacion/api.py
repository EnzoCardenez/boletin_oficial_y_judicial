from rest_framework import viewsets, mixins, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend


from .models import Publicacion
from .serializers import PublicacionSerializer


class PublicacionViewset(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Publicacion.objects.all()
    serializer_class = PublicacionSerializer
    permission_classes = [IsAuthenticated,]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = [
        'fecha_publicacion',
        'fecha_modificacion',
        'creado_por',
        'modificado_por',
        'id',
        ]
    lookup_field = 'uuid'
