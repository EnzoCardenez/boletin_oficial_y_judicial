from django.db.models import Q
from django_filters import rest_framework as filters

import django_filters

from .models import Usuario


class UsuarioFilter(filters.FilterSet):
    class Meta:
        model = Usuario
        fields = ('last_name',)

    Filtro = filters.CharFilter(method='buscar_usuario', label='Buscar usuario')
    es_boletin = django_filters.BooleanFilter(field_name='es_boletin')

    @staticmethod
    def buscar_usuario(queryset, name, value):

        value = value.strip()
        query = Q(last_name__icontains=value) | Q(first_name__icontains=value) | Q(username__icontains=value)

        return queryset.filter(query)
