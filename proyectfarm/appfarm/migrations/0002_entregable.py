# Generated by Django 4.1.2 on 2022-11-20 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appfarm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entregable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('fecha_de_entrega', models.DateField()),
                ('entregado', models.BooleanField()),
            ],
        ),
    ]
