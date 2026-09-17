from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GrupoViewSet, MaterialViewSet

router = DefaultRouter()
router.register(r'grupos', GrupoViewSet)
router.register(r'materiais', MaterialViewSet)

urlpatterns = [
    path('', include(router.urls)),

]