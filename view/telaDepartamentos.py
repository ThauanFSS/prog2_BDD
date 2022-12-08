from functools import partial
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.popup import Popup

from controller.departamentoctrl import DepartamentoCtrl


class ViewDepartamentos:

    def __init__(self, gerencia_tela):
        self._gt = gerencia_tela
        self._telacad = self._gt.get_screen("CadastroDepartamento")
        self._telalistar = self._gt.get_screen("ListarDepartamentos")

    def cad_atual_departamento(self):
        result = ""
        try:
            id_departamento = self._telacad.lbl_id_departamento.text
            nome = self._telacad.txi_nome.text
            control = DepartamentoCtrl()
            if self._telacad.bt_cad_atual.text == "Excluir":
                result = control.excluir_departamento(id_departamento)
                self.busca_departamentos()
                self._gt.current = "ListarTurmas"
            else:
                result = control.salvar_atualizar_departamento(nome=nome, id=id_departamento)
            self._popJanela(result)
            self._limparTela()
        except Exception as e:
            print(e)
            self._telacad._popJanela(f"Não foi possível {self._telacad.bt_cad_atual.text} o departamento!!!")

    def montarTelaAt(self, iddepartamento=None, botao=None):
        control = DepartamentoCtrl()
        departamento = None
        if iddepartamento:
            departamento = control.buscar_departamento(iddepartamento)
        if departamento:
            for d in departamento:
                self._telacad.lbl_id_departamento.text = d['lblId'].text
                self._telacad.txi_nome.text = d['lblNome'].text
                self._telacad.bt_cad_atual.text = botao.text

    def _limparTela(self):
        self._telacad.lbl_id_departamento.text = ""
        self._telacad.txi_nome.text = ""
        self._telacad.bt_cad_atual.text = "Cadastrar"

    def _popJanela(self, texto=""):
        popup = Popup(title='Informação', content=Label(text=texto), auto_dismiss=True)
        popup.size_hint = (0.98, 0.4)
        popup.open()

    def _limpar_tela_listar(self):
        cabecalho = [
            self._telalistar.col_id,
            self._telalistar.col_nome,
            self._telalistar.lbl_atualizar,
            self._telalistar.lbl_excluir
        ]
        #self._telalistar.grid_lista.clear_widget()
        #for c in cabecalho:
        #    self._telalistar.grid_lista.add_widget(c)

    def buscar_depatamentos(self):
        try:
            control = DepartamentoCtrl()
            idPesq = self._telalistar.id_departamento.text
            if idPesq:
                resultado = control.buscar_departamento(idPesq)
            else:
                resultado = control.buscar_departamento()
            self._limpar_tela_listar()
            for res in resultado:
                res['btAtualizar'].bind(on_release=partial(self._gt.tela_cadastro_departamento, res['lblId'].text))
                res['btExcluir'].bind(on_release=partial(self._gt.tela_cadastro_departamento, res['lblId'].text))
                self._telalistar.grid_lista.add_widget(res['lblId'])
                self._telalistar.grid_lista.add_widget(res['lblNome'])
                self._telalistar.grid_lista.add_widget(res['btAtualizar'])
                self._telalistar.grid_lista.add_widget(res['btExcluir'])
        except Exception as e:
            print(e)