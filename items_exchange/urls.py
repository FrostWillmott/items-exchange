from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from ads.views import AdViewSet, ExchangeProposalViewSet

router = DefaultRouter()
router.register(r'ads', AdViewSet, basename='ad')

router.register(r'exchange-proposals', ExchangeProposalViewSet, basename='exchangeproposal')

schema_view = get_schema_view(
   openapi.Info(
      title="API Документация",
      default_version='v1',
      description="Описание API для проекта обмена объявлениями",
      contact=openapi.Contact(email="i.tkachenko@zohomail.eu"),
   ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

]
