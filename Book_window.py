from PyQt5.QtWidgets import *
import json

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.v_main_lay = QVBoxLayout()

        self.book_lbl = QLabel("Kitob")
        self.author_lbl = QLabel("Muallif")

        self.book_edit = QLineEdit()
        self.book_edit.setPlaceholderText("...")
        self.author_edit = QLineEdit()
        self.author_edit.setPlaceholderText("...")

        self.conf_btn = QPushButton("Ro'yhatga qoshish")
        self.conf_btn.clicked.connect(self.Confirm)

        self.book_list = QLabel("Kitoblar Ro'yhati")
        self.item_list = QListWidget()

        self.v_main_lay.addWidget(self.book_lbl)
        self.v_main_lay.addWidget(self.book_edit)
        self.v_main_lay.addWidget(self.author_lbl)
        self.v_main_lay.addWidget(self.author_edit)
        self.v_main_lay.addWidget(self.conf_btn)
        self.v_main_lay.addStretch()
        self.v_main_lay.addWidget(self.book_list)
        self.v_main_lay.addWidget(self.item_list)

        self.setLayout(self.v_main_lay)

    def Confirm(self):
        book = self.book_edit.text().strip()
        author = self.author_edit.text().strip()
        try:
            with open("data.json", "r") as f:
                data = json.load(f)
        except(FileNotFoundError, json.JSONDecodeError):
            data = {}
        if author:
            if book:
                if author not in data:
                    data[book] = author
                    with open("data.json", "w") as f:
                        f.seek(0)
                        json.dump(data, f, indent=4)
                    self.book_edit.clear()
                    self.author_edit.clear()
                else:
                    if book in data:
                        QMessageBox.critical(self, "Message", "This book exists")
                    else:
                        data[book] = author
                        with open("data.json", "w") as f:
                            f.seek(0)
                            json.dump(data, f, indent=4)
                        self.book_edit.clear()
                        self.author_edit.clear()
            else:
                QMessageBox.critical(self, "Message", "Please fill all partas")
        else:
            QMessageBox.critical(self, "Message", "Please fill all partas")
        
        with open("data.json", "r") as f:
            data = json.load(f)
            for key, value in data.items():
                self.item_list.addItem(f"{value} \t {key}")

app = QApplication([])
win = MyWindow()

win.show()
app.exec_()
