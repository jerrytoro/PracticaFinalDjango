
from wsgiref.validate import validator
from django.db import models
from .validators import validar_ci, validar_codigo, validar_creditos
# Create your models here.


class Carrera(models.Model):
    codigo=models.CharField(max_length=3,primary_key=True,validators=[validar_codigo])
    nombre=models.CharField(max_length=50)
    duracion=models.PositiveSmallIntegerField(default=5)

    def __str__(self):
        txt="{0} (Duración: {1} año(S))"
        return txt.format(self.nombre, self.duracion)


class Estudiante(models.Model):
    ci=models.CharField(max_length=8,primary_key=True,validators=[validar_ci])
    apellidoPaterno=models.CharField(max_length=35)
    apellidoMaterno=models.CharField(max_length=35)
    nombres=models.CharField(max_length=35)
    fechaNacimiento= models.DateField()
    sexos=[
        ('F','Femenino'),
        ('M','Masculino')
    ]
    sexo=models.CharField(max_length=1,choices=sexos,default='F')
    carrera=models.ForeignKey(Carrera,null=False,blank=False,on_delete=models.CASCADE)
    vigencia=models.BooleanField(default=True)

    def nombreCompleto(self):
        txt="{0} {1} {2}"
        return txt.format(self.apellidoPaterno, self.apellidoMaterno, self.nombres)

    def __str__(self):
        txt="{0} / Carrera: {1} / {2}"
        if self.vigencia:
            estadoEstudiane="VIGENTE"
        else: estadoEstudiane="DE BAJA"
        return txt.format(self.nombreCompleto(), self.carrera, estadoEstudiane)
    

class Curso(models.Model):
    codigo=models.CharField(max_length=3,primary_key=True,validators=[validar_codigo])
    nombre=models.CharField(max_length=30)
    creditos=models.PositiveSmallIntegerField(validators=[validar_creditos])
    docente=models.CharField(max_length=100)

    def __str__(self):
        txt="{0} ({1}) / Docente: {2}"
        return txt.format(self.nombre, self.codigo, self.docente)


class Matricula(models.Model):
    id=models.AutoField(primary_key=True)
    estudiante=models.ForeignKey(Estudiante,null=False,blank=False,on_delete=models.CASCADE)
    curso=models.ForeignKey(Curso,null=False,blank=False,on_delete=models.CASCADE)
    fechaMatricula=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        txt="{0} matriculad{1} en el curso {2} / Fecha: {3}"
        if self.estudiante.sexo=='F':
            letraSexo="a"
        else:letraSexo="o"

        fecMat=self.fechaMatricula.strftime("%A %d/%m/%Y %H:%M:%S")
        return txt.format(self.estudiante.nombreCompleto(), letraSexo,self.curso, fecMat)
