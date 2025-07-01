from .models  import Articulo, Trabajador,TipoTarea

def get_articulos_dict():
    return {art.id:art.nombre for art in Articulo.objects.all()}

def get_trabajadores_dict():
    return {trab.id: trab.nombre for trab in Trabajador.objects.all()}

def get_tipos_tarea_dict():
    return {tipo.id: tipo.nombre for tipo in TipoTarea.objects.all()}
