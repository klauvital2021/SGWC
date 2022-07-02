# Generated by Django 4.0.5 on 2022-07-02 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_consulta', models.DateField(verbose_name='Data Consulta')),
                ('hora', models.TimeField(verbose_name='Hora')),
                ('especialidade', models.CharField(choices=[('1', 'Alergista'), ('2', 'Cardiologia'), ('3', 'Clinico Geral'), ('4', 'Dermatologia'), ('5', 'Endocrinologia'), ('6', 'Fisiatria'), ('7', 'Fonoaudiologia'), ('8', 'Gastroenterologia'), ('9', 'Geriatria'), ('10', 'Ginecologia'), ('11', 'Nefrologia'), ('12', 'Neurologia'), ('13', 'Nutrição'), ('14', 'Obstetrícia'), ('15', 'Odontologia'), ('16', 'Oftalmologia'), ('17', 'Oncologia'), ('18', 'Ortopedia'), ('19', 'Otorrinolaringologia'), ('20', 'Pediatria'), ('21', 'Pneumologia'), ('22', 'Proctologia'), ('23', 'Psicologia'), ('24', 'Reumatologia'), ('25', 'Traumatologia'), ('26', 'Urologia'), ('27', 'Outras'), ('28', 'Reumatologia')], max_length=30, verbose_name='Especialidade')),
                ('local', models.CharField(blank=True, max_length=100, null=True, verbose_name='Local')),
                ('nome_especialista', models.CharField(max_length=100, verbose_name='Especialista')),
                ('fone_contato', models.CharField(blank=True, max_length=100, null=True, verbose_name='Fone')),
                ('atendimento', models.CharField(choices=[('1', 'Primeira'), ('2', 'Retorno-Exames'), ('3', 'Retorno')], max_length=30, verbose_name='Atendimento')),
                ('motivo_consulta', models.CharField(blank=True, max_length=300, null=True, verbose_name='Motivo Consulta')),
                ('sintomas', models.CharField(blank=True, max_length=300, null=True, verbose_name='Sintomas')),
                ('observacao', models.CharField(blank=True, max_length=300, null=True, verbose_name='Observação')),
                ('cancelamento', models.DateField(blank=True, null=True, verbose_name='Data Cancelamento')),
                ('motivo_cancelamento', models.CharField(blank=True, choices=[('1', 'Primeira'), ('2', 'Retorno-Exames'), ('3', 'Retorno')], max_length=30, null=True, verbose_name='Motivo Cancelamento')),
                ('acompanhante_responsavel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.responsavel', verbose_name='Acompanhante Responsável')),
                ('dependente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.dependente')),
            ],
            options={
                'ordering': ('data_consulta', 'hora'),
            },
        ),
        migrations.CreateModel(
            name='PosConsulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnostico', models.TextField(verbose_name='Diagnóstico')),
                ('tratamento', models.TextField(blank=True, null=True, verbose_name='Tratamento')),
                ('receita', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Upload Receita')),
                ('observacao', models.TextField(blank=True, null=True, verbose_name='Tratamento')),
                ('acompanhante_responsavel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.responsavel', verbose_name='Responsável')),
                ('consulta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consulta.consulta')),
                ('dependente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.dependente')),
            ],
        ),
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicamento_prescrito', models.CharField(max_length=100, verbose_name='Medicamento Prescrito')),
                ('principio_ativo', models.CharField(blank=True, max_length=40, verbose_name='Princípo Ativo')),
                ('indicacoes', models.TextField(blank=True, null=True, verbose_name='Indicações')),
                ('tipo_medicamento', models.CharField(choices=[('1', 'Comprimido'), ('2', 'Cápsulas'), ('3', 'Creme'), ('4', 'Gotas'), ('5', 'Injeção Musc'), ('6', 'Injeção Subcutânea'), ('7', 'Injeção Venosa'), ('8', 'Pomada'), ('9', 'Solução'), ('10', 'Spray'), ('11', 'Supositório')], max_length=18, verbose_name='Tipo de Medicamento')),
                ('dosagem', models.CharField(max_length=40, verbose_name='Dosagem')),
                ('posologia', models.CharField(choices=[('1 vez ', '1 vez'), ('2 vezes ', '2 vezes'), ('3 vezes ', '3 vezes'), ('4 vezes ', '4 vezes')], max_length=30, verbose_name='Posologia')),
                ('uso_continuo', models.CharField(choices=[('Sim ', 'Sim'), ('Não ', 'Não')], max_length=30, verbose_name='Uso Continuo')),
                ('data_inicio', models.DateField(blank=True, null=True, verbose_name='Dta Inicio')),
                ('data_fim', models.DateField(blank=True, null=True, verbose_name='Dta Fim')),
                ('forma_uso', models.TextField(verbose_name='Forma de Uso')),
                ('orientacao_tratamento', models.TextField(verbose_name='Orientações')),
                ('medico_responsavel', models.CharField(blank=True, max_length=100, null=True, verbose_name='Médico Responsável')),
                ('fornecedor_principal', models.CharField(choices=[('1', 'Farmácia Hospital'), ('2', 'Farmácia Popular'), ('3', 'Farmácia - Drogaria'), ('4', 'Drogaria - Site'), ('5', 'Mercado Livre'), ('6', 'Outros')], max_length=20, verbose_name='Fornecedor')),
                ('dependente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.dependente')),
                ('pos_consulta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consulta.posconsulta')),
            ],
            options={
                'ordering': ('medicamento_prescrito',),
            },
        ),
    ]