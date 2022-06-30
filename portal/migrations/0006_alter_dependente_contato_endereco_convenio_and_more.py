# Generated by Django 4.0.4 on 2022-06-29 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0005_alter_cuidador_regime_contratacao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dependente',
            name='contato_endereco_convenio',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Endereço Convênio'),
        ),
        migrations.AlterField(
            model_name='dependente',
            name='contato_fone_convenio',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Telefone Convênio'),
        ),
        migrations.AlterField(
            model_name='dependente',
            name='convenio_medico',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Convênio'),
        ),
    ]
