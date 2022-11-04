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


global input_log, input_pass

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
    with open("cred.json", "r", encoding='utf-8') as file:
        users = json.load(file)
    with open("cred.json", "w", encoding='utf-8') as file:
        users.append(user)
        json.dump(users, file)
        open_kab()
        reg_window.close()


def handle_auth():
    user = {"login": auth_ui.input_login.text(), "password": auth_ui.input_password.text()}
    with open("cred.json", "r", encoding='utf-8') as file:
        users = json.load(file)
    if user in users:
        open_kab()
        auth_window.close()
    else:
        print("Неправильный логин или пароль")

def open_kab():
    global kab_window
    global kab_ui
    kab_window = QMainWindow()
    kab_ui = kabinet.Ui_kabinet()
    kab_ui.setupUi(kab_window)
    kab_ui.exitkab.clicked.connect(exit_click)
    kab_window.show()


def exit_click():
    kab_window.close()
    main_window.show()

open_main()

main_ui.pushButton.clicked.connect(open_auth)
main_ui.pushButton_2.clicked.connect(open_reg)

app.exec()