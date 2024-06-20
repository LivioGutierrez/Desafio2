#Services: Extraer la logica de negocio
from .models import Tarea, SubTarea

def recupera_tareas_y_sub_tareas():
    #eliminada = False
    lista_tareas= Tarea.objects.filter(eliminada = False)
    
    arreglo_tareas_subtareas = []
    
    #Busqueda inversa
    for tarea in  lista_tareas:
        sub_tareas= tarea.subtarea_set.filter(elimanda= False)
        
        dicc_tareas={
            'tarea': tarea,
            'sub_tarea': sub_tareas
        }
        
        arreglo_tareas_subtareas.append(dicc_tareas)
    
    return arreglo_tareas_subtareas

def crear_nueva_tarea(descripcion= '', eliminada= False):
    tarea= Tarea(descripcion= descripcion, eliminada= eliminada)
    print(tarea.id)
    tarea.save()
    
    return recupera_tareas_y_sub_tareas

def crear_sub_tarea(tarea_id, descripsion= ''):
    tarea= Tarea.objects.get(id= tarea_id)
    
    subtarea= SubTarea(descripsion= descripsion, eliminada= False, tarea_id= tarea)
    subtarea.save()
    
    return recupera_tareas_y_sub_tareas

def elimina_tarea(tarea_id):
    tarea= Tarea.objects.get(id= tarea_id)
    tarea.eliminada= True #eliminado logico
    tarea.save()
    #obj_tarea.delete()  Esto es una eliminacion fisica, se borra el registro de la tabla
    
    return recupera_tareas_y_sub_tareas

def elimina_sub_tarea(SubTareatarea_id):
    tarea= SubTarea.objects.get(id= SubTareatarea_id)
    tarea.eliminada= True
    tarea.save()
    
    return recupera_tareas_y_sub_tareas

def imprimir_en_pantalla():
    pass

#from desafioadl import services
#retorno = services.crear_nueva_tarea('tarea1')
#retorno = services.crear_sub_tarea(1,'subtarea 2')
#retorno = services.recupera_tareas_y_sub_tareas()
#retorno = services.elimina_tarea(1)
#retorno = services.elimina_sub_tarea(2)