from django.db import models
from django.urls import reverse

# ---------- Modelo Multi Tabelas ----------

status_choices = (
        ('1', 'Ativo'),
        ('2', 'Inativo')
    )

civil_choices = (
    ('1', 'Solteiro(a)'),
    ('2', 'Casado(a)'),
    ('3', 'Divorciado(a)'),
    ('4', 'Viuvo(a)'),
    ('5', 'União Estável'),
    ('6', 'Outros')
    )

regime_choices = (
    ('1', 'CLT'),
    ('2', 'PJ'),
    ('3', 'Free Lance'),
    ('4', 'Prestação Serviços')
    )

turno_choices = (
    ('1', 'Diurno'),
    ('2', 'Noturno')
    )

parentesco_choices = (
    ('1', 'Filho'),
    ('2', 'Neto'),
    ('3', 'Irmão'),
    ('4', 'Outro')

)


tipo_usuario_choices = (
    ('1', 'Administrador'),
    ('2', 'Responsável'),
    ('3', 'Cuidador'),
    ('4', 'Dependente'),
    ('5', 'Técnico em Enfermagem')

    )

class Usuario(models.Model):
    nome = models.CharField(max_length=200, unique=True, blank=False, null=False, verbose_name='Nome')
    dtanasc = models.DateField(db_column='dtanasc', blank=True, null=True, verbose_name='Data de nascimento')
    rg = models.CharField(max_length=20, blank=True, null=True, verbose_name='RG')
    cpf = models.CharField(max_length=14, unique=True, blank=True, null=True, verbose_name='CPF')
    endereco = models.CharField(max_length=100, blank=False, null=False, verbose_name='Endereço')
    bairro = models.CharField(max_length=30, blank=False, null=False, verbose_name='Bairro')
    cidade = models.CharField(max_length=30, blank=False, null=False, verbose_name='Cidade')
    uf = models.CharField(db_column='UF', max_length=2, blank=True, null=True, verbose_name='Estado')
    celular_whatsapp = models.CharField(max_length=25, unique=True, blank=False, null=False, verbose_name='Celular - WhatsApp')
    celular_recado = models.CharField(max_length=25, blank=True, null=True, verbose_name='Contato Recado')
    estado_civil = models.CharField(max_length=1, choices=civil_choices, verbose_name='Estado Civil')
    nome_conjuge = models.CharField(max_length=100, blank=False, null=False, verbose_name='Cônjuge')
    naturalidade = models.CharField(max_length=20, blank=True, null=True, verbose_name='Naturalidade')
    nacionalidade = models.CharField(max_length=20, blank=False, null=False, verbose_name='Nacionalidade')
    status = models.CharField(max_length=1, choices=status_choices, verbose_name='Estatus')
    tipo_usuario = models.CharField(max_length=1, choices=tipo_usuario_choices, verbose_name='Usuário')


    def __str__(self):
        return self.nome

class Familia(models.Model):
    nome = models.CharField(max_length=200, unique=True, blank=False, null=False, verbose_name='Nome')
    endereco = models.CharField(max_length=100, blank=False, null=False, verbose_name='Endereço')
    bairro = models.CharField(max_length=30, blank=False, null=False, verbose_name='Bairro')
    cidade = models.CharField(max_length=30, blank=False, null=False, verbose_name='Cidade')
    uf = models.CharField(db_column='UF', max_length=2, blank=True, null=True, verbose_name='Estado')
    email = models.EmailField(max_length=30, unique=True, blank=True, null=True, verbose_name='E-mail')
    senha = models.CharField(max_length=20, blank=False, null=False)
    status = models.CharField(max_length=1, choices=status_choices, verbose_name='Estatus')

    def __str__(self):
        return self.nome

class Responsavel(Usuario):
    familia = models.ForeignKey(Familia, on_delete=models.CASCADE, blank=True)
    parentesco_choices = models.CharField(max_length=1, choices=parentesco_choices, verbose_name='Tipo de Responsável')

    def __str__(self):
        return self.nome


class Cuidador(Usuario):
    data_inicio = models.DateField(db_column='dtaIni', blank=True, null=True, verbose_name='Data de Início')
    data_fim = models.DateField(db_column='dtaFim', blank=True, null=True, verbose_name='Data da Saída')
    regime_contratacao = models.CharField(max_length=1, choices=regime_choices, verbose_name='Regime de Contratação')
    carga_horaria_semanal = models.IntegerField(db_column='carga_horaria_semanal', blank=True, null=True, verbose_name='Carga Hóraria Semanal')
    turno_trabalho = models.CharField(max_length=1, blank=False, null=False, choices=turno_choices, verbose_name='Turno')
    quem_indicou = models.CharField(max_length=100, blank=False, null=False, verbose_name='Indicação')
    salario_atual = models.DecimalField(db_column='salario_atual', max_digits=10, decimal_places=2, blank=False, null=False, default=0, verbose_name='Salário atual')
    adicional = models.DecimalField(db_column='adicional', max_digits=10, decimal_places=2, blank=False, null=False, default=0, verbose_name='Adicional noturno')
    dia_pagamento = models.DateField(db_column='dia_pagamento', blank=True, null=True, verbose_name='Dia de pagamento')
    observacao = models.TextField(max_length=1000, blank=False, null=False, verbose_name='Senha')
    familia = models.ForeignKey(Familia, on_delete=models.CASCADE, blank=True)


    def __str__(self):
        return self.nome

class Dependente(Usuario):
    convenio_medico = models.CharField(max_length=100, blank=False, null=False, verbose_name='Convênio')
    contato_fone_convenio = models.CharField(max_length=20, blank=False, null=False, verbose_name='Telefone Convênio')
    contato_endereco_convenio = models.CharField(max_length=100, blank=False, null=False, verbose_name='Endereço Convênio')
    familia = models.ForeignKey(Familia, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.nome



