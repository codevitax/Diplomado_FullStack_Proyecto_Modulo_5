# Generated by Django 4.1.6 on 2023-02-17 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camion', '0003_alter_camion_modelo_alter_camion_placa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viaje',
            name='destino',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='viaje',
            name='origen',
            field=models.TextField(),
        ),
    ]
