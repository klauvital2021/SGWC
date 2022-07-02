# Generated by Django 4.0.5 on 2022-07-02 22:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
        ('consulta', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='dependente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    related_name='consultas', to='crm.dependente'),
        ),
        migrations.AlterField(
            model_name='posconsulta',
            name='dependente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    related_name='pos_consultas', to='crm.dependente'),
        ),
    ]
