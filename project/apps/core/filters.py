from django.contrib import admin
from django.utils.translation import gettext as _


# Filters Admin

class PublicadoListFilter(admin.SimpleListFilter):
    title = 'Publicado'

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'publicado'

    def lookups(self, request, model_admin):
        return (
            ('true', 'Publicados'),
            ('false', 'No Publicados'),
        )

    def queryset(self, request, queryset):
        value = self.value()
        if value:
            return queryset.exclude(publicado__isnull=value == 'true')

        return queryset.all()


# DRF Filter Common.
def filter_unaccent_contains(queryset, name, value):
    # TODO: add unaccent within the join list.
    lookup = '__'.join([name, 'icontains'])
    return queryset.filter(**{lookup: value})
