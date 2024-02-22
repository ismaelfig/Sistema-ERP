import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton, QListWidget, QFileDialog, QDialog, QMessageBox, QHBoxLayout
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt

class CadastroMembroDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.membro = {}

        self.init_ui()

    def init_ui(self):
        # Componentes do diálogo
        self.label_nome = QLabel('Nome:')
        self.edit_nome = QLineEdit()

        self.label_endereco = QLabel('Endereço:')
        self.edit_endereco = QLineEdit()

        self.label_telefone = QLabel('Telefone:')
        self.edit_telefone = QLineEdit()

        self.label_nascimento = QLabel('Data de Nascimento:')
        self.edit_nascimento = QLineEdit()

        self.label_funcao = QLabel('Função:')
        self.edit_funcao = QLineEdit()

        self.label_foto = QLabel('Foto:')
        self.btn_selecionar_foto = QPushButton('Selecionar Foto')
        self.btn_selecionar_foto.clicked.connect(self.selecionar_foto)

        self.btn_cadastrar = QPushButton('Cadastrar')
        self.btn_cadastrar.clicked.connect(self.accept)

        # Layout do diálogo
        layout = QVBoxLayout()
        layout.addWidget(self.label_nome)
        layout.addWidget(self.edit_nome)
        layout.addWidget(self.label_endereco)
        layout.addWidget(self.edit_endereco)
        layout.addWidget(self.label_telefone)
        layout.addWidget(self.edit_telefone)
        layout.addWidget(self.label_nascimento)
        layout.addWidget(self.edit_nascimento)
        layout.addWidget(self.label_funcao)
        layout.addWidget(self.edit_funcao)
        layout.addWidget(self.label_foto)
        layout.addWidget(self.btn_selecionar_foto)
        layout.addWidget(self.btn_cadastrar)

        self.setLayout(layout)

    def selecionar_foto(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(self, "Selecionar Foto", "", "Image Files (*.png *.jpg *.bmp *.jpeg);;All Files (*)", options=options)

        if file_name:
            pixmap = QPixmap(file_name)
            pixmap = pixmap.scaledToWidth(100, Qt.SmoothTransformation)
            self.label_foto.setPixmap(pixmap)

    def accept(self):
        # Obter os dados do membro
        self.membro['nome'] = self.edit_nome.text()
        self.membro['endereco'] = self.edit_endereco.text()
        self.membro['telefone'] = self.edit_telefone.text()
        self.membro['data_nascimento'] = self.edit_nascimento.text()
        self.membro['funcao'] = self.edit_funcao.text()
        self.membro['foto'] = self.label_foto.pixmap().toImage() if self.label_foto.pixmap() else None

        super().accept()

    def get_membro(self):
        return self.membro

class IgrejaApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.usuarios = [{'usuario': 'admin', 'senha': 'senha123'}]
        self.usuario_logado = None
        self.membros = []
        self.ofertas_dizimos = []

        self.init_ui()

    def init_ui(self):
        # Configuração da janela principal
        self.setWindowTitle('Sistema de Gestão de Igrejas')
        self.setGeometry(100, 100, 800, 600)

        # Widget central
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Layout principal
        layout = QVBoxLayout()

        # Componentes
        self.label_membros = QLabel('Membros:')
        self.list_membros = QListWidget()
        self.btn_cadastrar_membro = QPushButton('Cadastrar Membro')
        self.btn_visualizar_membro = QPushButton('Visualizar Membro')
        self.btn_alterar_membro = QPushButton('Alterar Membro')
        self.btn_deletar_membro = QPushButton('Deletar Membro')
        self.btn_lancar_oferta_dizimo = QPushButton('Lançar Oferta/Dízimo')
        self.btn_logout = QPushButton('Logout')

        # Adicionar componentes ao layout
        layout.addWidget(self.label_membros)
        layout.addWidget(self.list_membros)
        layout.addWidget(self.btn_cadastrar_membro)
        layout.addWidget(self.btn_visualizar_membro)
        layout.addWidget(self.btn_alterar_membro)
        layout.addWidget(self.btn_deletar_membro)
        layout.addWidget(self.btn_lancar_oferta_dizimo)
        layout.addWidget(self.btn_logout)

        # Conectar botões aos slots
        self.btn_cadastrar_membro.clicked.connect(self.cadastrar_membro)
        self.btn_visualizar_membro.clicked.connect(self.visualizar_membro)
        self.btn_alterar_membro.clicked.connect(self.alterar_membro)
        self.btn_deletar_membro.clicked.connect(self.deletar_membro)
        self.btn_lancar_oferta_dizimo.clicked.connect(self.lancar_oferta_dizimo)
        self.btn_logout.clicked.connect(self.logout)

        # Configurar layout central
        central_widget.setLayout(layout)

        self.atualizar_lista_membros()
        self.show_login()

    def show_login(self):
        login_dialog = LoginDialog(self)
        if login_dialog.exec_():
            usuario, senha = login_dialog.get_login_info()
            if any(u['usuario'] == usuario and u['senha'] == senha for u in self.usuarios):
                self.usuario_logado = usuario
                self.show()
            else:
                QMessageBox.critical(self, 'Erro de Login', 'Usuário ou senha incorretos. Tente novamente.')
                self.close()

    def cadastrar_membro(self):
        # Diálogo de cadastro de membro
        dialog = CadastroMembroDialog(self)
        if dialog.exec_():
            membro = dialog.get_membro()
            self.membros.append(membro)
            self.atualizar_lista_membros()

    def visualizar_membro(self):
        # Obter o índice selecionado
        index = self.list_membros.currentRow()

        if index != -1:
            membro = self.membros[index]
            dialog = VisualizarMembroDialog(self, membro)
            dialog.exec_()

    def alterar_membro(self):
        # Obter o índice selecionado
        index = self.list_membros.currentRow()

        if index != -1:
            membro = self.membros[index]
            dialog = AlterarMembroDialog(self, membro)
            if dialog.exec_():
                novo_membro = dialog.get_membro()
                self.membros[index] = novo_membro
                self.atualizar_lista_membros()

    def deletar_membro(self):
        # Obter o índice selecionado
        index = self.list_membros.currentRow()

        if index != -1:
            resposta = QMessageBox.question(self, 'Deletar Membro', 'Tem certeza que deseja deletar este membro?',
                                            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if resposta == QMessageBox.Yes:
                del self.membros[index]
                self.atualizar_lista_membros()

    def lancar_oferta_dizimo(self):
        # Diálogo de lançamento de oferta/dízimo
        dialog = LancarOfertaDizimoDialog(self)
        if dialog.exec_():
            oferta_dizimo = dialog.get_oferta_dizimo()
            self.ofertas_dizimos.append(oferta_dizimo)

    def logout(self):
        self.close()
        self.show_login()

    def atualizar_lista_membros(self):
        self.list_membros.clear()
        for membro in self.membros:
            self.list_membros.addItem(membro['nome'])

class LoginDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.usuario = QLineEdit(self)
        self.senha = QLineEdit(self)
        self.senha.setEchoMode(QLineEdit.Password)
        self.btn_login = QPushButton('Login', self)
        self.btn_cadastrar = QPushButton('Cadastrar', self)

        layout = QVBoxLayout(self)
        layout.addWidget(QLabel('Usuário:'))
        layout.addWidget(self.usuario)
        layout.addWidget(QLabel('Senha:'))
        layout.addWidget(self.senha)
        layout.addWidget(self.btn_login)
        layout.addWidget(self.btn_cadastrar)

        self.btn_login.clicked.connect(self.accept)
        self.btn_cadastrar.clicked.connect(self.cadastrar)

    def get_login_info(self):
        return self.usuario.text(), self.senha.text()

    def cadastrar(self):
        novo_usuario_dialog = NovoUsuarioDialog(self)
        novo_usuario_dialog.exec_()

class NovoUsuarioDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.usuario = QLineEdit(self)
        self.senha = QLineEdit(self)
        self.senha.setEchoMode(QLineEdit.Password)
        self.btn_cadastrar = QPushButton('Cadastrar', self)

        layout = QVBoxLayout(self)
        layout.addWidget(QLabel('Novo Usuário:'))
        layout.addWidget(self.usuario)
        layout.addWidget(QLabel('Senha:'))
        layout.addWidget(self.senha)
        layout.addWidget(self.btn_cadastrar)

        self.btn_cadastrar.clicked.connect(self.accept)

    def get_usuario_info(self):
        return self.usuario.text(), self.senha.text()

class VisualizarMembroDialog(QDialog):
    def __init__(self, parent=None, membro=None):
        super().__init__(parent)

        self.setWindowTitle('Visualizar Membro')
        self.setGeometry(200, 200, 400, 300)

        self.label_nome = QLabel(f'Nome: {membro["nome"]}')
        self.label_endereco = QLabel(f'Endereço: {membro["endereco"]}')
        self.label_telefone = QLabel(f'Telefone: {membro["telefone"]}')
        self.label_nascimento = QLabel(f'Data de Nascimento: {membro["data_nascimento"]}')
        self.label_funcao = QLabel(f'Função: {membro["funcao"]}')
        self.label_foto = QLabel()

        if membro["foto"]:
            imagem = QImage(membro["foto"])
            pixmap = QPixmap.fromImage(imagem)
            self.label_foto.setPixmap(pixmap.scaledToWidth(100, Qt.SmoothTransformation))

        layout = QVBoxLayout(self)
        layout.addWidget(self.label_nome)
        layout.addWidget(self.label_endereco)
        layout.addWidget(self.label_telefone)
        layout.addWidget(self.label_nascimento)
        layout.addWidget(self.label_funcao)
        layout.addWidget(self.label_foto)

class AlterarMembroDialog(CadastroMembroDialog):
    def __init__(self, parent=None, membro=None):
        super().__init__(parent)

        self.setWindowTitle('Alterar Membro')
        self.setGeometry(200, 200, 400, 300)

        self.edit_nome.setText(membro["nome"])
        self.edit_endereco.setText(membro["endereco"])
        self.edit_telefone.setText(membro["telefone"])
        self.edit_nascimento.setText(membro["data_nascimento"])
        self.edit_funcao.setText(membro["funcao"])

        if membro["foto"]:
            imagem = QImage(membro["foto"])
            pixmap = QPixmap.fromImage(imagem)
            self.label_foto.setPixmap(pixmap.scaledToWidth(100, Qt.SmoothTransformation))

    def get_membro(self):
        membro = super().get_membro()
        membro['id'] = self.edit_nome.text()  # Pode ser necessário um identificador único
        return membro

if __name__ == '__main__':
    app = QApplication(sys.argv)
    igreja_app = IgrejaApp()
    sys.exit(app.exec_())
