from PyQt6 import uic
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
import sys

from register import *
from login import *
from kabinet import *
from PyQt6 import QtCore, QtGui, QtWidgets

Form, Window = uic.loadUiType("autorization.ui")

global input_log, input_pass

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

def auth_click():
    global authorization
    authorization = QtWidgets.QMainWindow()
    form = Ui_authorization()
    form.setupUi(authorization)
    form.loginbtn.clicked.connect(login_OK_click)
    window.close()
    authorization.show()

def reg_click():
    global registration
    registration = QtWidgets.QMainWindow()
    form = Ui_registration()
    form.setupUi(registration)
    form.regbtn.clicked.connect(reg_OK_click)
    window.close()
    registration.show()


def reg_OK_click():
    global kabinet
    kabinet = QtWidgets.QMainWindow()
    form = Ui_kabinet()
    form.setupUi(kabinet)
    form.exitkab.clicked.connect(exit_click)
    registration.close()
    kabinet.show()


def login_OK_click():
    global authorization
    form = Ui_authorization()
    form.setupUi(authorization)
    input_log = str(form.gettext())
    input_pass = str(form.input_password.text())
    with open('logins.txt') as f:
        userdata = f.readline()
        while userdata != input_log + "-" + input_pass and userdata != "":
            userdata = f.readline()
        if userdata is input_log + "-" + input_pass:
            global kabinet
            kabinet = QtWidgets.QMainWindow()
            form = Ui_kabinet()
            form.setupUi(kabinet)
            form.exitkab.clicked.connect(exit_click)
            authorization.close()
            kabinet.show()
        else:
            print("хацкер")

def exit_click():
    kabinet.close()
    window.show()

form.pushButton.clicked.connect(auth_click)
form.pushButton_2.clicked.connect(reg_click)

app.exec()