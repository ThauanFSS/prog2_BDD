from kivy.properties import ObjectProperty, StringProperty, NumericProperty
from kivy.uix.screenmanager import Screen, ScreenManager

from telaColaboradores import ViewColaboradores
from telaDepartamentos import ViewDepartamentos


class TelaInicial(Screen):
    pass


class CadastroDepartamento(Screen):
    lbl_id_departamento = ObjectProperty(None)
    txi_nome = ObjectProperty(None)
    bt_cad_atual: ObjectProperty(None)


class ListarDepartamentos(Screen):
    id_departamento = ObjectProperty(None)
    col_id = ObjectProperty(None)
    col_nome = ObjectProperty(None)
    lbl_atualizar = ObjectProperty(None)
    lbl_excluir = ObjectProperty(None)
    grid_lista = ObjectProperty(None)


class CadastroColaborador(Screen):
    lbl_id: NumericProperty()
    txi_nome: StringProperty()
    txi_endereco: StringProperty()
    txi_sexo: StringProperty()
    txi_nasc: StringProperty()
    txi_salario: NumericProperty()
    sp_departamento: ObjectProperty()
    bt_cad_atual: ObjectProperty(None)

class ListarColaboradores(Screen):
    chk_pesq_id: ObjectProperty()
    chk_pesq_nome: ObjectProperty()
    txi_pesq_id: StringProperty()
    txi_pesq_nome: StringProperty()
    gl_pesquisa_id: ObjectProperty()
    gl_pesquisa_nome: ObjectProperty()
    layout_pesq_id: ObjectProperty()
    layout_pesq_nome: ObjectProperty()
    layout_lista_colaboradores: ObjectProperty()
    pesq = ObjectProperty()


class GerenciaTelas(ScreenManager):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._tela_departamento = ViewDepartamentos(self)
        self._tela_colaborador = ViewColaboradores(self)

    def tela_inicial(self):
        self.current = "TelaInicial"

    def tela_cadastro_departamento(self, id=None, botao=None):
        self.current = 'CadastroDepartamento'
        self._tela_departamento.montarTelaAt(id, botao)

    def tela_listar_departamento(self):
        self.current = "ListarDepartamentos"
        self._tela_departamento._limpar_tela_listar()

    def tela_cadastro_colaborador(self, id="", botao='None'):
        self.current = "CadastroColaborador"
        self._tela_colaborador.montar_tela_at(id, botao)

    def tela_listar_colaboradores(self):
        self._tela_colaborador.alternar_pesq("id")
        self.current = "ListarColaboradoreses"
        self._tela_colaborador._limpar_tela_listar()

    def cadastrar_atualizar(self):
        self._tela_departamento.cad_atual_departamento()

    def cadastrar_atualizar_colaborador(self):
        self._tela_colaborador.cad_atual_colaborador()

    def buscar_departamentos(self):
        self._tela_departamento.buscar_depatamentos()

    def buscar_colaboradores(self):
        self._tela_colaborador.busca_colaborador()

    def buscar_colaboradores_nome(self, nome=""):
        self._tela_colaborador.busca_colaborador(nome)