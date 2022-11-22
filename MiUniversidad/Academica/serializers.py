from dataclasses import field, fields

from pyexpat import model
from rest_framework import serializers
from .models import Carrera, Curso, Estudiante, Matricula


class CarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model=Carrera
        fields="__all__"


class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Estudiante
        fields="__all__"


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Curso
        fields="__all__"


class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Matricula
        fields="__all__"


