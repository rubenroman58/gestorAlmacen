# Generated by Django 5.1.6 on 2025-06-29 19:36

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pda', '0025_alter_albarandevolucion_fecha'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cataluña',
            name='articulo',
        ),
        migrations.RemoveField(
            model_name='levante',
            name='articulo',
        ),
        migrations.RemoveField(
            model_name='madrid',
            name='articulo',
        ),
        migrations.AlterField(
            model_name='albarandevolucion',
            name='fecha',
            field=models.DateField(default=datetime.date(2025, 6, 29)),
        ),
        migrations.CreateModel(
            name='Delegacion1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tot_unid', models.IntegerField(blank=True, null=True)),
                ('p_alq_medio', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('articulo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lineas_delegacion1', to='pda.articulo')),
            ],
        ),
        migrations.CreateModel(
            name='Delegacion2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tot_unid', models.IntegerField(blank=True, null=True)),
                ('p_alq_medio', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('articulo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lineas_delegacion2', to='pda.articulo')),
            ],
        ),
        migrations.CreateModel(
            name='Delegacion3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tot_unid', models.IntegerField(blank=True, null=True)),
                ('p_alq_medio', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('articulo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lineas_delegacion3', to='pda.articulo')),
            ],
        ),
        migrations.CreateModel(
            name='Delegacion4',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tot_unid', models.IntegerField(blank=True, null=True)),
                ('p_alq_medio', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('articulo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lineas_delegacion4', to='pda.articulo')),
            ],
        ),
        migrations.DeleteModel(
            name='Andalucia',
        ),
        migrations.DeleteModel(
            name='Cataluña',
        ),
        migrations.DeleteModel(
            name='Levante',
        ),
        migrations.DeleteModel(
            name='Madrid',
        ),
    ]
