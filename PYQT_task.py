from PyQt5.QtWidgets import *
import json

class MyWindow(QWidget):

    Cities = {
        "Tashkent": ["Tashkent", "Chirchiq", "Angren", "Olmaliq", "Yangiyul"],
        "Samarkand": ["Samarkand", "Katta Kurgan", "Bulungur", "Juma", "Panjakent"],
        "Bukhara": ["Bukhara", "Guzar", "Kagan", "Koykon", "Shavkul"],
        "Khorezm": ["Urgench", "Khiva", "Shavat", "Turtkul", "Gurlan"],
        "Fergana": ["Fergana", "Kokand", "Margilan", "Rishtan", "Quvasay"],
        "Namangan": ["Namangan", "Chust", "Popkorn", "Khanabad", "Kasaba"],
        "Andijan": ["Andijan", "Shahrixon", "Jalayir", "Aska", "Khanabad"],
        "Kashkadarya": ["Qarshi", "Kitob", "Boysun", "Quzar", "G'izduvan"],
        "Surkhandarya": ["Termez", "Sherboyni", "Sariosiy", "Denov", "Angor"],
        "Jizzakh": ["Jizzakh", "Zarafshan", "Forqueta", "Yangigul", "Yangirul"],
        "Navoiy": ["Navoiy", "Kyzylkum", "Uchquduk", "Karumkum", "Guzar"],
        "Karakalpakstan": ["Nukus", "Muizhnak", "Kungrad", "Beruniy", "Taquantau"]
        }

    def __init__(self):
        super().__init__()

        self.v_main_lay = QVBoxLayout()
        self.h_main_lay = QHBoxLayout()
        self.v_lbl_lay = QVBoxLayout()
        self.h_secondary = QHBoxLayout()
        self.v_choice = QVBoxLayout()
        self.h_btn_lay = QHBoxLayout()

        self.setWindowTitle("Information")

        self.lbl_jins = QLabel("Jins")
        self.lbl_jins.setStyleSheet("font-size: 15px")
        self.lbl_city = QLabel("City")
        self.lbl_city.setStyleSheet("font-size: 15px")
        self.r_male = QRadioButton("Male")
        self.r_female = QRadioButton("Female")

        self.r_choice = QComboBox()
        self.r_choice.addItems(["None", "Tashkent", "Samarkand", "Bukhara", "Khorezm", "Fergana", "Namangan","Andijan",
                                "Kashkadarya", "Surkhandarya", "Jizzakh", "Navoiy", ])
        self.r_choice.activated.connect(self.City)
        self.c_choice = QComboBox()
        self.c_choice.hide()
        self.s_btn = QPushButton("Sumbit")
        self.s_btn.clicked.connect(self.Submit)
        self.e_btn = QPushButton("Exit")
        self.e_btn.clicked.connect(self.Exit)

        self.name_editor = QLineEdit()
        self.name_editor.setPlaceholderText("Name")
        self.second_editor = QLineEdit()
        self.second_editor.setPlaceholderText("Second")
        self.age_editor = QLineEdit()
        self.age_editor.setPlaceholderText("Age")

        self.h_main_lay.addWidget(self.lbl_jins)
        self.h_main_lay.addWidget(self.r_male)
        self.h_main_lay.addWidget(self.r_female)

        self.v_lbl_lay.addWidget(self.lbl_city)
        self.v_choice.addWidget(self.r_choice)
        self.v_choice.addWidget(self.c_choice)

        self.h_secondary.addLayout(self.v_lbl_lay)
        self.h_secondary.addLayout(self.v_choice)

        self.h_btn_lay.addWidget(self.s_btn)
        self.h_btn_lay.addWidget(self.e_btn)

        self.v_main_lay.addWidget(self.name_editor)
        self.v_main_lay.addWidget(self.second_editor)
        self.v_main_lay.addWidget(self.age_editor)
        self.v_main_lay.addLayout(self.h_main_lay)
        self.v_main_lay.addLayout(self.h_secondary)
        self.v_main_lay.addLayout(self.h_btn_lay)

        self.setLayout(self.v_main_lay)

    def Submit(self):
        info = True
        if not self.name_editor.text().strip() and not self.second_editor.text().strip() and not self.age_editor.text().strip():
            QMessageBox.warning(self, "Warning", "Please fill all the sections")
            info = False
            return
        if self.r_choice.currentIndex() == 0:
            QMessageBox.warning(self, "Warning", "Please choose Region")
            info = False
            return
        if not self.r_male.isChecked() and not self.r_female.isChecked():
            QMessageBox.warning(self, "Warning", "Please choose Male or Female")
            info = False
            return

        if self.r_male.isChecked:
            jins = "Male"
        else:
            jins = "Female"

        for i in self.name_editor.text().split():
            if not i.isalpha():
                QMessageBox.warning(self, "Warning", "Please enter letters only for 'Name'")
                info = False

        for i in self.second_editor.text().split():
            if not i.isalpha():
                QMessageBox.warning(self, "Warning", "Please enter letters only for 'Second'")
                info = False

        for i in self.age_editor.text().split():
            if not i.isdigit():
                QMessageBox.warning(self, "Warning", "Please enter integer only for 'age'")
                info = False
        if info:
            data = {"name": self.name_editor.text(),
                    "second": self.second_editor.text(),
                    "age": self.age_editor.text(),
                    "Jins": jins,
                    "Region": self.r_choice.currentText(),
                    "City": self.c_choice.currentText()
                    }
        
            f = open("Info.json", "w")
            json.dump(data, f, indent= 4)
            f.close()

            self.name_editor.clear()
            self.second_editor.clear()
            self.age_editor.clear()

    def Exit(self):
        self.close()

    def City(self):
        self.c_choice.clear()
        self.c_choice.show()
        if self.r_choice.currentIndex() == 0:
            self.c_choice.hide()
        if self.r_choice.currentText() in self.Cities:
            self.c_choice.addItems(self.Cities[self.r_choice.currentText()])

app = QApplication([])
win = MyWindow()

win.show()
app.exec_()
