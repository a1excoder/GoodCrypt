from PySide2.QtGui import QIcon
from PySide2.QtWidgets import *

from gui import Ui_WizardPage

from tkinter import Tk
from tkinter.filedialog import askopenfilenames

import sys
import os
import pyAesCrypt
import webbrowser
import random



if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('welcome.ico'))


    Form = QWidget()
    ui = Ui_WizardPage()
    ui.setupUi(Form)
    Form.show()


    def start_random_pass():
        password_2 = ''
        for x in range(34):
            password_2 = password_2 + random.choice(list('+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'))
        ui.lineEdit.setText(password_2)


    def start_crypt():
        if ui.lineEdit.text() == '':
            ui.label_5.setText("Введите пароль!")
        else:
            password = ui.lineEdit.text()
            bufferSize = 512 * 1024
            Tk().withdraw()
            filename = askopenfilenames()


            for file_name in filename:
                pyAesCrypt.encryptFile(str(file_name), str(file_name) + ".aes", password, bufferSize)
                os.remove(file_name)
                ui.label_5.setText("Файлы зашифрованы!")
            




    def start_decrypt():
        if ui.lineEdit_3.text() == '':
            ui.label_6.setText("Введите пароль!")
        else:
            password = ui.lineEdit_3.text()
            bufferSize = 512 * 1024
            Tk().withdraw()
            filename = askopenfilenames()

            try:
                for file_name in filename:
                    pyAesCrypt.decryptFile(str(file_name),str(os.path.splitext(file_name)[0]),password,bufferSize)
                    os.remove(file_name)
                    ui.label_6.setText("Файлы расшифрованы!")
            except:
                ui.label_6.setText("Пароль не верный!")





    def site_dev():
        webbrowser.open("https://a1excode.netxisp.host/", new=0, autoraise=True)

    def quit():
        sys.exit()



    ui.pushButton.clicked.connect( start_crypt )
    ui.pushButton_3.clicked.connect( start_random_pass )


    ui.pushButton_9.clicked.connect( quit )
    ui.pushButton_10.clicked.connect( quit )


    ui.commandLinkButton.clicked.connect( site_dev )

    ui.pushButton_8.clicked.connect( start_decrypt )


sys.exit(app.exec_())