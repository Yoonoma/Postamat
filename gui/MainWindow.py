import sys
from datetime import datetime
from enum import Enum

from PyQt5 import QtWidgets
from PyQt5.QtCore import QTime, QTimer, Qt
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QShortcut, QTableWidgetItem, QMessageBox, QDialog, QLabel, QVBoxLayout
from loguru import logger
# import requests

from database import SQLiteDB
# from cells.cells_thread import CellsThread
from readers.reader_type import Reader
from resources.config import ADMIN_KEY, PWD_DB, database, ScannerState, Device
from .gui import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        ####################################
        ## Начальная настройка интерфейса ##
        ####################################
        # Инициализация UI
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()  # запуск интерфейса

        # Журнал 
        logger.add("debug.log", format="{time} {level} {message}", level="DEBUG", rotation="1 week")

        # Переход на домашний экран [по умолчанию]
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)

        # Отображение "часов" в ленте
        timer = QTimer(self)
        timer.timeout.connect(self._showTime)
        timer.start(1000)

        # Инициализация локальной база данных SQLite
        self.db = SQLiteDB(PWD_DB)
        self.init_tables(self.ui.table_user, "User")

        # Инициализация считывателей QR и RFID
        # self.qr_reader = Reader("thr-QR scanner ", Device.QR,
        #                         self.get_scanner_data)  # Сканер QR
        # self.rfid_reader = Reader("thr-RFID scanner", Device.RFID,
        #                           self.get_scanner_data)  # Сканер RFID

        # Статусы сканеров по умолчанию
        self.state_scanner_qr = ScannerState.user
        self.state_scanner_rfid = ScannerState.user

        # Слоты считывания данных
        self.ui.qr_data.textChanged[str].connect(self.scanner_hendler_qr)
        self.ui.rfid_data.textChanged[str].connect(self.scanner_hendler_rfid)

        # Слоты для добавления нового пользователя
        self.ui.new_key_rfid.textChanged[str].connect(self.new_rfid_key)
        self.ui.new_key_qr.textChanged[str].connect(self.new_qr_code_tag)

        # Настройка виртуальной клавиатуры
        self.input_password_admin = ''
        for n in range(0, 10):
            self.ui.list_virtual_keyboard_buttons[n].pressed.connect(
                lambda num=str(n): self.digit_virtual_keyboard(num))

        ####################################
        # Сигналы кнопок навигации         #
        ####################################
        self.ui.btn_home_admin.clicked.connect(self.swith_page_virtual_keyboard)
        self.ui.btn_keyboard_home.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_home))
        self.ui.btn_admin_home.clicked.connect(self.swith_page_home)
        self.ui.btn_admin_staff.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_admin_staff))
        self.ui.btn_admin_staff_cells.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_admin_cells))

        ####################################
        # Раздел администратора            #
        ####################################

        ## Виртуальная клавиатура
        # Кнопка "Clear All"
        self.ui.btn_keyboard_clear_all.clicked.connect(self.clear_all_virtual_keyboard)
        # Кнопка "Backspace"
        self.ui.btn_keyboard_backspace.clicked.connect(self.backspace_virtual_keyboard)
        # Проверка пароля на валидность
        self.ui.le_virtual_keyboard_input.textChanged[str].connect(
            lambda: self.check_password(self.input_password_admin, ADMIN_KEY))

        ## Работа с таблицей "Сотрудники"
        # Кнопка "Удалить ключ"
        self.ui.btn_tab_staff_delete_key.clicked.connect(self.delete_user)
        # Кнопка "Добавить новый ключ"
        self.ui.btn_tab_staff_add_new_key.clicked.connect(self.add_user)

        ####################################
        ## Тестирование
        # self.ui.stackedWidget.setCurrentWidget(self.ui.page_admin_staff)
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_virtual_keyboard)

        # Горячие клавиши завершения работы программы
        self.shortcut = QShortcut(QKeySequence("Ctrl+O"), self)
        self.shortcut.activated.connect(self.__del__)

        ####################################

    # Обработчик сканера RFID-метов
    def scanner_hendler_rfid(self):
        data = self.ui.rfid_data.text()
        logger.debug(f"RFID scanned the key [{data}] state - {self.state_scanner_rfid}")
        if not data:
            return

        if self.state_scanner_rfid == ScannerState.new_user:
            self.ui.new_key_rfid.setText(data)
            self.ui.rfid_data.clear()
            return

        if self.state_scanner_rfid == ScannerState.admin:
            self.ui.rfid_data.clear()
            return

        if self.state_scanner_rfid == ScannerState.expectation:  # Если режим сканера переведен в режим ожидания
            self.ui.rfid_data.clear()
            return

        if self.state_scanner_rfid == ScannerState.user:  # Если режим сканера переведен в режим пользователя
            # Защита от повторного сканирования QR-кодов и RFID-меток
            self.switch_scanners_on_standby()  # Перевод сканеров в режим ожидания
            if self.db.key_verification("id_rfid", data):  # Если rfid метка авторизована в системе
                if self.db.is_taken_tag("id_rfid", data):  # Если метка изъята
                    # Модель диалогового окна
                    msg_reply = self.show_dialog("Уведомление",
                                                 "Метка изъята.\nВернуть метку в шкаф?",
                                                 QMessageBox.Information,
                                                 [("Да", QMessageBox.ActionRole), ("Отмена", QMessageBox.NoRole)])

                    btn_msg_yes = msg_reply.buttons()[0]  # Кнопка "Да" модели диалогового окна
                    msg_reply.exec_()
                    if msg_reply.clickedButton() == btn_msg_yes:  # Если пользователь нажал "вернуть метку"
                        self.user_returned_tag("id_rfid", data)
                else:
                    self.user_taken_tag("id_rfid", data)

            else:  # Не удалось инициализировать rfid метку
                self.show_message("Ошибка", "RFID-метка не найдена или повреждена.\nОбратитесь к администратору.",
                                  timer_seconds=5)

            self.switch_scanners_to_user_mode()  # Перевод сканеров в режим пользователя
        self.ui.rfid_data.clear()

    # Обработчик сканера QR-кодов
    def scanner_hendler_qr(self):
        data = self.ui.qr_data.text()
        logger.debug(f"QR scanned the key [{data}] state - {self.state_scanner_qr}")
        if not data:
            return

        if self.state_scanner_qr == ScannerState.expectation:
            self.ui.qr_data.clear()
            return

        if self.state_scanner_qr == ScannerState.admin:
            self.ui.qr_data.clear()
            return

        if self.state_scanner_qr == ScannerState.new_user:
            self.ui.new_key_qr.setText(data)
            self.ui.qr_data.clear()
            return

        if self.state_scanner_qr == ScannerState.user:
            # Защита от повторного сканирования QR-кодов и RFID-меток
            self.switch_scanners_on_standby()  # Перевод сканеров в режим ожидания

            if data[len(database["QR_PREFIX"])] == "QR_PREFIX":  # елси qr-код включает в себя префикс для id-сотрудника
                # алгоритм с rfid
                pass
            elif self.db.key_verification("id_qr", data):  # Если qr-код авторизована в системе как id-tag
                if self.db.is_taken_tag("id_qr", data):  # Если метка изъята
                    self.user_returned_tag("id_qr", data)
            else:
                self.show_message("Ошибка", "QR-код не найден.\nОбратитесь к администратору.",
                                  timer_seconds=5)

            self.switch_scanners_to_user_mode()  # Перевод сканеров в режим пользователя

        self.ui.qr_data.clear()

    # Обработка логики [вернуть метку]
    def user_returned_tag(self, id_type_scanner: str, data: str) -> None:
        # cell_number = None
        # cells.open_cell(cell_number)
        id_tag = self.db.get_id_tag(id_type_scanner, data)
        log = f"Метку №{id_tag} вернули в шкаф | с помощью  {id_type_scanner} " \
              f"| время: [{datetime.fromtimestamp(1576280665)}]"
        logger.info(log)
        self.ui.list_log.addItem(log)

        self.db.returned_tag(id_type_scanner, data)
        self.update_table(self.ui.table_user, "User")
        ## Запрос на сервер
        # url = f"/api/external/tags/{id_tag}/assign"
        # response = requests.post(url)
        self.show_message("Уведомление", f"Положите метку в ячейку №{1}", timer_seconds=5)

    # Обработка логики [взять метку]
    def user_taken_tag(self, id_type_scanner, data):
        # cell_number = None
        # cells.open_cell(cell_number)
        id_tag = self.db.get_id_tag(id_type_scanner, data)
        log = f"Метку №{id_tag} взяли в шкаф | с помощью  {id_type_scanner} " \
              f"| время: [{datetime.fromtimestamp(1576280665)}]"
        logger.info(log)
        self.ui.list_log.addItem(log)

        self.db.taken_tag(id_type_scanner, data)
        self.update_table(self.ui.table_user, "User")
        ## Запрос на сервер
        # url = f"/api/external/tags/{id_tag}/assign"
        # response = requests.post(url)
        self.show_message("Уведомление", f"Возьмите метку из ячейки №{1}",  # .format(cell number)
                          timer_seconds=5)

    # Перевод сканеров в режим ожидания
    def switch_scanners_on_standby(self):
        self.state_scanner_qr = ScannerState.expectation
        self.state_scanner_rfid = ScannerState.expectation

    # Перевод сканеров в режим пользователя
    def switch_scanners_to_user_mode(self):
        self.state_scanner_qr = ScannerState.user
        self.state_scanner_rfid = ScannerState.user

    # Получение данных из QR-сканера и RFID-сканера
    def get_scanner_data(self, scan_data: str, type_scanner: Enum):
        if type_scanner == Device.QR:
            self.ui.qr_data.setText(scan_data)
        if type_scanner == Device.RFID:
            self.ui.rfid_data.setText(scan_data)

    # Переключение на страницу виртуальной клавиатуры для авторизации на страницу администратора
    def swith_page_virtual_keyboard(self) -> None:
        self.input_password_admin = ''
        self.ui.le_virtual_keyboard_input.clear()
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_virtual_keyboard)

    # Переключение на домашнюю страницу
    def swith_page_home(self) -> None:
        self.state_scanner_rfid = ScannerState.user
        self.state_scanner_qr = ScannerState.user
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)

    # Ввод пароля с вирт. клавиатуры
    def digit_virtual_keyboard(self, num: str) -> None:
        self.input_password_admin += num
        self.ui.le_virtual_keyboard_input.setText(self.input_password_admin)

    # Обработчик кнопки "backspace"
    def backspace_virtual_keyboard(self) -> None:
        self.input_password_admin = self.input_password_admin[:-1]
        self.ui.le_virtual_keyboard_input.setText(self.input_password_admin)

    # Обработчик кнопки "Clear All"
    def clear_all_virtual_keyboard(self) -> None:
        self.input_password_admin = ''
        self.ui.le_virtual_keyboard_input.clear()

    # Проверка пароля на валидность
    def check_password(self, input_key: str, password: str) -> None:
        if len(ADMIN_KEY) == len(input_key):
            if input_key == password:
                self.input_password_admin = ''
                self.ui.le_virtual_keyboard_input.clear()
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_admin_cells)
                logger.debug("Launch is admin panel.")
                self.state_scanner_qr = ScannerState.admin
                self.state_scanner_rfid = ScannerState.admin

    # Виджет часов, показывающий время с часами, минутами и секундами
    def _showTime(self) -> None:
        current_time = QTime.currentTime()
        label_time = current_time.toString('hh:mm:ss')
        self.ui.lbl_board_time.setText(label_time + "         ")

    # Инициализация таблицы ключей + меток (id метки, RFID ключ, QR-Code ключ)
    def init_tables(self, table: QtWidgets.QTableWidget, name_table: str) -> None:
        column_count = len(self.db.get_column_names(name_table)) - 1  # (-id)
        table.setColumnCount(column_count)  # Количество колонок

        # Заголовки таблицы Сотрудники
        table.setHorizontalHeaderLabels(database[f"header_{name_table}"])

        # Выравнивание заголовков - по центру
        for i in range(column_count):
            table.horizontalHeaderItem(i).setTextAlignment(Qt.AlignHCenter)

        self.update_table(table, name_table)

    # Обновляет данные в таблице
    def update_table(self, table: QtWidgets.QTableWidget, name_table: str) -> None:
        data_table = self.db.get_data_table(name_table)  # Данные таблицы из БД
        table.setRowCount(self.db.get_count_row(name_table))  # Количество строк

        row = 0
        for record in data_table:
            record = record[1:]  # [1:] убирает primary key в таблице
            for i in range(len(record)):
                table.setItem(row, i, QTableWidgetItem(str(record[i])))
            row += 1

    # Добавляет нового пользователя в систему
    def add_user(self):

        self.state_scanner_qr = ScannerState.new_user
        self.state_scanner_rfid = ScannerState.new_user

        # Модель диалогового окна [подтверждение действия]
        self.msg_add_user = self.show_dialog("Новый сотрудник",
                                             "Отсканируйте сначала RFID-код метку, после QR-код метки.",
                                             QMessageBox.Information,
                                             [("Отмена", QMessageBox.ActionRole)])
        btn_msg_cancel = self.msg_add_user.buttons()[0]  # Кнопка "Отмена" диалогового окна [подтверждение действия]
        self.msg_add_user.exec_()

        if self.msg_add_user.clickedButton() == btn_msg_cancel:
            self.switch_scanners_admin()
            return

    def new_rfid_key(self):
        if not self.ui.new_key_rfid.text():
            return
        self.show_message("Новый сотрудник", "Карта RFID отсканирована.\nОтсканируйте QR-код метки.", 5)

    # Доделать
    def new_qr_code_tag(self):
        rfid = self.ui.new_key_rfid.text()
        qr_key_tag = self.ui.new_key_qr.text()
        if not rfid or not qr_key_tag:  # Если RFID-код не считан
            self.switch_scanners_admin()
            return

        # Проверка на наличие ключей в БД
        if self.db.key_verification("key_tag", qr_key_tag):
            self.show_message("Ошибка", "Операция прервана. Данная метка уже существует.", 5)
            self.switch_scanners_admin()
            return

        if self.db.key_verification("id_rfid", rfid):
            self.show_message("Ошибка", "Операция прервана. Данная карта уже существует.", 5)
            self.switch_scanners_admin()
            return

        self.db.new_user(qr_key_tag, rfid)

        self.update_table(self.ui.table_user, "User")
        self.ui.new_key_qr.clear()
        self.ui.new_key_rfid.clear()
        self.switch_scanners_admin()
        self.msg_add_user.close()
        self.show_message("Новый сотрудник", "Успешно. Новый сотрудник создан и добавлен в базу данных.", 4)

    # Перевод сканеров в режим администратора
    def switch_scanners_admin(self):
        self.state_scanner_qr = ScannerState.admin
        self.state_scanner_rfid = ScannerState.admin

    # Удаляет пользователя из системы
    def delete_user(self):
        table_user = "User"
        self.delete_record_table(table_user, self.ui.table_user.currentIndex().row(), self.ui.table_user)
        self.update_table(self.ui.table_user, table_user)

    # Удаляет запись из таблицы
    def delete_record_table(self, name_table: str, selected_row: int, table: QtWidgets.QTableWidget) -> None:
        # Если администратор не выбрал запись в таблице
        if selected_row == -1:
            # Модель диалогового окна [ошибка]
            msg_warning = self.show_dialog(
                "Ошибка!",
                "\nВыберите строку для удаления данных о сотрудниках.",
                QMessageBox.Warning,
                [("ОК", QMessageBox.NoRole)]
            )
            msg_warning.exec_()
            return

        selected_sql_table_tag = table.item(selected_row, 1).text()  # ID метки
        selected_sql_table_rfid = (table.item(selected_row, 2).text())  # Ключ RFID

        # Модель диалогового окна [подтверждение действия]
        msg_reply_text = f"Вы действительно хотите удалить:\nID метки - [{selected_sql_table_tag}] | " \
                         f"RFID-Код - [{selected_sql_table_rfid}] ?"

        msg_reply = self.show_dialog("Уведомление", msg_reply_text, QMessageBox.Question,
                                     [("Да", QMessageBox.ActionRole),
                                      ("Отмена", QMessageBox.NoRole)])
        msg_reply.exec_()

        if msg_reply.clickedButton() == msg_reply.buttons()[0]:
            self.db.delete_record_where(name_table, condition="AND",
                                        key_tag=selected_sql_table_tag,
                                        id_RFID=selected_sql_table_rfid)
            logger.debug(f"Delete key_tag - [{selected_sql_table_tag}] | RFID-code - [{selected_sql_table_rfid}]")

    def show_dialog(self, title: str, text: str, icon: QMessageBox.Icon,
                    btns: list[(str, QMessageBox.ButtonRole)]) -> QMessageBox:
        msg = QMessageBox(self)
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.setFont(self.ui.font_btn_dialog)
        msg.setIcon(icon)
        QTimer.singleShot(60 * 1000, msg.close)  # Через 60 секунд QTimer вызовет mesg.close()

        for text_btn, role in btns:
            btn = msg.addButton(text_btn, role)
            btn.setFixedSize(120, 50)
        return msg

    def show_message(self, title: str, text: str, timer_seconds: int) -> None:
        msg = QDialog(self)
        msg.setWindowTitle(title)

        # Текст
        lbl = QLabel(msg)
        lbl.setText(text)
        lbl.setAlignment(Qt.AlignCenter)
        lbl.setStyleSheet("font-size: 20px")

        # Сетка
        layout = QVBoxLayout(msg)
        layout.addWidget(lbl)
        layout.addWidget(lbl)

        msg.resize(480, 360)  # размер окна
        QTimer.singleShot(timer_seconds * 1000, msg.close)  # Через timer_seconds секунд QTimer вызовет mesg.close()
        msg.exec_()

    def __del__(self) -> None:
        del self.qr_reader  # завершает работу считывателя QR кодов
        del self.rfid_reader  # завершает работу считывателя RFID меток
        self.db.close()  # закрывает соединение с базой данных SQLite
        super(QtWidgets.QMainWindow, self).close()  # завершает работу UI интерфейса
        logger.info("Application is closed.")


# Запуск приложения
def application():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
