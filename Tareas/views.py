from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from .serializers import RegistroUsuarioSerializer, TareasSerializer, PerfilUsuarioSerializer
from .models import Tareas

# Create your views here.
class RegistroView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RegistroUsuarioSerializer

class PerfilUsuarioView(generics.RetrieveAPIView):
    serializer_class = PerfilUsuarioSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

class TareasViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TareasSerializer

    def get_queryset(self):
        query_set = Tareas.objects.filter(owner=self.request.user)
        completed = self.request.query_params.get('completed')
        if completed in ('true', 'false'):
            query_set = query_set.filter(completed=(completed == 'true'))
        return query_set
    

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)