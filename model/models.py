import peewee
from playhouse.mysql_ext import MySQLConnectorDatabase

class BaseModel(peewee.Model):

    class Meta:
        database = MySQLConnectorDatabase('companhia', user='root', password='',
                                           host='localhost', port=3306, charset='utf8mb4')

class Departamentos(BaseModel):
    num_dep = peewee.IntegerField(10, unique=True, primary_key=True)
    nome = peewee.CharField(max_length=100)

    def __init__(self, *args, **kwargs):
        self._criatabela()
        super().__init__(*args, **kwargs)

    def _criatabela(self):
        try:
            self.create_table()
        except peewee.OperationalError as e:
            print("Erro: " + str(e))

class Colaboradores(BaseModel):
    id = peewee.IntegerField(10, unique=True,primary_key=True)
    nome = peewee.CharField(max_length=100)
    endereco = peewee.CharField(100)
    sexo = peewee.CharField(10)
    data_nasci = peewee.DateField()
    salario = peewee.DecimalField()
    fk_departamentos_num_dep = peewee.ForeignKeyField(Departamentos, related_name='departamento')


    def __init__(self, *args, **kwargs):
        self._criatabela()
        super().__init__(*args, **kwargs)

    def _criatabela(self):
        try:
            self.create_table()
        except peewee.OperationalError as e:
            print("Erro: " + str(e))

class Dependentes(BaseModel):
    nome = peewee.CharField(max_length=100)
    sexo = peewee.CharField(10)
    dt_nasc = peewee.DateField()
    grau_parentesco = peewee.CharField()
    id = peewee.IntegerField(10, unique=True ,primary_key=True)
    fk_colaboradores_id = peewee.ForeignKeyField(Colaboradores, related_name='colaboradores')

    def __init__(self, *args, **kwargs):
        self._criatabela()
        super().__init__(*args, **kwargs)

    def _criatabela(self):
        try:
            self.create_table()
        except peewee.OperationalError as e:
            print("Erro: " + str(e))

class Horastrabalho(BaseModel):
    id_hora=peewee.IntegerField(10,unique=True ,primary_key=True)
    horas_trabalhada = peewee.TimeField()

    def __init__(self, *args, **kwargs):
        self._criatabela()
        super().__init__(*args, **kwargs)

    def _criatabela(self):
        try:
            self.create_table()
        except peewee.OperationalError as e:
            print("Erro: " + str(e))

class Projetos(BaseModel):
    num_proj = peewee.IntegerField(10, unique=True,primary_key=True)
    nome = peewee.CharField(max_length=100)
    periodo_des = peewee.DateField()
    fk_horastrabalhada_id = peewee.ForeignKeyField(Horastrabalho, related_name='horastrabalhada')
    fk_departamentos_num_dep = peewee.ForeignKeyField(Departamentos, related_name='Departamentos')


    def __init__(self, *args, **kwargs):
        self._criatabela()
        super().__init__(*args, **kwargs)

    def _criatabela(self):
        try:
            self.create_table()
        except peewee.OperationalError as e:
            print("Erro: " + str(e))



class Supervisor(BaseModel):
    id_sup= peewee.IntegerField(10,unique=True,primary_key=True )
    fk_colaboradores_id = peewee.ForeignKeyField(Colaboradores, related_name='colaboradores')

    def __init__(self, *args, **kwargs):
        self._criatabela()
        super().__init__(*args, **kwargs)

    def _criatabela(self):
        try:
            self.create_table()
        except peewee.OperationalError as e:
            print("Erro: " + str(e))


class Limpeza(BaseModel):
    cargo = peewee.CharField(50)
    jornada_trab = peewee.TimeField()
    fk_supervisor_id = peewee.ForeignKeyField(Supervisor, related_name='supervisor')
    fk_colaboradores_id = peewee.ForeignKeyField(Colaboradores, related_name='colaboradores')

    def __init__(self, *args, **kwargs):
        self._criatabela()
        super().__init__(*args, **kwargs)

    def _criatabela(self):
        try:
            self.create_table()
        except peewee.OperationalError as e:
            print("Erro: " + str(e))


class Pesquisador(BaseModel):
    area_atuacao = peewee.CharField(50)
    fk_colaboradores_id = peewee.ForeignKeyField(Colaboradores, related_name='colaboradores')
    fk_projetos_num_proj = peewee.ForeignKeyField(Projetos, related_name='projetos')

    def __init__(self, *args, **kwargs):
        self._criatabela()
        super().__init__(*args, **kwargs)

    def _criatabela(self):
        try:
            self.create_table()
        except peewee.OperationalError as e:
            print("Erro: " + str(e))

class Secretario(BaseModel):
    grau_escolaridade = peewee.CharField(50)
    fk_colaboradores_id = peewee.ForeignKeyField(Colaboradores, related_name='colaboradores')

    def __init__(self, *args, **kwargs):
        self._criatabela()
        super().__init__(*args, **kwargs)

    def _criatabela(self):
        try:
            self.create_table()
        except peewee.OperationalError as e:
            print("Erro: " + str(e))