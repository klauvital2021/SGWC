from django.db import models
from django.contrib.sessions.models import Session
#from django.contrib.auth.models import AbstractUser
from django.urls import reverse

# ---------- Modelo Multi Tabelas ----------

status_choices = (
        ('A', 'Ativo'),
        ('I', 'Inativo'),
    )

civil_choices = (
    ('1', 'Solteiro(a)'),
    ('2', 'Casado(a)'),
    ('3', 'Divorciado(a)'),
    ('4', 'Viuvo(a)'),
    ('5', 'União Estável'),
    ('6', 'Outros'),
    )

regime_choices = (
    ('CLT', 'CLT'),
    ('PJ', 'PJ'),
    ('FREE', 'Free Lance'),
    ('PS', 'Prestação Serviços'),
    )

turno_choices = (
    ('D', 'Diurno'),
    ('N', 'Noturno'),
    )

parentesco_choices = (
    ('F', 'Filho'),
    ('N', 'Neto'),
    ('I', 'Irmão'),
    ('O', 'Outro'),

)

class Usuario(models.Model):
    nome = models.CharField(max_length=200, unique=True, blank=False, null=False, verbose_name='Nome')
    dtanasc = models.DateField(db_column='dtanasc', blank=False, null=False, verbose_name='Dta Nasc')
    rg = models.CharField(max_length=200, blank=True, null=True, verbose_name='RG')
    cpf = models.CharField(max_length=200, blank=True, null=True, verbose_name='CPF')
    endereco = models.CharField(max_length=200, blank=True, null=True, verbose_name='Endereço')
    bairro = models.CharField(max_length=200, blank=True, null=True, verbose_name='Bairro')
    cidade = models.CharField(max_length=200, blank=True, null=True, verbose_name='Cidade')
    uf = models.CharField(db_column='UF', max_length=2, blank=True, null=True, verbose_name='Estado')
    celular_whatsapp = models.CharField(max_length=200, unique=True, blank=True, null=True, verbose_name='Celular-What')
    celular_recado = models.CharField(max_length=200, blank=True, null=True, verbose_name='Recado')
    estado_civil = models.CharField(max_length=10, choices=civil_choices,blank=True, null=True, verbose_name='Estado Civil')
    nome_conjuge = models.CharField(max_length=200, blank=True, null=True, verbose_name='Cônjuge')
    nacionalidade = models.CharField(max_length=200, blank=True, null=True, verbose_name='Nacionalidade')
    status = models.CharField(max_length=1, choices=status_choices, blank=True, null=True, verbose_name='Estatus')

    class Meta:
        ordering = ['nome']


class Familia(models.Model):
    nome = models.CharField(max_length=200, unique=True, blank=False, null=False, verbose_name='Nome')
    endereco = models.CharField(max_length=100, blank=False, null=False, verbose_name='Endereço')
    bairro = models.CharField(max_length=30, blank=False, null=False, verbose_name='Bairro')
    cidade = models.CharField(max_length=30, blank=False, null=False, verbose_name='Cidade')
    uf = models.CharField(db_column='UF', max_length=2, blank=True, null=True, verbose_name='Estado')
    email = models.EmailField(max_length=30, unique=True, blank=True, null=True, verbose_name='E-mail')
    senha = models.CharField(max_length=20, blank=False, null=False)
    status = models.CharField(max_length=1, choices=status_choices, verbose_name='Estatus')


    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("familia_edit", kwargs={"familia_pk": self.id})


class Responsavel(Usuario):
    familia = models.ForeignKey(Familia, on_delete=models.CASCADE, blank=True, null=False, default='1', verbose_name='Família')
    parentesco = models.CharField(max_length=1, choices=parentesco_choices, verbose_name='Tipo de Responsável')
    email = models.EmailField(max_length=100, unique=True, blank=True, null=True, verbose_name='Email')
    senha = models.CharField(max_length=20, blank=False, null=False)


    class Meta:
       ordering = ['nome']

    def __str__(self):
        return "{} - {} - {} - {} - {}".format(self.nome, self.familia.id, self.familia.nome, self.email, self.parentesco)

    def __int__(self):
        return self.familia_id

    def get_absolute_url(self):
        return reverse("responsavel_edit", kwargs={"responsavel_pk": self.id})


class Cuidador(Usuario):
    familia = models.ForeignKey(Familia, on_delete=models.CASCADE, blank=True, default='1')
    data_inicio = models.DateField(db_column='dtaIni', blank=True, null=True, verbose_name='Admissão')
    data_fim = models.DateField(db_column='dtaFim', blank=True, null=True, verbose_name='Demissão')
    regime_contratacao = models.CharField(max_length=10, choices=regime_choices, null=True, verbose_name='Contratação')
    carga_horaria_semanal = models.IntegerField(db_column='carga_horaria_semanal', blank=False, default=44, null=False, verbose_name='Carga Hor Sem')
    turno_trabalho = models.CharField(max_length=1, blank=False, null=False, choices=turno_choices, verbose_name='Turno')
    quem_indicou = models.CharField(max_length=100, blank=False, null=False, verbose_name='Indicação')
    salario_atual = models.DecimalField(db_column='salario_atual', max_digits=10, decimal_places=2, blank=False, null=False, default=0, verbose_name='Salário')
    adicional = models.DecimalField(db_column='adicional', max_digits=10, decimal_places=2, blank=True, null=True, default=0, verbose_name='Adicional')
    dia_pagamento = models.IntegerField(db_column='dia_pagamento', blank=True, null=True, verbose_name='Dia pag')
    observacao = models.TextField(max_length=1000, blank=False, null=False, verbose_name='Observação')
    email = models.EmailField(max_length=30, unique=True, blank=True, null=True, verbose_name='E-mail')
    senha = models.CharField(max_length=20, blank=True, null=True, verbose_name='Senha')

    class Meta:
       ordering = ['nome']

    def __str__(self):
        return "{} - {} - {} - {} ".format(self.nome, self.familia.nome, self.dia_pagamento, self.salario_atual)


class Dependente(Usuario):
    convenio_medico = models.CharField(max_length=100, blank=True, null=True, verbose_name='Convênio')
    contato_fone_convenio = models.CharField(max_length=20, blank=True, null=True, verbose_name='Telefone Convênio')
    contato_endereco_convenio = models.CharField(max_length=100, blank=True, null=True, verbose_name='Endereço Convênio')
    familia = models.ForeignKey(Familia, on_delete=models.CASCADE, blank=True, default='1',)

    class Meta:
       ordering = ['nome']

    def __str__(self):
        return "{} - {} ".format(self.nome, self.familia.nome)



