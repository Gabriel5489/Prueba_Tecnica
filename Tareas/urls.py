from rest_framework import routers
from django.urls import path, include
from .views import TareasViewSet, RegistroView, PerfilUsuarioView

router = routers.DefaultRouter()

router.register(r'tareas', TareasViewSet, basename='tareas')

urlpatterns = [
    path('registro', RegistroView.as_view(), name='registro'),
    path('perfil', PerfilUsuarioView.as_view(), name='perfil'),

    path('', include(router.urls))
]