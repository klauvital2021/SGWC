# Generated by Django 4.0.5 on 2022-07-04 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consulta', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posconsulta',
            name='dependente',
        ),
    ]
