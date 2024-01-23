from rest_framework import routers

from usuario import api as usuario_api

# Define routes
router = routers.DefaultRouter()

router.register(prefix='usuario', viewset=usuario_api.UsuarioViewset)
