
import re
from urllib import request
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from .models import Carrera, Curso, Estudiante, Matricula
from .serializers import CarreraSerializer, CursoSerializer, EstudianteSerializer, MatriculaSerializer






class CarreraViewSet(viewsets.ModelViewSet):
    queryset=Carrera.objects.all()
    serializer_class=CarreraSerializer


class EstudianteViewSet(viewsets.ModelViewSet):
    queryset=Estudiante.objects.all()
    serializer_class=EstudianteSerializer


class CursoViewSet(viewsets.ModelViewSet):
    queryset=Curso.objects.all()
    serializer_class=CursoSerializer


class MatriculaViewSet(viewsets.ModelViewSet):
    queryset=Matricula.objects.all()
    serializer_class=MatriculaSerializer




@api_view(["GET"])
def carrera_contador(request):
    """
    Cantidad de items, ACCES ROL: ANONYMUS}
    Cantidad de items registrados en carrera
    """

    try:
        
        cantidad=Carrera.objects.count()
        return JsonResponse(
            {
                "cantidad":cantidad
            },
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse(
            {
                "message":str(e)
            },
            status=400
        )