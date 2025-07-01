from django.test import TestCase
from .models import TipoTarea, Patio, Paquete, AlbaranDevolucion, LineaArticulo, Trabajador, Articulo
from datetime import date, time
from django.urls import reverse
from datetime import datetime

# Pruebas unitarias para algunos modelos.
class ModeloTests(TestCase):
    def test_crear_tipo_tarea(self):
        tipo = TipoTarea.objects.create(nombre="Montaje")
        self.assertEqual(str(tipo), f"Id: {tipo.id}-Nombre: Montaje")

    def test_trabajador(self):
        tipo = Trabajador.objects.create(nombre='Ruben')
        self.assertEqual(str(tipo), f"Id: {tipo.id}-Nombre: Ruben")

    def test_trabajador(self):
        tipo = Articulo.objects.create(nombre='Articulo')
        self.assertEqual(str(tipo), f"Id: {tipo.id}-Nombre: Articulo")

    def test_crear_albaran(self):
        albaran = AlbaranDevolucion.objects.create(numero=1234, fecha=date(2025, 1, 1))
        self.assertEqual(str(albaran), "El numero del albaran es 1234, fecha:2025-01-01")

    def test_crear_linea_articulo(self):
        albaran = AlbaranDevolucion.objects.create(numero=5678)
        linea = LineaArticulo.objects.create(
            albaran=albaran,
            idArticulo=111,
            cantidad_buena=10,
            cantidad_mala=2,
            chatarra=1
        )
        self.assertIn("Articulo 111 en albaran", str(linea))

    def test_crear_paquete(self):
        patio = Patio.objects.create(idTipTarea=1, idOper1=1)
        paquete = Paquete.objects.create(
            tarea=patio,
            codBarrasPaquete=123456,
            idTipArticulo=10,
            cantidad_paquete=5,
            horaInicio=time(10, 0),
            horaFin=time(12, 0)
        )
        self.assertEqual(str(paquete), f"Paquete de 5 art. (Tarea #{patio.id})")

    def test_crear_patios(self):
        patio = Patio.objects.create(
            fecha=date.today(),
            horaInicio=time(8, 0),
            horaFin=time(14, 0),
            idTipTarea=1,
            idOper1=101,
            idOper2=102,
            cantidad=10
        )
        self.assertEqual(str(patio), f"Tarea 1 - Operador 101 ({patio.fecha})")


        #Pruebas unitarias para las vistas
class VistaTest(TestCase):

    def setUp(self):
        # Crear datos necesarios
        self.trabajador = Trabajador.objects.create(nombre="Ruben")
        self.tipo_tarea = TipoTarea.objects.create(nombre="Montaje")
        self.articulo = Articulo.objects.create(nombre="Tornillo")

    def test_iniciar_tarea(self):
        # Simula el envio del formulario para iniciar la tarea
        response = self.client.post(reverse('iniciar_tarea'), {
            'idTipTarea': self.tipo_tarea.id,
            'idOper1': self.trabajador.id,
            'idOper2': '',
            'cantidad': 0
        })
        
        self.assertEqual(response.status_code, 302)  # Redirección exitosa
        self.assertEqual(Patio.objects.count(), 1)

    def test_crear_paquete_get(self):
        # Crear tarea para poder acceder a la vista
        tarea = Patio.objects.create(
            idTipTarea=self.tipo_tarea.id,
            idOper1=self.trabajador.id,
            cantidad=0,
            fecha=datetime.now().date(),
            horaInicio=datetime.now().time().replace(microsecond=0)
        )

        response = self.client.get(reverse('crear_paquete', kwargs={'tarea_id': tarea.id}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'form')

    def test_crear_paquete_post(self):
        # Crear una tarea existente
        tarea = Patio.objects.create(
            idTipTarea=self.tipo_tarea.id,
            idOper1=self.trabajador.id,
            cantidad=0,
            fecha=datetime.now().date(),
            horaInicio=datetime.now().time().replace(microsecond=0)
        )

        response = self.client.post(reverse('crear_paquete', kwargs={'tarea_id': tarea.id}), {
            'codBarrasPaquete': 123456,
            'idTipArticulo': self.articulo.id,
            'cantidad_paquete': 5
        })

        self.assertEqual(response.status_code, 302)  # Debe redirigir
        self.assertEqual(Paquete.objects.count(), 1)
        paquete = Paquete.objects.first()
        self.assertEqual(paquete.tarea.id, tarea.id)
        self.assertEqual(paquete.cantidad_paquete, 5)


            #----------------PRUEBAS DE INTEGRACIÓN----------------#


    class IntegracionTest(TestCase):
        def setUp(self):
            self.trabajador1 = Trabajador.objects.create(nombre="Juan")
            self.trabajador2 = Trabajador.objects.create(nombre="Ana")
            self.tipo_tarea = TipoTarea.objects.create(nombre="Montaje")
            self.articulo = Articulo.objects.create(nombre="Tornillo")

        def test_flujo_completo_tarea_paquete(self):
             # Paso 1: Crear una tarea (iniciar_tarea)
            response = self.client.post(reverse('iniciar_tarea'), {
                'idTipTarea': self.tipo_tarea.id,
                'idOper1': self.trabajador1.id,
                'idOper2': self.trabajador2.id,
                'cantidad': 0
            })

            self.assertEqual(response.status_code, 302)  # Redirección exitosa
            tarea = Patio.objects.first()
            self.assertIsNotNone(tarea)
            self.assertEqual(tarea.idOper1, self.trabajador1.id)
            self.assertEqual(tarea.idOper2, self.trabajador2.id)

            # Paso 2: Crear paquete para esa tarea
            response = self.client.post(reverse('crear_paquete', kwargs={'tarea_id': tarea.id}), {
                'codBarrasPaquete': 987654,
                'idTipArticulo': self.articulo.id,
                'cantidad_paquete': 15
            })
            self.assertEqual(response.status_code, 302)
            paquete = Paquete.objects.first()
            self.assertIsNotNone(paquete)
            self.assertEqual(paquete.tarea.id, tarea.id)
            self.assertEqual(paquete.cantidad_paquete, 15)

            # Paso 3: Finalizar la tarea
            response = self.client.get(reverse('finalizar_tarea', kwargs={'tarea_id': tarea.id}))
            self.assertEqual(response.status_code, 302)
            tarea.refresh_from_db()
            self.assertIsNotNone(tarea.horaFin)


       
