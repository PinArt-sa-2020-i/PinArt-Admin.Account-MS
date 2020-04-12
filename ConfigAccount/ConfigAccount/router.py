from rest_framework import routers
from Account.views import TipoNotificacionViewSet, ConfigNotificacionesViewSet, MedioViewSet, SesionesViewSet, CuentasEnlazadasViewSet

router = routers.DefaultRouter()

router.register(r'ConfigNotificaciones', ConfigNotificacionesViewSet)
router.register(r'TipoNotificaciones', TipoNotificacionViewSet)
router.register(r'Medio', MedioViewSet)
router.register(r'Sesiones', SesionesViewSet)
router.register(r'CuentasEnlazadas', CuentasEnlazadasViewSet)

#urlpatterns = router.urls