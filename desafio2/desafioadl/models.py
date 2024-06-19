from django.db import models

# Create your models here.
class Tarea (models.Model):
    id= models.AutoField(primary_key=True ,null=False)
    descripcion= models.CharField(max_length=100)
    eliminar= models.BooleanField(default=False)

class SubTarea(models.Model):
    id= models.AutoField(primary_key=True ,null=False)
    descripcion= models.CharField(max_length=100)
    eliminar= models.BooleanField(default=False)
    tarea_id= models.IntegerField(models.ForeignKey(Tarea, on_delete=models.CASCADE))