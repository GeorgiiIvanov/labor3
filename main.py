from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from shifrowanie import *

Form, Window = uic.loadUiType("registration.ui")  #открытие формы с регистрацией

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()


def click_reg(): #что происходит по нажатию на кнопку: Зарегистрироваться
    file1 = open("Reg.txt", "w")
    file1.write(encrypt(form.login.displayText(), key, alfavitREG)) #Запись в файл зашифрованного логина
    file1.write('\n')
    file1.write(encrypt(form.password.displayText(), key, alfavitREG))#Запись в файл зашифрованного пароля
    file1.close()
    global window2
    Form2, Window2 = uic.loadUiType("personalKab.ui") #открытие формы с Личным кабинетом
    window2 = Window2()
    form2 = Form2()
    form2.setupUi(window2)
    window2.show()
    window.close() #закрытие предыдущей формы
    form2.name_pk.setText(form.name.displayText())


    def click_encrypt(): #что происходит по нажатию на кнопку: зашифровать
        file2 = open("information.txt", "w")
        file2.write(encrypt(form2.plainTextEdit.toPlainText().lower(), key, alfavit)) #записть в файл зашифрованной информации
        file2.close()
        global window3
        Form3, Window3 = uic.loadUiType("decrypt_inf.ui") #открытие формы Личного кабинета с кнопкой Расшифровать
        window3 = Window3()
        form3 = Form3()
        form3.setupUi(window3)
        window3.show()
        window2.close() #закрытие предыдущей формы
        form3.name_pk2.setText(form.name.displayText())
        def click_decrypt(): #что происходит по нажатию на кнопку: расшифровать
            file3 = open("information.txt", "r") #считывание зашифрованной информации из файла
            data = file3.read()
            file3.close()
            form3.plainTextEdit.setPlainText(decrypt(data, key, alfavit)) #расшифровка информации и вывод ее на экран
        def click_exit(): #что происходит по нажатию на кнопку: выйти
            global window4
            Form4, Window4 = uic.loadUiType("exitWindow.ui") #открытие формы с выходом
            window4 = Window4()
            form4 = Form4()
            form4.setupUi(window4)
            window4.show()
            def exitPK():  #что происходит по нажатию на кнопку: выйти из личного кабинета
                window3.close() #закрытие формы с расшифровкой
                window4.close() #закрытие формы с выходом
                window.show()  #открытие формы с регистрацией
            def closeForm():  #что происходит по нажатию на кнопку: закрыть приложение
                window3.close()  #закрытие формы с расшифровкой
                window4.close()  #закрытие формы с выходом
            form4.close_form.clicked.connect(closeForm) #нажатие на кнопку закрыть приложение
            form4.exit_pk.clicked.connect(exitPK) #нажатие на кнопку выйти из личного кабинета
        form3.exit.clicked.connect(click_exit) #нажатие на кнопку выйти
        form3.decrypt_pk.clicked.connect(click_decrypt) #нажатие на кнопку расшифровать

    form2.encrypt_pk.clicked.connect(click_encrypt) #нажатие на кнопку зашифровать


form.reg.clicked.connect(click_reg) # нажатие на кнопку Зарегистрироваться
app.exec_()



