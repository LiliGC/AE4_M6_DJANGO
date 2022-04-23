# Generated by Django 4.0.3 on 2022-04-18 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('correo_electronico', models.EmailField(max_length=30)),
                ('telefono', models.CharField(max_length=15)),
                ('direccion', models.CharField(max_length=100)),
            ],
        ),
    ]
