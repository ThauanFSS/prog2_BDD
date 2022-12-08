from model.models import Departamentos
from kivy.uix.button import Button
from kivy.uix.label import Label
from controller.utils import Util
from peewee import ModelSelect

class DepartamentoCtrl:

    def __init__(self):
        self._lista = []

    def salvar_atualizar_departamento(self, nome, num_dep=None):
        try:
            if id:
                departamento = Departamentos.get_by_id(num_dep)
                departamento.nome = nome
            else:
                departamento = Departamentos(nome=nome)
            departamento.save()
            return "Departamento salvo com sucesso!!!"
        except Exception as e:
            print(e)
            return "Não foi possível salvar ou atualizar!!!"

    def excluir_departamento(self, num_dep):
        try:
            Departamentos.delete_by_id(num_dep)
            Departamentos.delete_instance()
            return "Departamento excluido com sucesso!!!"
        except Exception as e:
            print(e)
            return "Falha ao excluir departamento!!!"

    def buscar_departamento(self, num_dep=None, nome=None):
        try:
            if num_dep:
                departamento = Departamentos.get_by_id(num_dep)
            elif nome:
                departamento = Departamentos.select().where(Departamentos.nome % f'%{nome}%')
            else:
                departamento = Departamentos.select()
        except Exception as e:
            print(e)
            return None
        itens = []
        if type(departamento) is Departamentos:
            itens.append(self._montar_departamento(departamento.num_dep, departamento.nome))
        elif type(departamento) is ModelSelect:
            for d in departamento:
                itens.append(self._montar_departamento(d.num_dep, d.nome))
        return itens

    def _montar_departamento(self, num_dep, nome):
        todosdepartamentos = {
            'lblId': self._criarLabel(num_dep, 0.2),
            'lblNome': self._criarLabel(nome, 0.4),
            'btAtualizar': self._criarBotao("Atualizar"),
            'btExcluir': self._criarBotao("Excluir")
        }
        return todosdepartamentos

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