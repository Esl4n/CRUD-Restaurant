# Generated by Django 4.1 on 2022-12-12 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='cantidadPersonas',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='telefono',
            field=models.IntegerField(),
        ),
    ]
