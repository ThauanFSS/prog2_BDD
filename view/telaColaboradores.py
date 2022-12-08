from functools import partial
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from controller.colaboradoresctrl import ColaboradorCtrl

class ViewColaboradores:

    def __init__(self, gerencia_tela):
        self._gt = gerencia_tela
        self._telacad = self._gt.get_screen("CadastroColaborador")
        self._telalistar = self._gt.get_screen("ListarColaboradores")

    def cad_atual_colaborador(self):
        control = ColaboradorCtrl()
        try:
            id_colaborador = self._telacad.lbl_id.text
            nome = self._telacad.txi_nome.text
            endereco = self._telacad.txi_endereco.text
            sexo = self._telacad.txi_sexo.text
            data_nasci = self._telacad.txi_nasc.text
            salario = self._telacad.txi_renda.text
            fk_departamentos_id = self._telacad.sp_departamento.text
            if self._telacad.bt_cad_atual.text == "Excluir":
                result = control.excluir_departamento(id_colaborador)
                self.busca_colaborador()
                self._gt.current = "ListarColaboradores"
            else:
                result = control.salvar_atualizar_departamento(id=id_colaborador,
                                                        nome=nome,
                                                        endereco=endereco,
                                                        sexo=sexo,
                                                        data_nasci=data_nasci,
                                                        salario=salario,
                                                        fk_departamentos_id=fk_departamentos_id)
            self._popJanela(result)
            self._limpar_tela()
            self._telacad.txi_nome.focus = True
        except Exception as e:
            print(str(e))
            self._popJanela(f"Não foi possível {self._telacad.bt_cad_atual.text} o colaborador!!!")

    def _limpar_tela_listar(self):
        self._telalistar.txi_pesq_id.text = ""
        self._telalistar.txi_pesq_nome.text = ""
        cabecalho = [
            self._telalistar.ids.col_id,
            self._telalistar.ids.col_nome,
            self._telalistar.ids.col_endereco,
            self._telalistar.ids.col_sexo,
            self._telalistar.ids.col_data_nasci,
            self._telalistar.ids.col_salario,
            self._telalistar.ids.col_departamento,
            self._telalistar.ids.lbl_atual,
            self._telalistar.ids.lbl_excluir
        ]
        self._telalistar.layout_lista_colaboradores.clear_widgets()
        for c in cabecalho:
            self._telalistar.layout_lista_colaboradores.add_widget(c)

    def busca_colaborador(self, nome=""):
        try:
            control = ColaboradorCtrl()
            id_pesq = self._telalistar.txi_pesq_id.text
            resultado = control.buscar_colaborador(id=id_pesq, nome=nome)
            self._limpar_tela_listar()
            for res in resultado:
                res['btAtualizar'].bind(on_release=partial(self._gt.tela_cadastro_colaborador, res['lblId'].text))
                res['btExcluir'].bind(on_release=partial(self._gt.tela_cadastro_colaborador, res['lblId'].text))
                self._telalistar.layout_lista_colaboradores.add_widget(res['lblId'])
                self._telalistar.layout_lista_colaboradores.add_widget(res['lblNome'])
                self._telalistar.layout_lista_colaboradores.add_widget(res['lblEndereco'])
                self._telalistar.layout_lista_colaboradores.add_widget(res['lblSexo'])
                self._telalistar.layout_lista_colaboradores.add_widget(res['lblDataNasci'])
                self._telalistar.layout_lista_colaboradores.add_widget(res['lblSalario'])
                self._telalistar.layout_lista_colaboradores.add_widget(res['lblDepartamento'])
                self._telalistar.layout_lista_colaboradores.add_widget(res['btAtualizar'])
                self._telalistar.layout_lista_colaboradores.add_widget(res['btExcluir'])
        except Exception as e:
            print(e)

    def montar_tela_at(self, id_colaborador="", botao=None):
        control = ColaboradorCtrl()
        self._montar_spinner()
        colaboradores = []
        if id_colaborador:
            colaboradores = control.buscar_colaborador(id=id_colaborador)
        if colaboradores:
            for c in colaboradores:
                self._telacad.lbl_id.text = c["lblId"].text
                self._telacad.txi_nome.text = c["lblNome"].text
                self._telacad.txi_endereco.text = c["lblEndereco"].text
                self._telacad.txi_sexo.text = c["lblSexo"].text
                self._telacad.txi_datanasci.text = c["lblDataNasci"].text
                self._telacad.txi_salario.text = c["lblSalario"].text
                self._telacad.sp_colaborador.text = c["lblDepartamento"].text
                self._telacad.bt_cad_atual.text = botao.text

    def _montar_spinner(self):
        lista_valores = self._buscar_departamentos_tela()
        self._telacad.sp_departamento.values = lista_valores


    def _buscar_departamentos_tela(self):
        control = ColaboradorCtrl()
        departamentos = control.buscarDepartamentos()
        nomesDepartamentos =[]
        for departamento in departamentos:
            nomesDepartamentos.append(departamento['nome'])
        return str(nomesDepartamentos)

    def _limpar_tela(self):
        self._telacad.lbl_id.text = ""
        self._telacad.txi_nome.text = ""
        self._telacad.txi_endereco.text = ""
        self._telacad.txi_sexo.text = ""
        self._telacad.txi_nasc.text = ""
        self._telacad.txi_salario.text = ""
        self._telacad.sp_departamento.text = "Selecione..."
        self._telacad.bt_cad_atual.text = "Cadastrar"

    def _popJanela(self, texto=""):
        popup = Popup(title='Informação', content=Label(text=texto), auto_dismiss=True)
        popup.size_hint = (0.98, 0.4)
        popup.open()

    def alternar_pesq(self, tipo):
        if self._telalistar.txi_pesq_id:
            self._telalistar.txi_pesq_id.text = ""
        if self._telalistar.txi_pesq_nome:
            self._telalistar.txi_pesq_nome.text = ""
        pesqNome = self._telalistar.gl_pesquisa_nome
        pesqId = self._telalistar.gl_pesquisa_id
        self._telalistar.pesq.remove_widget(pesqNome)
        self._telalistar.pesq.remove_widget(pesqId)
        if tipo == "id":
            pesqId.active = True
            pesqNome.active = False
            self._telalistar.pesq.add_widget(pesqId, 2)
        elif tipo == "nome":
            pesqNome.active = True
            pesqId.active = False
            self._telalistar.pesq.add_widget(pesqNome,2)