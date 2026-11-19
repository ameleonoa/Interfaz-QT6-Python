import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox

from principal import Ui_MainWindow


class FormularioEstudiante(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnGuardar.clicked.connect(self.guardar)

    def guardar(self):
        nombre = self.ui.inputNombre.text().strip()
        apellido = self.ui.inputApellido.text().strip()
        matricula = self.ui.inputMatricula.text().strip()
        telefono = self.ui.inputTelefono.text().strip()

        if not all((nombre, apellido, matricula, telefono)):
            QMessageBox.warning(
                self,
                "Campos incompletos",
                "Completa todos los campos.",
            )
            return

        QMessageBox.information(
            self,
            "Registro guardado",
            f"Nombre: {nombre}\nApellido: {apellido}\n"
            f"Matricula: {matricula}\nTelefono: {telefono}",
        )


def main():
    app = QApplication(sys.argv)
    ventana = FormularioEstudiante()
    ventana.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
