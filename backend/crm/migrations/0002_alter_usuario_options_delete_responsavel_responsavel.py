# Generated by Django 4.0.5 on 2022-07-02 22:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consulta', '0002_alter_consulta_dependente_and_more'),
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usuario',
            options={'ordering': ('user__first_name', 'user__last_name')},
        ),
        migrations.DeleteModel(
            name='Responsavel',
        ),
        migrations.CreateModel(
            name='Responsavel',
            fields=[
            ],
            options={
                'verbose_name': 'Responsável',
                'verbose_name_plural': 'Responsáveis',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('crm.usuario',),
        ),
    ]
