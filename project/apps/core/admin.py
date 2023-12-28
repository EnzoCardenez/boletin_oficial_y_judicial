from django.contrib import admin
from django.utils import timezone
from django.utils.translation import gettext as _

from . import filters


class PublicadoAdmin(admin.ModelAdmin):
    actions = ['publicar', 'no_publicar']

    def publicar(self, request, queryset):
        updated_records = queryset.update(publicado=timezone.now())
        message = _('updated records %s' % updated_records)
        self.message_user(request, message)

    publicar.short_description = 'Publicar los registros seleccionados'

    def no_publicar(self, request, queryset):
        registros_actualizados = queryset.update(publicado=None)
        mensaje = f'Registros actualizados {registros_actualizados}'
        self.message_user(request, mensaje)

    no_publicar.short_description = 'No publicar los registros seleccionados'

    def get_list_display(self, request):
        return list(super().get_list_display(request)) + ['publicado']

    def get_list_filter(self, request):
        list_filter = [filters.PublicadoListFilter] + list(super().get_list_filter(request))
        return list_filter
