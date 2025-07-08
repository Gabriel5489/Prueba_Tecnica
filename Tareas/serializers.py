from rest_framework import serializers
from .models import Tareas
from django.contrib.auth import get_user_model

Usuario = get_user_model()

class TareasSerializer(serializers.ModelSerializer):
    title = serializers.CharField(min_length=3)

    class Meta:
        model = Tareas
        fields = ('id', 'title', 'description', 'completed', 'created_at', 'owner')
        read_only_fields = ('id', 'created_at', 'owner')

class RegistroUsuarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8, max_length=30)

    class Meta:
        model = Usuario
        fields = ('id', 'username', 'email', 'password')

    def validate_email(self, value):
        if Usuario.objects.filter(email=value).exists():
            raise serializers.ValidationError("El email ya está siendo usado por otro usuario")
        return value
    
    def create(self, validated_data):
        return Usuario.objects.create_user(username=validated_data['username'], email=validated_data['email'], password=validated_data['password'])
    
class PerfilUsuarioSerializer(serializers.ModelSerializer):
    username = serializers.CharField(read_only=True)

    class Meta:
        model = Usuario
        fields = ('id', 'username', 'email', 'password', 'is_active')