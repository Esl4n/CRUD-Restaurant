# Generated by Django 4.1 on 2022-12-10 19:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('telefono', models.IntegerField(max_length=9)),
                ('fecha_hora', models.DateTimeField()),
                ('cantidadPersonas', models.IntegerField(max_length=2)),
                ('estado', models.CharField(max_length=40)),
                ('observacion', models.CharField(max_length=500, null=True)),
            ],
        ),
    ]
