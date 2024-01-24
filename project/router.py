from rest_framework import routers

from usuario import api as usuario_api
from publicacion import api as publicacion_api

# Define routes
router = routers.DefaultRouter()

router.register(prefix='usuario', viewset=usuario_api.UsuarioViewset)
router.register(prefix=r'publicacion', viewset=publicacion_api.PublicacionViewset, basename='publicacion')
