from rest_framework.routers import DefaultRouter
from .views import RecruteurViewSet

router = DefaultRouter()
router.register(r'', RecruteurViewSet, basename='recruteur')

urlpatterns = router.urls
