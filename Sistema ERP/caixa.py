# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'venda.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

###IMPORTS SISTEMA###
import mysql.connector
import pandas as pd

### ARQUIVOS VARIAVEIS DE CONTROLE###
import variaveisControle

###VARIAVEIS DE CONEXÃO COM BANCO DE DADOS###
host = variaveisControle.host
user = variaveisControle.user
password = variaveisControle.password
database = variaveisControle.database

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(456, 296)
        Form.setStyleSheet("background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.lb_produto = QtWidgets.QLabel(Form)
        self.lb_produto.setGeometry(QtCore.QRect(40, 92, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lb_produto.setFont(font)
        self.lb_produto.setStyleSheet("color: rgb(255, 255, 255);")
        self.lb_produto.setObjectName("lb_produto")
        self.qb_produto = QtWidgets.QComboBox(Form)
        self.qb_produto.setGeometry(QtCore.QRect(140, 100, 311, 31))
        self.qb_produto.setStyleSheet("color: rgb(255, 255, 255);")
        self.qb_produto.setObjectName("qb_produto")
        self.lb_quantidade = QtWidgets.QLabel(Form)
        self.lb_quantidade.setGeometry(QtCore.QRect(50, 170, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lb_quantidade.setFont(font)
        self.lb_quantidade.setStyleSheet("color: rgb(255, 255, 255);")
        self.lb_quantidade.setObjectName("lb_quantidade")
        self.sb_quantidade = QtWidgets.QSpinBox(Form)
        self.sb_quantidade.setGeometry(QtCore.QRect(130, 170, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.sb_quantidade.setFont(font)
        self.sb_quantidade.setStyleSheet("color: rgb(255, 255, 255);")
        self.sb_quantidade.setObjectName("sb_quantidade")
        self.lb_cliente = QtWidgets.QLabel(Form)
        self.lb_cliente.setGeometry(QtCore.QRect(40, 30, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lb_cliente.setFont(font)
        self.lb_cliente.setStyleSheet("color: rgb(255, 255, 255);")
        self.lb_cliente.setObjectName("lb_cliente")
        self.qb_cliente = QtWidgets.QComboBox(Form)
        self.qb_cliente.setGeometry(QtCore.QRect(140, 40, 311, 31))
        self.qb_cliente.setStyleSheet("color: rgb(255, 255, 255);")
        self.qb_cliente.setObjectName("qb_cliente")
        self.bt_cancela = QtWidgets.QPushButton(Form)
        self.bt_cancela.setGeometry(QtCore.QRect(260, 220, 81, 71))
        self.bt_cancela.setStyleSheet("image: url(:/icon_cancela/icons/cancelar.png);")
        self.bt_cancela.setText("")
        self.bt_cancela.setObjectName("bt_cancela")
        self.bt_adicionar = QtWidgets.QPushButton(Form)
        self.bt_adicionar.setGeometry(QtCore.QRect(130, 220, 81, 71))
        self.bt_adicionar.setStyleSheet("image: url(:/icon_add/icons/adicionar.png);")
        self.bt_adicionar.setText("")
        self.bt_adicionar.setObjectName("bt_adicionar")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Caixa"))
        self.lb_produto.setText(_translate("Form", "Produto:"))
        self.lb_quantidade.setText(_translate("Form", "Qtd:"))
        self.lb_cliente.setText(_translate("Form", "Cliente:"))
        self.bt_cancela.setToolTip(_translate("Form", "<html><head/><body><p><img src=\":/icon_add/icons/adicionar.png\"/></p></body></html>"))
        self.bt_adicionar.setToolTip(_translate("Form", "<html><head/><body><p><img src=\":/icon_add/icons/adicionar.png\"/></p></body></html>"))

        self.qb_cliente.activated.connect(self.inserirCliente)

    def inserirCliente(self):
        # Conexão com o banco de dados #
        mydb = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        mycursor = mydb.cursor()
        consultaSQL = "SELECT Nome FROM cliente"
        mycursor.execute(consultaSQL)
        clients = mycursor.fetchall()

        # Populate qb_cliente combo box with fetched clients
        self.qb_cliente.clear()
        self.qb_cliente.addItems([client[0] for client in clients])

        # Close the database connection
        mycursor.close()

### Imagens Vendas ###
import icon_add
import icon_cancela


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
