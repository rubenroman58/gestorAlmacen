"""
URL configuration for Patio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import  admin
from django.urls import path
from pda.views import productos_horizontal,productos_vertical,exportar_datos, login_view,eliminar_tarea,eliminar_alabarn,detalles_albaran,lista_albaranes_completa,estadisticas_trabajador,detalles_tarea,lista_tareas_completa,lista_trabajadores,estadisticas
from pda.views import manuales,proyectos_destacados,comparativa_productividad,iniciar_tarea,exportar_trabajadores_excel,editar_linea_articulo,eliminar_linea_articulo,HomeView,salir,finalizar_tarea,seleccionar_albaran,agregar_lineas2,agregar_lineas,crear_paquete
urlpatterns = [
    path('admin/', admin.site.urls),
    path('iniciar-tarea/', iniciar_tarea, name='iniciar_tarea'),
    path('crear-paquete/<int:tarea_id>/', crear_paquete, name='crear_paquete'),
    path('',login_view,name='login'),
    path('paginaInicial/',HomeView.as_view(),name='home'),
    path('cerrar_programa/',salir),
    path('iniciar_tarea/',iniciar_tarea),
    path('finalizar-tarea/<int:tarea_id>/', finalizar_tarea, name='finalizar_tarea'),
    path('seleccionar_albaran/', seleccionar_albaran, name='seleccionar_albaran'),
    path('agregar_lineas/<int:albaran_id>/', agregar_lineas, name='agregar_lineas'),
    path('estadisticas/',estadisticas),
    path('estadisticasTrabajadores/', lista_trabajadores),
    path('lista_tareas/', lista_tareas_completa,name='listaTareas'),
    path('tarea/<int:tarea_id>/',detalles_tarea, name='detalle_tarea'),
    path('estadisticas_trabajador/<int:trabajador_id>/',estadisticas_trabajador,name='estadisticas_trabajador'),
    path('lista_albaranes/',lista_albaranes_completa, name='listaAlbaranes'),
    path('detalle_albaran/<int:albaran_id>/',detalles_albaran, name='detalle_albaran'),
    path('eliminar_albaran/<int:albaran_id>/',eliminar_alabarn,name='eliminarAlbaran'),
    path('eliminar_tarea/<int:tarea_id>/',eliminar_tarea,name='eliminarTarea'),
    path('editar_linea/<int:linea_id>/', editar_linea_articulo, name='editar_linea'),
    path('eliminar_linea/<int:linea_id>/', eliminar_linea_articulo, name='eliminar_linea'),
    path('añadir_linea/<int:albaran_id>/',agregar_lineas2,name='añadir_lineas'),
    path('exportar-trabajadores/',exportar_trabajadores_excel,name='exportar_trabajadores'),
    path('estadisticas/comparativa/',comparativa_productividad, name='comparativa_productividad'),
    path('informes/',exportar_datos,name='informes'),
    path('productos_vertical/',productos_vertical,name='productos_vertical'),
    path('productos_horizontal/',productos_horizontal,name='productos_horizontal'),
    path('proyectos_destacados/',proyectos_destacados,name='proyectos_destacados'),
    path('manuales/',manuales,name='manuales')
]

