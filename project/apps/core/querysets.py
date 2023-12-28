from django.db.models import QuerySet


class PublicadoQuerySet(QuerySet):
    def get_queryset(self):
        return self.filter(publicado__isnull=False)
