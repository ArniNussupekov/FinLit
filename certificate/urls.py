from rest_framework.routers import DefaultRouter

from certificate.views import CertificateViewSet


router = DefaultRouter()
router.register(r'', CertificateViewSet, basename='certificate')
urlpatterns = router.urls