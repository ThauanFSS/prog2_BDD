from model.models import Colaboradores, Departamentos
from kivy.uix.button import Button
from kivy.uix.label import Label
from controller.utils import Util
from peewee import ModelSelect
import locale

class ColaboradorCtrl:

    def __init__(self):
        self._lista = []

    def salvar_atualizar_departamento(self, nome,endereco,sexo,data_nasci,salario,fk_departamentos_num_dep, id=None):
        try:
            d = Departamentos.get(nome=fk_departamentos_num_dep)
            dn = self._data_nasci_tela_banco(data_nasci)  # "aaaa-mm-dd"
            s = self._salario_tela_banco(salario)
            if id:
                colaborador = Colaboradores.get_by_id(id)
                colaborador.nome = nome
                colaborador.endereco = endereco
                colaborador.sexo = sexo
                colaborador.data_nasci = dn
                colaborador.salario = s
                colaborador.fk_departamentos_num_dep = d
            else:
                colaborador = Colaboradores(nome=nome,endereco = endereco,sexo = sexo,data_nasci = dn,salario = s,fk_departamentos_num_dep = d)
            colaborador.save()
            return "Colaborador salvo com sucesso!!!"
        except Exception as e:
            print(e)
            return "Não foi possível salvar ou atualizar!!!"

    def excluir_departamento(self, id):
        try:
            Colaboradores.delete_by_id(id)
            Colaboradores.delete_instance()
            return "Colaborador excluido com sucesso!!!"
        except Exception as e:
            print(e)
            return "Falha ao excluir departamento!!!"

    def _data_nasci_tela_banco(self, data_nasci):
        if Util.valida_data(data_nasci):
            d = data_nasci.split('/')  # converte a string em lista
            databanco = f"{d[2]}-{d[1]}-{d[0]}"  # monta uma string no fomato "aaaa-mm-dd"
            return databanco

    def _salario_tela_banco(self, salario):
        try:
            sa = salario.replace(".", "")  # remove o ponto da renda
            sa = sa.replace(",", ".")  # troca a virgula por ponto
            return float(sa)
        except Exception as e:
            print(e)

    def buscar_colaborador(self, num_dep=None, nome=None):
        try:
            if id:
                colaborador = Colaboradores.get_by_id(id)
            elif nome:
                colaborador = Colaboradores.select().where(Colaboradores.nome % f'%{nome}%')
            else:
                colaborador = Colaboradores.select()
        except Exception as e:
            print(e)
            return None
        itens = []
        if type(colaborador) is Colaboradores:
            itens.append(
                self._montar_colaborador(colaborador.id, colaborador.nome, colaborador.endereco, colaborador.sexo,
                                         colaborador.data_nasci, colaborador.salario,
                                         colaborador.fk_departamentos_num_dep.nome))
        elif type(colaborador) is ModelSelect:
            for c in colaborador:
                itens.append(self._montar_colaborador(c.id, c.nome, c.endereco, c.sexo, c.data_nasci, c.salario,
                                                      c.fk_departamentos_num_dep.nome))
        return itens

    def _data_nasci_banco_tela(self, data):
        data_tela = ""
        if data:
            data_array = str(data).split("-")  # converte a data para array
            data_tela = f'{data_array[2]}/{data_array[1]}/{data_array[0]}'
        return data_tela

    def _salario_banco_tela(self, salario):
        locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')
        salariotela = str(locale.currency(salario, grouping=True, symbol=None))
        return salariotela

    def _montar_colaborador (self, id, nome,endereco,sexo,data_nasci,salario,fk_departamentos_num_dep):
        nasc = self._data_nasci_banco_tela(data_nasci)  # 01/01/2000
        sal = self._salario_banco_tela(salario)  # 9.999,99
        todoscolaboradores = {
            'lblId': self._criarLabel(id, 0.1),
            'lblNome': self._criarLabel(nome, 0.4),
            'lblEndereco': self._criarLabel(endereco, 0.4),
            'lblSexo': self._criarLabel(sexo, 0.1),
            'lblData_nasci': self._criarLabel(nasc, 0.1),
            'lblSalario': self._criarLabel(sal, 0.1),
            'lblDepartamento': self._criarLabel(fk_departamentos_num_dep, 0.4),
            'btAtualizar': self._criarBotao("Atualizar"),
            'btExcluir': self._criarBotao("Excluir")
        }
        return todoscolaboradores

    def _criarLabel(self, texto, tam):
        label = Label()
        label.text = str(texto)
        label.size_hint_y = None
        label.size_hint_x = tam
        label.height = '30dp'
        return label

    def _criarBotao(self, texto):
        botao = Button(text=texto,
                       font_size='10sp',
                       size_hint_y=None,
                       height='30dp',
                       size_hint_x=.1)
        return botao

    def buscarDepartamentos(self):
        departamentosbanco = Departamentos.select()
        departamentos = []
        for departamento in departamentosbanco:
            departamentos.append({"num_dep": departamento.num_dep, "nome": departamento.nome})
        return