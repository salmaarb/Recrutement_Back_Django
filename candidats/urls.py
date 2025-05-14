from rest_framework.routers import DefaultRouter
from .views import CandidatViewSet

router = DefaultRouter()
router.register(r'', CandidatViewSet, basename='candidat')

urlpatterns = router.urls
