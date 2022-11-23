from PyQt6 import uic
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
import sys
import autorization
import register
import login
import kabinet
from PyQt6 import QtWidgets
import json
from cypher import *
import os.path


global input_log, input_pass, xor

app = QApplication(sys.argv)


def open_main():
    global main_window
    global main_ui
    main_window = QMainWindow()
    main_ui = autorization.Ui_MainWindow()
    main_ui.setupUi(main_window)
    main_window.show()


def open_auth():
    global auth_window
    global auth_ui
    main_window.close()
    auth_window = QMainWindow()
    auth_ui = login.Ui_authorization()
    auth_ui.setupUi(auth_window)
    auth_window.show()
    auth_ui.loginbtn.clicked.connect(handle_auth)


def open_reg():
    global reg_window
    global reg_ui
    main_window.close()
    reg_window = QMainWindow()
    reg_ui = register.Ui_registration()
    reg_ui.setupUi(reg_window)
    reg_window.show()
    reg_ui.regbtn.clicked.connect(handle_reg)


def handle_reg():
    user = {"login": reg_ui.new_login.text(), "password": reg_ui.new_pass.text()}
    if os.path.isfile("cred.json"):
        with open("cred.json", "r", encoding='utf-8') as file:
            users = json.loads(cypher(file.read(), key))
    else:
        users = []
    with open("cred.json", "w", encoding='utf-8') as file:
        users.append(user)
        file.write(cypher(json.dumps(users), key))
    open_kab()
    reg_window.close()


def handle_auth():
    user = {"login": auth_ui.input_login.text(), "password": auth_ui.input_password.text()}
    if os.path.isfile("cred.json"):
        with open("cred.json", "r", encoding='utf-8') as file:
            users = json.loads(cypher(file.read(), key))
    else:
        users = []
    if user in users:
        open_kab()
        auth_window.close()
    else:
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Ошибка")
        msgBox.setText("Вы ввели неправильный логин или пароль")
        msgBox.exec()

def open_kab():
    global kab_window
    global kab_ui
    kab_window = QMainWindow()
    kab_ui = kabinet.Ui_kabinet()
    kab_ui.setupUi(kab_window)
    kab_ui.kabcyph.clicked.connect(show_cypher)
    kab_ui.kabdecyph.clicked.connect(show_decypher)
    kab_ui.cypher_btn.clicked.connect(output_cypher)
    kab_ui.decypher_btn.clicked.connect(output_decypher)
    kab_ui.exitkab.clicked.connect(exit_click)
    kab_window.show()


def show_cypher():
    kab_ui.stackedWidget.setCurrentWidget(kab_ui.cypher_window)


def show_decypher():
    kab_ui.stackedWidget.setCurrentWidget(kab_ui.decypher_window)


def output_cypher():
    text = kab_ui.cypher_le.text()
    with open('output.txt', "w", encoding='utf-8') as f:
        f.write(cypher(text,key))


def output_decypher():
    text = kab_ui.decypher_le.text()
    with open('output.txt', "w", encoding='utf-8') as f:
        f.write(cypher(text, key))

def exit_click():
    kab_window.close()
    main_window.show()


open_main()


main_ui.pushButton.clicked.connect(open_auth)
main_ui.pushButton_2.clicked.connect(open_reg)

app.exec()