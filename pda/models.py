from django.db import models
from django.utils import timezone


class TipoTarea(models.Model):
    cod_tarea=models.TextField(null=True,blank=True)
    nombre=models.TextField(null=True,blank=True)
    def __str__(self):
       return f"Id: {self.id}-Nombre: {self.nombre}"


class Patio(models.Model):
    fecha = models.DateField(verbose_name='Fecha', null=True, blank=True)
    horaInicio = models.TimeField(verbose_name='H.Inicio', null=True, blank=True)
    horaFin = models.TimeField(verbose_name='H.Fin', null=True, blank=True)
    idTipTarea = models.IntegerField(verbose_name='Tip.Tarea', null=True, blank=True)
    idOper1 = models.IntegerField(verbose_name='Op.1', null=True, blank=True)
    idOper2 = models.IntegerField(verbose_name='Op.2', null=True, blank=True)
    cantidad = models.IntegerField(verbose_name='Cantidad', null=True, blank=True)

    def __str__(self):
        return f"Tarea {self.idTipTarea} - Operador {self.idOper1} ({self.fecha})"


class Paquete (models.Model):
    tarea = models.ForeignKey(Patio, on_delete=models.CASCADE, related_name="paquetes")
    codBarrasPaquete=models.IntegerField(verbose_name='Cod.Barras', null=True, blank=True)
    idTipArticulo=models.IntegerField(verbose_name='Tip.Articulo', null=True, blank=True)
    cantidad_paquete=models.IntegerField(verbose_name='Cantidad paquete', null=True, blank=True)
    horaInicio=models.TimeField(verbose_name='Hora Inicio', null=True, blank=True)
    horaFin= models.TimeField(verbose_name='Hora Fin', null=True, blank=True)
    
    def __str__(self):
        return f"Paquete de {self.cantidad_paquete} art. (Tarea #{self.tarea.id})"
    

class AlbaranDevolucion(models.Model):
    numero=models.IntegerField(verbose_name='Num.Albaran', unique=True)
    fecha=models.DateField(default=timezone.localdate())
  
    def __str__(self):
        return f"El numero del albaran es {self.numero}, fecha:{self.fecha}"
    

class LineaArticulo(models.Model):
    albaran = models.ForeignKey(AlbaranDevolucion, on_delete=models.CASCADE, related_name='lineas')
    idArticulo=models.IntegerField(null=True, blank=True)
    cantidad_buena=models.IntegerField(null=True, blank=True)
    cantidad_mala=models.IntegerField(null=True, blank=True)
    chatarra=models.IntegerField(null=True, blank=True)
    def __str__(self):
       return f"Articulo {self.idArticulo} en albaran: {self.albaran}"
    

class Trabajador(models.Model):
    nombre=models.TextField(null=True,blank=True)
    apellidos=models.TextField(null=True,blank=True)
    def __str__(self):
       return f"Id: {self.id}-Nombre: {self.nombre}-Apellidos:{self.apellidos}"
   
    
class Articulo(models.Model):
    nombre=models.TextField(null=True,blank=True)
    def __str__(self):
       return f"Id: {self.id}-Nombre: {self.nombre}"
   
class Delegacion1(models.Model):
    articulo=models.ForeignKey(Articulo,on_delete=models.CASCADE,null=True,related_name='lineas_delegacion1')
    tot_unid=models.IntegerField(null=True,blank=True)                        
    p_alq_medio=models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    
    def __str__(self):
        return f"Tot.unid: {self.tot_unid}-P.Alq.Medio: {self.p_alq_medio}"
    
class Delegacion2(models.Model):
    articulo=models.ForeignKey(Articulo,on_delete=models.CASCADE,null=True,related_name='lineas_delegacion2')
    tot_unid=models.IntegerField(null=True,blank=True)                        
    p_alq_medio=models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    
    def __str__(self):
        return f"Tot.unid: {self.tot_unid}-P.Alq.Medio: {self.p_alq_medio}"
        
class Delegacion3(models.Model):
    articulo=models.ForeignKey(Articulo,on_delete=models.CASCADE,null=True,related_name='lineas_delegacion3')
    tot_unid=models.IntegerField(null=True,blank=True)                        
    p_alq_medio=models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    
    def __str__(self):
        return f"Tot.unid: {self.tot_unid}-P.Alq.Medio: {self.p_alq_medio}"
    

class Delegacion4(models.Model):
    articulo=models.ForeignKey(Articulo,on_delete=models.CASCADE,null=True,related_name='lineas_delegacion4')
    tot_unid=models.IntegerField(null=True,blank=True)
    p_alq_medio=models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    
    def __str__(self):
        return f"Tot.unid: {self.tot_unid}-P.Alq.Medio: {self.p_alq_medio}"
    
    
class Costes(models.Model):
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE, null=True, related_name='costes')
    precio = models.DecimalField(max_digits=10, decimal_places=3)

    def __str__(self):
        return f"Precio: {self.precio} - Artículo: {self.articulo.nombre}"
