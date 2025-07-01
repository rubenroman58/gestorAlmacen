from django import forms
from .models import Patio, Trabajador, Paquete, AlbaranDevolucion, LineaArticulo, Articulo, TipoTarea

# Formulario para agregar/modificar trabajador
class TrabajadorForm(forms.ModelForm):
    nombre = forms.CharField(label='Trabajador')

    class Meta:
        model = Trabajador
        fields = ['nombre']

# Formulario para el modelo Patio
class PatioForm(forms.ModelForm):
    idOper1 = forms.IntegerField(required=True, min_value=0, label='Trab.1')
    idTipTarea = forms.IntegerField(required=True, min_value=0, label='Tip.Tarea')
    idOper2 = forms.IntegerField(required=False, min_value=0, label='Trab.2')

    class Meta:
        model = Patio
        fields = ['idTipTarea', 'idOper1', 'idOper2']

    # Validaciones personalizadas(se ejecuta después de la validación básica)
    def clean(self):
        cleaned_data = super().clean()
        oper1 = cleaned_data.get('idOper1')
        oper2 = cleaned_data.get('idOper2')
        tip_tarea = cleaned_data.get('idTipTarea')

        # Verifica que los trabajadores no sean el mismo
        if oper1 and oper2 and oper1 == oper2:
            raise forms.ValidationError("El trabajador y el trabajador 2 no pueden ser el mismo")

        # Verifica que los ID de trabajadores y tipo de tarea sean válidos
        if not Trabajador.objects.filter(id=oper1).exists():
            raise forms.ValidationError('El ID del trabajador 1 no es válido')
        
        if oper2 and not Trabajador.objects.filter(id=oper2).exists():
            raise forms.ValidationError('El ID del trabajador 2 no es válido')
        
        if not TipoTarea.objects.filter(id=tip_tarea).exists():
            raise forms.ValidationError('El ID del tipo de tarea no es válido')
        
        return cleaned_data

# Formulario para el modelo Paquete
class PaqueteForm(forms.ModelForm):
    codBarrasPaquete = forms.IntegerField(required=True, min_value=0, label='Cod.Barras.Paquete')
    idTipArticulo = forms.IntegerField(required=True, min_value=0, label='Tip.Articulo')
    cantidad_paquete = forms.IntegerField(min_value=0, label='Cantidad.Paquete')

    class Meta:
        model = Paquete
        fields = ['codBarrasPaquete', 'idTipArticulo', 'cantidad_paquete']

    # Validación del ID del artículo
    def clean(self):
        cleaned_data = super().clean()
        idTipArticulo = cleaned_data.get('idTipArticulo')
        if not Articulo.objects.filter(id=idTipArticulo).exists():
            raise forms.ValidationError('El ID del artículo no es válido')
        return cleaned_data

# Formulario para el modelo Albarán
class AlbaranForm(forms.ModelForm):
    numero = forms.IntegerField(required=True, min_value=0, label='Num.Albaran')

    class Meta:
        model = AlbaranDevolucion
        fields = ['numero']

# Formulario para el modelo LineaArticulo
class LineaArticuloForm(forms.ModelForm):
    idArticulo = forms.IntegerField(required=True, label='Id.Articulo')
    cantidad_buena = forms.IntegerField(min_value=0)
    cantidad_mala = forms.IntegerField(min_value=0)
    chatarra = forms.IntegerField(min_value=0)

    # Validación del ID del artículo
    def clean(self):
        cleaned_data = super().clean()
        idArticulo = cleaned_data.get('idArticulo')
        if not Articulo.objects.filter(id=idArticulo).exists():
            raise forms.ValidationError('El ID del artículo es inválido')
        return cleaned_data

    class Meta:
        model = LineaArticulo
        fields = ['idArticulo', 'cantidad_buena', 'cantidad_mala', 'chatarra']
