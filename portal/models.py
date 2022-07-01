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

    def get_absolute_url(self):
        return reverse("cuidador_edit", kwargs={"cuidador_pk": self.id})

class Dependente(Usuario):
    convenio_medico = models.CharField(max_length=100, blank=True, null=True, verbose_name='Convênio')
    contato_fone_convenio = models.CharField(max_length=20, blank=True, null=True, verbose_name='Telefone Convênio')
    contato_endereco_convenio = models.CharField(max_length=100, blank=True, null=True, verbose_name='Endereço Convênio')
    familia = models.ForeignKey(Familia, on_delete=models.CASCADE, blank=True, default='1',)

    class Meta:
       ordering = ['nome']

    def __str__(self):
        return "{} - {} ".format(self.nome, self.familia.nome)


tipo_medicamento_choices = (
   ('Comprimido', 'Comprimido'),
   ('Cápsulas', 'Cápsulas'),
   ('Creme', 'Creme'),
   ('Gotas', 'Gotas'),
   ('Injeção Musc', 'Injeção Musc'),
   ('Injeção Subcutânea', 'Injeção Subcutânea'),
   ('Injeção Venosa', 'Injeção Venosa'),
   ('Pomada', 'Pomada'),
   ('Solução', 'Solução'),
   ('Spray', 'Spray'),
   ('Supositório', 'Supositório'),

)

especialidade_choices = (
    ('Alergista', 'Alergista'),
    ('Cardiologia', 'Cardiologia'),
    ('Clinico Geral', 'Clinico Geral'),
    ('Dermatologia', 'Dermatologia'),
    ('Endocrinologia', 'Endocrinologia'),
    ('Fisiatria', 'Fisiatria'),
    ('Fonoaudiologia', 'Fonoaudiologia'),
    ('Gastroenterologia', 'Gastroenterologia'),
    ('Geriatria', 'Geriatria'),
    ('Ginecologia', 'Ginecologia'),
    ('Nefrologia', 'Nefrologia'),
    ('Neurologia', 'Neurologia'),
    ('Nutrição', 'Nutrição'),
    ('Obstetrícia', 'Obstetrícia'),
    ('Odontologia', 'Odontologia'),
    ('Oftalmologia', 'Oftalmologia'),
    ('Oncologia', 'Oncologia'),
    ('Ortopedia', 'Ortopedia'),
    ('Otorrinolaringologia', 'Otorrinolaringologia'),
    ('Pediatria', 'Pediatria'),
    ('Pneumologia', 'Pneumologia'),
    ('Proctologia', 'Proctologia'),
    ('Psicologia', 'Psicologia'),
    ('Reumatologia', 'Reumatologia'),
    ('Traumatologia', 'Traumatologia'),
    ('Urologia', 'Urologia'),
    ('Outras', 'Outras'),
    ('Reumatologia', 'Reumatologia'),

)
atendimento_choices = (
    ('Primeira', 'Primeira'),
    ('Retorno-Exames', 'Retorno-Exames'),
    ('Retorno', 'Retorno'),
    )


class Consultas(models.Model):
    dependente = models.ForeignKey(Dependente, on_delete=models.CASCADE, blank=False, null=False,)
    data_consulta = models.DateField(db_column='data_consulta', blank=False, null=False, verbose_name='Data Consulta')
    hora = models.TimeField(db_column='hora_consulta', blank=False, null=False, verbose_name='Hora')
    especialidade = models.CharField(max_length=30, choices=especialidade_choices, blank=False, null=False, verbose_name='Especialista')
    local = models.CharField(max_length=100, blank=True, null=True, verbose_name='Local')
    nome_especialista = models.CharField(max_length=100, blank=False, null=False, verbose_name='Médico(a)')
    fone_contato = models.CharField(max_length=100, blank=True, null=True, verbose_name='Fone')
    atendimento = models.CharField(max_length=30, choices=atendimento_choices, verbose_name='Atendimento')
    motivo_consulta = models.CharField(max_length=300, blank=True, null=True, verbose_name='Motivo Consulta')
    sintomas = models.CharField(max_length=300, blank=True, null=True, verbose_name='Sintomas')
    observacao = models.CharField(max_length=300, blank=True, null=True, verbose_name='Observação')
    acompanhante_resp = models.ForeignKey(Responsavel, on_delete=models.CASCADE, blank=False, null=False)
    cancelamento = models.DateField(db_column='dataCancelamento', blank=True, null=True, verbose_name='Data Cancelamento')
    motivo_canc = models.CharField(max_length=30, choices=atendimento_choices, blank=True, null=True, verbose_name='Motivo Cancelamento')

    class Meta:
       ordering = ['data_consulta', 'hora']

    def __str__(self):
        return "{} - {} - {} - {}".format(self.especialidade, self.dependente.nome, self.nome_especialista, self.acompanhante_resp.nome)


class Pos_Consultas(models.Model):
    dependente = models.ForeignKey(Dependente, on_delete=models.CASCADE, blank=False, null=False,verbose_name='Dependente')
    consulta = models.ForeignKey(Consultas, on_delete=models.CASCADE, blank=True, null=True)
    acompanhante_resp = models.ForeignKey(Responsavel, on_delete=models.CASCADE, blank=False, null=False, verbose_name='Responsável')
    diagnostico = models.TextField(max_length=200, blank=False, null=False, verbose_name='Diagnóstico')
    tratamento = models.TextField(max_length=200, blank=True, null=True, verbose_name='Tratamento')
    receita = models.ImageField(upload_to= '', blank=True, null=True, width_field = 'width', height_field = 'height', verbose_name='Upload Receita')
    observacao = models.TextField(max_length=200, blank=True, null=True, verbose_name='Tratamento')

    def __str__(self):
        return "{} - {} - {} ".format(self.consulta.id, self.dependente)

    def get_upload_to(instance, filename):
        """
        Obtain a valid upload path for an image file.

        This needs to be a module-level function so that it can be referenced within migrations,
        but simply delegates to the `get_upload_to` method of the instance, so that AbstractImage
        subclasses can override it.
        """
        return instance.get_upload_to(filename)

posologia_choices = (
        ('1 vez ', '1 vez'),
        ('2 vezes ', '2 vezes'),
        ('3 vezes ', '3 vezes'),
        ('4 vezes ', '4 vezes'),
    )
uso_continuo_choices = (
        ('Sim ', 'Sim'),
        ('Não ', 'Não'),
    )
fornecedor_principal_choices = (
        ('Farmácia Hospital ', 'Farmácia Hospital'),
        ('Farmácia Popular ', 'Farmácia Popular'),
        ('Farmácia - Drogaria ', 'Farmácia - Drogaria'),
        ('Drogaria - Site ', 'Drogaria - Site'),
        ('Mercado Livre ', 'Mercado Livre'),
        ('Outros ', 'Outros'),
    )

class Medicamentos(models.Model):
    medicamento_prescrito = models.CharField(max_length=100, blank=False, null=False,verbose_name='Medicamento Prescrito')
    principio_ativo = models.CharField(max_length=40, blank=True, null=False, verbose_name='Princípo Ativo')
    indicacoes = models.TextField(max_length=100, blank=True, null=True, verbose_name='Indicações')
    tipo_medicamento = models.CharField(max_length=18, choices=tipo_medicamento_choices, verbose_name='Tipo de Medicamento')
    dosagem = models.CharField(max_length=40, blank=False, null=False, verbose_name='Princípo Ativo')
    posologia = models.CharField(max_length=30, choices=posologia_choices, verbose_name='Tipo de Medicamento')
    uso_continuo = models.CharField(max_length=30, choices=uso_continuo_choices, verbose_name='Uso Continuo')
    data_inicio = models.DateField(db_column='dtaInicio', blank=True, null=True, verbose_name='Dta Inicio')
    data_fim = models.DateField(db_column='dtaFim', blank=True, null=True, verbose_name='Dta Fim')
    forma_uso = models.TextField(max_length=100, blank=False, null=False, verbose_name='Forma de Uso')
    orientacao_tratamento = models.TextField(max_length=100, blank=False, null=False, verbose_name='Orientações')
    medico_resp = models.CharField(max_length=100, blank=True, null=True, verbose_name='Medico Resp')
    fornecedor_principal = models.CharField(max_length=20, choices=fornecedor_principal_choices, verbose_name='Fornecedor')
    dependente = models.ForeignKey(Dependente, on_delete=models.CASCADE, blank=False)
    pos_consulta = models.ForeignKey(Pos_Consultas, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
            ordering = ['medicamento_prescrito']

    def __str__(self):
            return "{} - {} -{} - {} - {} - {} ".format(self.medicamento_prescrito, self.dependente, self.fornecedor_principal, self.indicacoes, self.dosagem, self.medico_resp)

    def get_absolute_url(self):
        return reverse("medicamento_edit", kwargs={"medicamento_pk": self.id})