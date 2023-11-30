import random
import sys
from PyQt6.QtWidgets import QApplication, QDialog
from layout import Ui_Dialog

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.zamow.clicked.connect(self.pizza)
        self.show()

    def pizza(self):
        cena = 0

        if self.ui.Hawajska.isChecked():
            cena = 30
            pizza = "Hawajska"
        elif self.ui.Margherita.isCheched():
            cena = 28
            pizza = "Margherita"
        elif self.ui.Capricciosa.isCheched():
            cena = 32
            pizza = "Capricciosa"
        elif self.ui.Quattro.isCheched():
            cena = 34
            pizza = "Quattro formaggi"
        elif self.ui.Ser.isCheched():
            cena = 5

        mail = self.ui.mail.text()

        time = random.randint(10,100)

        if "@" in mail:
            self.ui.result.setText(f"Klient {mail} zamówił pizze: {pizza}. Cenna: {cena} złotych. Przewidywany czas dostawy wynosi: {time} minut. Prosze o cierpliwość")
        else:
            self.ui.result.setText(f"Mail musi zawierac @")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec())