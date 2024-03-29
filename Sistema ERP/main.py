# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

###Abrir Telas###
from cliente import Ui_formCliente
from caixa import Ui_Form

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(812, 187)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lb_logoEmpresa = QtWidgets.QLabel(self.centralwidget)
        self.lb_logoEmpresa.setGeometry(QtCore.QRect(260, 100, 241, 51))
        self.lb_logoEmpresa.setStyleSheet("image: url(:/logo_empresa/logo_empresa.png)")
        self.lb_logoEmpresa.setText("")
        self.lb_logoEmpresa.setObjectName("lb_logoEmpresa")
        self.bt_cliente = QtWidgets.QPushButton(self.centralwidget)
        self.bt_cliente.setGeometry(QtCore.QRect(0, 0, 91, 81))
        self.bt_cliente.setStyleSheet("image:url(:/icon_cliente/icons/cliente.png)")
        self.bt_cliente.setText("")
        self.bt_cliente.setObjectName("bt_cliente")
        self.bt_fornecedor = QtWidgets.QPushButton(self.centralwidget)
        self.bt_fornecedor.setGeometry(QtCore.QRect(90, 0, 91, 81))
        self.bt_fornecedor.setStyleSheet("image: url(:/icon_fornecedor/icons/fornecedor.png)")
        self.bt_fornecedor.setText("")
        self.bt_fornecedor.setObjectName("bt_fornecedor")
        self.bt_vendas = QtWidgets.QPushButton(self.centralwidget)
        self.bt_vendas.setGeometry(QtCore.QRect(270, 0, 91, 81))
        self.bt_vendas.setStyleSheet("image:url(:/icon_vendas/icons/venda.png)")
        self.bt_vendas.setText("")
        self.bt_vendas.setObjectName("bt_vendas")
        self.bt_produtos = QtWidgets.QPushButton(self.centralwidget)
        self.bt_produtos.setGeometry(QtCore.QRect(180, 0, 91, 81))
        self.bt_produtos.setStyleSheet("image:url(:/icon_produtos/icons/produtos.png)")
        self.bt_produtos.setText("")
        self.bt_produtos.setObjectName("bt_produtos")
        self.bt_bancos = QtWidgets.QPushButton(self.centralwidget)
        self.bt_bancos.setGeometry(QtCore.QRect(450, 0, 91, 81))
        self.bt_bancos.setStyleSheet("image: url(:/icon_bancos/icons/banco.png)")
        self.bt_bancos.setText("")
        self.bt_bancos.setObjectName("bt_bancos")
        self.bt_pagar = QtWidgets.QPushButton(self.centralwidget)
        self.bt_pagar.setGeometry(QtCore.QRect(360, 0, 91, 81))
        self.bt_pagar.setStyleSheet("image:url(:/icon_pagar/icons/contasPagar.png)")
        self.bt_pagar.setText("")
        self.bt_pagar.setObjectName("bt_pagar")
        self.bt_caixa = QtWidgets.QPushButton(self.centralwidget)
        self.bt_caixa.setGeometry(QtCore.QRect(630, 0, 91, 81))
        self.bt_caixa.setStyleSheet("image: url(:/icon_caixa/icons/caixa.png)")
        self.bt_caixa.setText("")
        self.bt_caixa.setObjectName("bt_caixa")
        self.bt_receber = QtWidgets.QPushButton(self.centralwidget)
        self.bt_receber.setGeometry(QtCore.QRect(540, 0, 91, 81))
        self.bt_receber.setStyleSheet("image:url(:/icon_receber/icons/receber.png)")
        self.bt_receber.setText("")
        self.bt_receber.setObjectName("bt_receber")
        self.bt_sair = QtWidgets.QPushButton(self.centralwidget)
        self.bt_sair.setGeometry(QtCore.QRect(720, 0, 91, 81))
        self.bt_sair.setStyleSheet("image: url(:/icon_sair/icons/sair.png)")
        self.bt_sair.setText("")
        self.bt_sair.setObjectName("bt_sair")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 812, 21))
        self.menubar.setObjectName("menubar")
        self.menuCadastro = QtWidgets.QMenu(self.menubar)
        self.menuCadastro.setObjectName("menuCadastro")
        self.menuOpera_es = QtWidgets.QMenu(self.menubar)
        self.menuOpera_es.setObjectName("menuOpera_es")
        self.menuSa_da_de_Produtos = QtWidgets.QMenu(self.menuOpera_es)
        self.menuSa_da_de_Produtos.setObjectName("menuSa_da_de_Produtos")
        self.menuEstoque = QtWidgets.QMenu(self.menuOpera_es)
        self.menuEstoque.setObjectName("menuEstoque")
        self.menuCompras = QtWidgets.QMenu(self.menuOpera_es)
        self.menuCompras.setObjectName("menuCompras")
        self.menuFinaceiro = QtWidgets.QMenu(self.menubar)
        self.menuFinaceiro.setObjectName("menuFinaceiro")
        self.menuConsultas = QtWidgets.QMenu(self.menubar)
        self.menuConsultas.setObjectName("menuConsultas")
        self.menuVendas = QtWidgets.QMenu(self.menuConsultas)
        self.menuVendas.setObjectName("menuVendas")
        self.menuConsumos = QtWidgets.QMenu(self.menuConsultas)
        self.menuConsumos.setObjectName("menuConsumos")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpera_es = QtWidgets.QAction(MainWindow)
        self.actionOpera_es.setObjectName("actionOpera_es")
        self.actionCliente = QtWidgets.QAction(MainWindow)
        self.actionCliente.setObjectName("actionCliente")
        self.actionFornecedor = QtWidgets.QAction(MainWindow)
        self.actionFornecedor.setObjectName("actionFornecedor")
        self.actionUsuarios = QtWidgets.QAction(MainWindow)
        self.actionUsuarios.setObjectName("actionUsuarios")
        self.actionFuncionarios = QtWidgets.QAction(MainWindow)
        self.actionFuncionarios.setObjectName("actionFuncionarios")
        self.actionVenda = QtWidgets.QAction(MainWindow)
        self.actionVenda.setObjectName("actionVenda")
        self.actionComsumo_de_Produtos = QtWidgets.QAction(MainWindow)
        self.actionComsumo_de_Produtos.setObjectName("actionComsumo_de_Produtos")
        self.actionSaldo = QtWidgets.QAction(MainWindow)
        self.actionSaldo.setObjectName("actionSaldo")
        self.actionCompras_2 = QtWidgets.QAction(MainWindow)
        self.actionCompras_2.setObjectName("actionCompras_2")
        self.actionPedido = QtWidgets.QAction(MainWindow)
        self.actionPedido.setObjectName("actionPedido")
        self.actionCancelar_Compras = QtWidgets.QAction(MainWindow)
        self.actionCancelar_Compras.setObjectName("actionCancelar_Compras")
        self.actionCAixa = QtWidgets.QAction(MainWindow)
        self.actionCAixa.setObjectName("actionCAixa")
        self.actionContas_Bancos = QtWidgets.QAction(MainWindow)
        self.actionContas_Bancos.setObjectName("actionContas_Bancos")
        self.actionContas_a_Pagar = QtWidgets.QAction(MainWindow)
        self.actionContas_a_Pagar.setObjectName("actionContas_a_Pagar")
        self.actionContas_a_Receber = QtWidgets.QAction(MainWindow)
        self.actionContas_a_Receber.setObjectName("actionContas_a_Receber")
        self.actionContas_Recebidas = QtWidgets.QAction(MainWindow)
        self.actionContas_Recebidas.setObjectName("actionContas_Recebidas")
        self.actionGeral = QtWidgets.QAction(MainWindow)
        self.actionGeral.setObjectName("actionGeral")
        self.actionResumido = QtWidgets.QAction(MainWindow)
        self.actionResumido.setObjectName("actionResumido")
        self.actionGeral_2 = QtWidgets.QAction(MainWindow)
        self.actionGeral_2.setObjectName("actionGeral_2")
        self.actionResumido_2 = QtWidgets.QAction(MainWindow)
        self.actionResumido_2.setObjectName("actionResumido_2")
        self.menuCadastro.addSeparator()
        self.menuCadastro.addAction(self.actionCliente)
        self.menuCadastro.addAction(self.actionFornecedor)
        self.menuCadastro.addAction(self.actionUsuarios)
        self.menuCadastro.addAction(self.actionFuncionarios)
        self.menuSa_da_de_Produtos.addAction(self.actionVenda)
        self.menuSa_da_de_Produtos.addAction(self.actionComsumo_de_Produtos)
        self.menuEstoque.addAction(self.actionSaldo)
        self.menuCompras.addAction(self.actionCompras_2)
        self.menuCompras.addAction(self.actionPedido)
        self.menuCompras.addAction(self.actionCancelar_Compras)
        self.menuOpera_es.addAction(self.menuSa_da_de_Produtos.menuAction())
        self.menuOpera_es.addAction(self.menuEstoque.menuAction())
        self.menuOpera_es.addAction(self.menuCompras.menuAction())
        self.menuFinaceiro.addAction(self.actionCAixa)
        self.menuFinaceiro.addAction(self.actionContas_Bancos)
        self.menuFinaceiro.addAction(self.actionContas_a_Pagar)
        self.menuFinaceiro.addSeparator()
        self.menuFinaceiro.addAction(self.actionContas_a_Receber)
        self.menuFinaceiro.addAction(self.actionContas_Recebidas)
        self.menuVendas.addAction(self.actionGeral)
        self.menuVendas.addAction(self.actionResumido)
        self.menuConsumos.addAction(self.actionGeral_2)
        self.menuConsumos.addAction(self.actionResumido_2)
        self.menuConsultas.addAction(self.menuVendas.menuAction())
        self.menuConsultas.addAction(self.menuConsumos.menuAction())
        self.menubar.addAction(self.menuCadastro.menuAction())
        self.menubar.addAction(self.menuOpera_es.menuAction())
        self.menubar.addAction(self.menuFinaceiro.menuAction())
        self.menubar.addAction(self.menuConsultas.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sistema ERP"))
        self.lb_logoEmpresa.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.bt_cliente.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.bt_fornecedor.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.bt_vendas.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.bt_produtos.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.bt_bancos.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.bt_pagar.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.bt_caixa.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.bt_receber.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.bt_sair.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.menuCadastro.setTitle(_translate("MainWindow", "Cadastros"))
        self.menuOpera_es.setTitle(_translate("MainWindow", "Operações"))
        self.menuSa_da_de_Produtos.setTitle(_translate("MainWindow", "Saída de Produtos"))
        self.menuEstoque.setTitle(_translate("MainWindow", "Estoque"))
        self.menuCompras.setTitle(_translate("MainWindow", "Compras"))
        self.menuFinaceiro.setTitle(_translate("MainWindow", "Finaceiro"))
        self.menuConsultas.setTitle(_translate("MainWindow", "Consultas"))
        self.menuVendas.setTitle(_translate("MainWindow", "Vendas"))
        self.menuConsumos.setTitle(_translate("MainWindow", "Consumos"))
        self.actionOpera_es.setText(_translate("MainWindow", "Operações"))
        self.actionCliente.setText(_translate("MainWindow", "Cliente"))
        self.actionFornecedor.setText(_translate("MainWindow", "Fornecedor"))
        self.actionUsuarios.setText(_translate("MainWindow", "Usuarios"))
        self.actionFuncionarios.setText(_translate("MainWindow", "Funcionarios"))
        self.actionVenda.setText(_translate("MainWindow", "Venda"))
        self.actionComsumo_de_Produtos.setText(_translate("MainWindow", "Consumo de Produtos"))
        self.actionSaldo.setText(_translate("MainWindow", "Saldo"))
        self.actionCompras_2.setText(_translate("MainWindow", "Compras"))
        self.actionPedido.setText(_translate("MainWindow", "Pedido"))
        self.actionCancelar_Compras.setText(_translate("MainWindow", "Cancelar"))
        self.actionCAixa.setText(_translate("MainWindow", "Caixa"))
        self.actionContas_Bancos.setText(_translate("MainWindow", "Contas Bancos"))
        self.actionContas_a_Pagar.setText(_translate("MainWindow", "Contas Pagar"))
        self.actionContas_a_Receber.setText(_translate("MainWindow", "Contas Receber"))
        self.actionContas_Recebidas.setText(_translate("MainWindow", "Contas Recebidas"))
        self.actionGeral.setText(_translate("MainWindow", "Geral"))
        self.actionResumido.setText(_translate("MainWindow", "Resumido"))
        self.actionGeral_2.setText(_translate("MainWindow", "Geral "))
        self.actionResumido_2.setText(_translate("MainWindow", "Resumido"))

        ###Botõe do Sistema ###
        self.bt_sair.clicked.connect(self.sairSistema) # Fecha o sistema
        self.bt_cliente.clicked.connect(self.telaCliente)# Botão cliente abre a tela cliente
        self.actionCliente.triggered.connect(self.telaCliente)#Menu cliente abre telaCliente
        self.bt_caixa.clicked.connect(self.telaCaixa)# Botão vendas abre telaVendas

    ### Funções Sistema ###
       ##Sair Sistema##
    def sairSistema(self):
        sys.exit()

    ### Abrir Tela Cliente###
    def telaCliente(self):
        self.formCliente = QtWidgets.QWidget()
        self.ui = Ui_formCliente()
        self.ui.setupUi(self.formCliente)
        self.formCliente.show()

    ## Abre a tela caixa ##
    def telaCaixa(self):
        self.Form = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.Form)
        self.Form.show()

### Imagens do Sistema ###
import icon_bancos
import icon_caixa
import icon_cliente
import icon_fornecedor
import icon_pagar
import icon_produtos
import icon_receber
import icon_sair
import icon_vendas
import logo_empresa


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
