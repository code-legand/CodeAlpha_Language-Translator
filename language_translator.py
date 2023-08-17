from PyQt5 import QtCore, QtGui, QtWidgets
import requests
import json

with open("key.txt") as file:
    API_KEY = file.read()


class Ui_MainWindow(object):
    target_language = ""
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(771, 551)
        MainWindow.setStyleSheet("background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));")

        MainWindow.setWindowIcon(QtGui.QIcon('translate_icon.png'))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.input_text = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.input_text.setFont(font)
        self.input_text.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.input_text.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.input_text.setStyleSheet("background-color: rgb(247, 249, 249);\n "
"")
        self.input_text.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.input_text.setPlainText("")
        self.input_text.setObjectName("input_text")
        self.horizontalLayout.addWidget(self.input_text)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.languageBox = QtWidgets.QComboBox(self.centralwidget)
        self.languageBox.setMinimumSize(QtCore.QSize(0, 25))
        self.languageBox.setStyleSheet("background-color: rgb(237, 255, 255);")
        self.languageBox.setObjectName("languageBox")

        self.addLanguages()
        self.languageBox.currentIndexChanged.connect(self.changeTargetLanguage)

        self.verticalLayout.addWidget(self.languageBox)
        self.convert_button = QtWidgets.QPushButton(self.centralwidget)
        self.convert_button.setMinimumSize(QtCore.QSize(100, 100))
        # self.convert_button.setMaximumSize(QtCore.QSize(100, 100))
        self.convert_button.setStyleSheet("background-image: url(translate_icon.png);\n"
"background-color: rgb(207, 255, 255); \n"
"background-repeat: no-repeat;\n"
"background-position: center;\n")
        self.convert_button.setText("")
        self.convert_button.setObjectName("convert_button")

        self.convert_button.clicked.connect(self.translateText)

        self.verticalLayout.addWidget(self.convert_button)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.input_text_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.input_text_2.setFont(font)
        self.input_text_2.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.input_text_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.input_text_2.setStyleSheet("background-color: rgb(247, 249, 249);\n"
"")
        self.input_text_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.input_text_2.setReadOnly(True)
        self.input_text_2.setPlainText("")
        self.input_text_2.setObjectName("input_text_2")
        self.horizontalLayout.addWidget(self.input_text_2)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 771, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Language Translator"))
        self.input_text.setPlaceholderText(_translate("MainWindow", "Enter text to translate"))


    def addLanguages(self):
        url = "https://api.apilayer.com/language_translation/languages"

        payload = {}
        headers= {
        "apikey": API_KEY
        }

        response = requests.request("GET", url, headers=headers, data = payload)

        result = response.text
        result = json.loads(result)
        language_objects = result['languages']
        language_codes = [lang["language"] for lang in language_objects]
        language_names = {lang["language"]:lang["language_name"] for lang in language_objects}
        self.languageBox.addItems(language_names.values())
        self.language_codes = language_codes
        self.language_names = language_names

    def changeTargetLanguage(self, index):
        self.target_language = self.language_codes[index]

    def translateText(self):
        text = self.input_text.toPlainText()
        url = f"https://api.apilayer.com/language_translation/translate?target={self.target_language}&source=en"

        payload = f"{text}".encode("utf-8")
        headers= {
        "apikey": API_KEY
        }

        response = requests.request("POST", url, headers=headers, data = payload)

        status_code = response.status_code
        result = response.text
        result = json.loads(result)

        if status_code == 200:
            result = result["translations"][0]["translation"]
            self.input_text_2.setPlainText(result)
        else:
            result = result["error"]
            self.input_text_2.setPlainText(result)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
