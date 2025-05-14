from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.views.generic import RedirectView

schema_view = get_schema_view(
   openapi.Info(
      title="API de Recrutement",
      default_version='v1',
      description="Documentation de l'API pour gestion des candidats et recruteurs",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), 
    path('api/candidats/', include('candidats.urls')),
    path('api/recruteurs/', include('recruteurs.urls')),
    path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', RedirectView.as_view(url='/api/swagger/', permanent=False)),  # 👈 redirection

]
