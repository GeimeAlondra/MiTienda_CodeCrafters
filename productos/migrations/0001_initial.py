# Generated by Django 4.2.5 on 2023-10-10 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('nombre', models.TextField(max_length=50)),
                ('descripcion', models.TextField(max_length=200)),
                ('fechaProduccion', models.DateField()),
                ('fechaVencimiento', models.DateField()),
                ('existencias', models.IntegerField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=9)),
                ('categoria', models.TextField(max_length=50)),
                ('proveedor', models.TextField(max_length=100)),
            ],
        ),
    ]
