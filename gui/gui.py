from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QHeaderView, QAbstractItemView, QScrollArea, QLabel, QFrame, QLineEdit

from resources.config import cupboard


class Ui_MainWindow(object):
    def __init__(self):
        self.list_cell_buttons = []
        self.list_virtual_keyboard_buttons = []

        self.font_btn_dialog = QtGui.QFont()
        self.font_btn_dialog.setPointSize(20)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Postamat")
        MainWindow.resize(cupboard["window_width"], cupboard["window_height"])
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))

        font_btn = QtGui.QFont()
        font_btn.setPointSize(20)

        font_virtual_keyboard_num = QtGui.QFont()
        font_virtual_keyboard_num.setPointSize(18)

        font_virtual_keyboard_action = QtGui.QFont()
        font_virtual_keyboard_action.setPointSize(16)

        font_btn_cells = QtGui.QFont()
        font_btn_cells.setPointSize(18)

        self.qr_data = QLineEdit()
        self.rfid_data = QLineEdit()

        self.new_key_qr = QLineEdit()
        self.new_key_rfid = QLineEdit()

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(30, 0, 30, 20)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_top_board = QtWidgets.QFrame(self.centralwidget)
        self.frame_top_board.setMinimumSize(QtCore.QSize(0, 70))
        self.frame_top_board.setStyleSheet("background-color: rgb(0, 102, 153);")
        self.frame_top_board.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_top_board.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_board.setObjectName("frame_top_board")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_top_board)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lbl_board_info = QtWidgets.QLabel(self.frame_top_board)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbl_board_info.setFont(font)
        self.lbl_board_info.setObjectName("lbl_board_info")
        self.horizontalLayout_2.addWidget(self.lbl_board_info)
        self.lbl_board_time = QtWidgets.QLabel(self.frame_top_board)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbl_board_time.setFont(font)
        self.lbl_board_time.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lbl_board_time.setTextFormat(QtCore.Qt.AutoText)
        self.lbl_board_time.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lbl_board_time.setObjectName("lbl_board_time")

        self.horizontalLayout_2.addWidget(self.lbl_board_time)

        self.verticalLayout.addWidget(self.frame_top_board)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")

        self.page_home = QtWidgets.QWidget()
        self.page_home.setObjectName("page_home")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page_home)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        self.lbl_home_info = QtWidgets.QLabel(self.page_home)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.lbl_home_info.setFont(font)
        self.lbl_home_info.setTextFormat(QtCore.Qt.AutoText)
        self.lbl_home_info.setScaledContents(False)
        self.lbl_home_info.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_home_info.setWordWrap(True)
        self.lbl_home_info.setIndent(-1)
        self.lbl_home_info.setObjectName("lbl_home_info")
        self.verticalLayout_4.addWidget(self.lbl_home_info)
        self.hlLayout_home_btn = QtWidgets.QHBoxLayout()
        self.hlLayout_home_btn.setObjectName("hlLayout_home_btn")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hlLayout_home_btn.addItem(spacerItem5)
        self.btn_home_admin = QtWidgets.QPushButton(self.page_home)
        self.btn_home_admin.setMinimumSize(QtCore.QSize(200, 80))
        self.btn_home_admin.setFont(font_btn)
        self.btn_home_admin.setObjectName("btn_home_admin")
        self.hlLayout_home_btn.addWidget(self.btn_home_admin)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hlLayout_home_btn.addItem(spacerItem6)
        self.verticalLayout_4.addLayout(self.hlLayout_home_btn)
        spacerItem7 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_4.addItem(spacerItem7)
        self.stackedWidget.addWidget(self.page_home)
        self.page_user = QtWidgets.QWidget()
        self.page_user.setObjectName("page_user")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page_user)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lbl_user_status = QtWidgets.QLabel(self.page_user)
        self.lbl_user_status.setMinimumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.lbl_user_status.setFont(font)
        self.lbl_user_status.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_user_status.setWordWrap(True)
        self.lbl_user_status.setObjectName("lbl_user_status")
        self.verticalLayout_5.addWidget(self.lbl_user_status)
        self.hLayout_user_btn = QtWidgets.QHBoxLayout()
        self.hLayout_user_btn.setObjectName("hLayout_user_btn")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hLayout_user_btn.addItem(spacerItem8)
        self.btn_user_close = QtWidgets.QPushButton(self.page_user)
        self.btn_user_close.setMinimumSize(QtCore.QSize(150, 75))
        self.btn_user_close.setFont(font_btn)
        self.btn_user_close.setObjectName("btn_user_close")
        self.hLayout_user_btn.addWidget(self.btn_user_close)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hLayout_user_btn.addItem(spacerItem9)
        self.verticalLayout_5.addLayout(self.hLayout_user_btn)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_5.addItem(spacerItem10)
        self.stackedWidget.addWidget(self.page_user)
        self.page_admin_cells = QtWidgets.QWidget()
        self.page_admin_cells.setObjectName("page_admin_cells")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page_admin_cells)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lbl_admin_info_1 = QtWidgets.QLabel(self.page_admin_cells)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_admin_info_1.sizePolicy().hasHeightForWidth())
        self.lbl_admin_info_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(38)
        self.lbl_admin_info_1.setFont(font)
        self.lbl_admin_info_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lbl_admin_info_1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lbl_admin_info_1.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_admin_info_1.setWordWrap(True)
        self.lbl_admin_info_1.setObjectName("lbl_admin_info_1")
        self.verticalLayout_2.addWidget(self.lbl_admin_info_1)
        self.hLayout_admin_btn = QtWidgets.QHBoxLayout()
        self.hLayout_admin_btn.setSpacing(8)
        self.hLayout_admin_btn.setObjectName("hLayout_admin_btn")
        self.hLayout_admin_btn.setContentsMargins(10, 0, 0, 0)
        self.hLayout_admin_btn.setSpacing(20)  # Растояние между кнопками

        self.btn_admin_home = QtWidgets.QPushButton(self.page_admin_cells)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_admin_home.sizePolicy().hasHeightForWidth())
        self.btn_admin_home.setSizePolicy(sizePolicy)
        self.btn_admin_home.setMinimumSize(QtCore.QSize(150, 60))
        self.btn_admin_home.setFont(font_btn)
        self.btn_admin_home.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.btn_admin_home.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_admin_home.setStyleSheet("background-color: rgb(111, 8, 37);")
        self.btn_admin_home.setObjectName("btn_admin_home")
        self.hLayout_admin_btn.addWidget(self.btn_admin_home)
        self.btn_admin_staff = QtWidgets.QPushButton(self.page_admin_cells)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_admin_staff.sizePolicy().hasHeightForWidth())
        self.btn_admin_staff.setSizePolicy(sizePolicy)
        self.btn_admin_staff.setMinimumSize(QtCore.QSize(150, 60))
        self.btn_admin_staff.setFont(font_btn)
        self.btn_admin_staff.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.btn_admin_staff.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_admin_staff.setStyleSheet("background-color: rgb(111, 8, 37);")
        self.btn_admin_staff.setObjectName("btn_admin_staff")
        self.hLayout_admin_btn.addWidget(self.btn_admin_staff)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hLayout_admin_btn.addItem(spacerItem11)
        self.verticalLayout_2.addLayout(self.hLayout_admin_btn)
        self.hLayout_admin_info_2 = QtWidgets.QHBoxLayout()
        self.hLayout_admin_info_2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.hLayout_admin_info_2.setObjectName("hLayout_admin_info_2")

        self.lbl_admin_inf2 = QtWidgets.QLabel(self.page_admin_cells)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_admin_inf2.sizePolicy().hasHeightForWidth())
        self.lbl_admin_inf2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lbl_admin_inf2.setFont(font)
        self.lbl_admin_inf2.setObjectName("lbl_admin_inf2")
        self.hLayout_admin_info_2.addWidget(self.lbl_admin_inf2)
        self.lbl_admin_inf3 = QtWidgets.QLabel(self.page_admin_cells)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_admin_inf3.sizePolicy().hasHeightForWidth())
        self.lbl_admin_inf3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.lbl_admin_inf3.setFont(font)
        self.lbl_admin_inf3.setFrameShape(QtWidgets.QFrame.HLine)
        self.lbl_admin_inf3.setLineWidth(2)
        self.lbl_admin_inf3.setText("")
        self.lbl_admin_inf3.setObjectName("lbl_admin_inf3")
        self.hLayout_admin_info_2.addWidget(self.lbl_admin_inf3)
        self.verticalLayout_2.addLayout(self.hLayout_admin_info_2)
        self.gridLayout_admin_btn_cells = QtWidgets.QGridLayout()
        self.gridLayout_admin_btn_cells.setObjectName("gridLayout_admin_btn_cells")
        self.gridLayout_admin_btn_cells.setContentsMargins(5, 5, 5, 10)
        self.btn_cell1 = QtWidgets.QPushButton(self.page_admin_cells)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cell1.sizePolicy().hasHeightForWidth())
        self.btn_cell1.setSizePolicy(sizePolicy)
        self.btn_cell1.setObjectName("btn_cell1")
        self.gridLayout_admin_btn_cells.addWidget(self.btn_cell1, 0, 0, 1, 1)
        self.btn_cell7 = QtWidgets.QPushButton(self.page_admin_cells)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cell7.sizePolicy().hasHeightForWidth())
        self.btn_cell7.setSizePolicy(sizePolicy)
        self.btn_cell7.setObjectName("btn_cell7")
        self.gridLayout_admin_btn_cells.addWidget(self.btn_cell7, 3, 1, 1, 1)
        self.btn_cell10 = QtWidgets.QPushButton(self.page_admin_cells)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cell10.sizePolicy().hasHeightForWidth())
        self.btn_cell10.setSizePolicy(sizePolicy)
        self.btn_cell10.setObjectName("btn_cell10")
        self.gridLayout_admin_btn_cells.addWidget(self.btn_cell10, 3, 2, 1, 1)
        self.btn_cell13 = QtWidgets.QPushButton(self.page_admin_cells)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cell13.sizePolicy().hasHeightForWidth())
        self.btn_cell13.setSizePolicy(sizePolicy)
        self.btn_cell13.setObjectName("btn_cell13")
        self.gridLayout_admin_btn_cells.addWidget(self.btn_cell13, 3, 3, 1, 1)
        self.btn_cell16 = QtWidgets.QPushButton(self.page_admin_cells)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cell16.sizePolicy().hasHeightForWidth())
        self.btn_cell16.setSizePolicy(sizePolicy)
        self.btn_cell16.setObjectName("btn_cell16")
        self.gridLayout_admin_btn_cells.addWidget(self.btn_cell16, 0, 4, 1, 1)
        self.btn_cell2 = QtWidgets.QPushButton(self.page_admin_cells)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cell2.sizePolicy().hasHeightForWidth())
        self.btn_cell2.setSizePolicy(sizePolicy)
        self.btn_cell2.setObjectName("btn_cell2")
        self.gridLayout_admin_btn_cells.addWidget(self.btn_cell2, 1, 0, 1, 1)

        self.btn_server_room = QtWidgets.QPushButton(self.page_admin_cells)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_server_room.sizePolicy().hasHeightForWidth())
        self.btn_server_room.setSizePolicy(sizePolicy)
        self.btn_server_room.setStyleSheet("background-color: rgb(8, 126, 139);")
        self.btn_server_room.setAutoRepeatInterval(100)
        self.btn_server_room.setObjectName("btn_server_room")
        self.gridLayout_admin_btn_cells.addWidget(self.btn_server_room, 0, 1, 3, 3)

        self.btn_cell17 = QtWidgets.QPushButton(self.page_admin_cells)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cell17.sizePolicy().hasHeightForWidth())
        self.btn_cell17.setSizePolicy(sizePolicy)
        self.btn_cell17.setObjectName("btn_cell17")
        self.gridLayout_admin_btn_cells.addWidget(self.btn_cell17, 1, 4, 1, 1)
        self.btn_cell3 = QtWidgets.QPushButton(self.page_admin_cells)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cell3.sizePolicy().hasHeightForWidth())
        self.btn_cell3.setSizePolicy(sizePolicy)
        self.btn_cell3.setObjectName("btn_cell3")
        self.gridLayout_admin_btn_cells.addWidget(self.btn_cell3, 2, 0, 1, 1)
        self.btn_cell18 = QtWidgets.QPushButton(self.page_admin_cells)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cell18.sizePolicy().hasHeightForWidth())
        self.btn_cell18.setSizePolicy(sizePolicy)
        self.btn_cell18.setObjectName("btn_cell18")
        self.gridLayout_admin_btn_cells.addWidget(self.btn_cell18, 2, 4, 1, 1)
        self.btn_cell4 = QtWidgets.QPushButton(self.page_admin_cells)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cell4.sizePolicy().hasHeightForWidth())
        self.btn_cell4.setSizePolicy(sizePolicy)
        self.btn_cell4.setObjectName("btn_cell4")
        self.gridLayout_admin_btn_cells.addWidget(self.btn_cell4, 3, 0, 1, 1)
        self.btn_cell19 = QtWidgets.QPushButton(self.page_admin_cells)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cell19.sizePolicy().hasHeightForWidth())
        self.btn_cell19.setSizePolicy(sizePolicy)
        self.btn_cell19.setObjectName("btn_cell19")
        self.gridLayout_admin_btn_cells.addWidget(self.btn_cell19, 3, 4, 1, 1)
        self.btn_cell5 = QtWidgets.QPushButton(self.page_admin_cells)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cell5.sizePolicy().hasHeightForWidth())
        self.btn_cell5.setSizePolicy(sizePolicy)
        self.btn_cell5.setObjectName("btn_cell5")
        self.gridLayout_admin_btn_cells.addWidget(self.btn_cell5, 4, 0, 1, 1)
        self.btn_cell8 = QtWidgets.QPushButton(self.page_admin_cells)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cell8.sizePolicy().hasHeightForWidth())
        self.btn_cell8.setSizePolicy(sizePolicy)
        self.btn_cell8.setObjectName("btn_cell8")
        self.gridLayout_admin_btn_cells.addWidget(self.btn_cell8, 4, 1, 1, 1)
        self.btn_cell11 = QtWidgets.QPushButton(self.page_admin_cells)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cell11.sizePolicy().hasHeightForWidth())
        self.btn_cell11.setSizePolicy(sizePolicy)
        self.btn_cell11.setObjectName("btn_cell11")
        self.gridLayout_admin_btn_cells.addWidget(self.btn_cell11, 4, 2, 1, 1)
        self.btn_cell14 = QtWidgets.QPushButton(self.page_admin_cells)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cell14.sizePolicy().hasHeightForWidth())
        self.btn_cell14.setSizePolicy(sizePolicy)
        self.btn_cell14.setObjectName("btn_cell14")
        self.gridLayout_admin_btn_cells.addWidget(self.btn_cell14, 4, 3, 1, 1)
        self.btn_cell20 = QtWidgets.QPushButton(self.page_admin_cells)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cell20.sizePolicy().hasHeightForWidth())
        self.btn_cell20.setSizePolicy(sizePolicy)
        self.btn_cell20.setObjectName("btn_cell20")
        self.gridLayout_admin_btn_cells.addWidget(self.btn_cell20, 4, 4, 1, 1)
        self.btn_cell6 = QtWidgets.QPushButton(self.page_admin_cells)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cell6.sizePolicy().hasHeightForWidth())
        self.btn_cell6.setSizePolicy(sizePolicy)
        self.btn_cell6.setObjectName("btn_cell6")
        self.gridLayout_admin_btn_cells.addWidget(self.btn_cell6, 5, 0, 1, 1)
        self.btn_cell9 = QtWidgets.QPushButton(self.page_admin_cells)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cell9.sizePolicy().hasHeightForWidth())
        self.btn_cell9.setSizePolicy(sizePolicy)
        self.btn_cell9.setObjectName("btn_cell9")
        self.gridLayout_admin_btn_cells.addWidget(self.btn_cell9, 5, 1, 1, 1)
        self.btn_cell12 = QtWidgets.QPushButton(self.page_admin_cells)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cell12.sizePolicy().hasHeightForWidth())
        self.btn_cell12.setSizePolicy(sizePolicy)
        self.btn_cell12.setObjectName("btn_cell12")
        self.gridLayout_admin_btn_cells.addWidget(self.btn_cell12, 5, 2, 1, 1)
        self.btn_cell15 = QtWidgets.QPushButton(self.page_admin_cells)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cell15.sizePolicy().hasHeightForWidth())
        self.btn_cell15.setSizePolicy(sizePolicy)
        self.btn_cell15.setObjectName("btn_cell15")
        self.gridLayout_admin_btn_cells.addWidget(self.btn_cell15, 5, 3, 1, 1)
        self.btn_cell21 = QtWidgets.QPushButton(self.page_admin_cells)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cell21.sizePolicy().hasHeightForWidth())
        self.btn_cell21.setSizePolicy(sizePolicy)
        self.btn_cell21.setObjectName("btn_cell21")
        self.gridLayout_admin_btn_cells.addWidget(self.btn_cell21, 5, 4, 1, 1)

        # Список кнопок для взаимодействия с ячейками
        self.list_cell_buttons.append(self.btn_server_room)
        for i in range(1, cupboard["count_cells"] + 1):
            self.list_cell_buttons.append(getattr(self, 'btn_cell%s' % i))

        for btn in self.list_cell_buttons:
            btn.setFont(font_btn_cells)

        self.verticalLayout_2.addLayout(self.gridLayout_admin_btn_cells)
        self.stackedWidget.addWidget(self.page_admin_cells)
        self.page_admin_staff = QtWidgets.QWidget()
        self.page_admin_staff.setObjectName("page_admin_staff")
        self.page_admin_staff.setContentsMargins(10,0,10,10)

        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page_admin_staff)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.verticalLayout_3.setSpacing(15)
        self.horizontalLayout.setObjectName("horizontalLayout")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_admin_staff_cells = QtWidgets.QPushButton(self.page_admin_staff)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_admin_staff_cells.sizePolicy().hasHeightForWidth())
        self.btn_admin_staff_cells.setSizePolicy(sizePolicy)
        self.btn_admin_staff_cells.setMinimumSize(QtCore.QSize(150, 60))

        self.btn_admin_staff_cells.setFont(font_btn)
        self.btn_admin_staff_cells.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.btn_admin_staff_cells.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_admin_staff_cells.setStyleSheet("background-color: rgb(111, 8, 37);")
        self.btn_admin_staff_cells.setObjectName("btn_admin_staff_cells")
        self.horizontalLayout.addWidget(self.btn_admin_staff_cells)
        spacerItem12 = QtWidgets.QSpacerItem(37, 57, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem12)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.tabWidget = QtWidgets.QTabWidget(self.page_admin_staff)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_staff = QtWidgets.QWidget()
        self.tab_staff.setObjectName("tab_staff")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_staff)

        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.table_user = QtWidgets.QTableWidget(self.tab_staff)
        self.table_user.setObjectName("table_user")
        self.table_user.resizeColumnsToContents()  # Размер столбцов по содержимому
        self.table_user.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # Растянуть таблицу на весь виджет
        self.table_user.setEditTriggers(QAbstractItemView.NoEditTriggers)  # Запрет на редактирование ячеек
        self.table_user.setStyleSheet("font-size: 20px;")  # Шрифт
        self.table_user.horizontalHeader().setDefaultSectionSize(60)  # ширина ячеек
        self.table_user.verticalHeader().setDefaultSectionSize(60)  # высота ячеек

        self.verticalLayout_6.addWidget(self.table_user)

        self.hLayout_tab_staff_btn = QtWidgets.QHBoxLayout()
        self.hLayout_tab_staff_btn.setObjectName("hLayout_tab_staff_btn")
        self.btn_tab_staff_add_new_key = QtWidgets.QPushButton(self.tab_staff)
        self.btn_tab_staff_add_new_key.setObjectName("btn_tab_staff_add_new_key")
        self.hLayout_tab_staff_btn.addWidget(self.btn_tab_staff_add_new_key)
        self.btn_tab_staff_add_new_key.setMinimumSize(50, 50)
        self.btn_tab_staff_add_new_key.setFont(font_btn)
        self.btn_tab_staff_delete_key = QtWidgets.QPushButton(self.tab_staff)

        self.btn_tab_staff_delete_key.setFont(font_btn)
        self.btn_tab_staff_delete_key.setObjectName("btn_tab_staff_delete_key")
        self.btn_tab_staff_delete_key.setMinimumSize(50, 50)
        self.hLayout_tab_staff_btn.addWidget(self.btn_tab_staff_delete_key)
        self.verticalLayout_6.addLayout(self.hLayout_tab_staff_btn)
        self.tabWidget.addTab(self.tab_staff, "")
        self.tab_log = QtWidgets.QWidget()
        self.tab_log.setObjectName("tab_log")
        self.tabWidget.addTab(self.tab_log, "")

        # Журнал [когда взял/положил метку]
        self.vLayout_tab_log = QtWidgets.QVBoxLayout(self.tab_log)
        self.vLayout_tab_log.setObjectName("vLayout_tab_log")

        self.list_log = QtWidgets.QListWidget(self.tab_log)

        self.vLayout_tab_log.addWidget(self.list_log)

        self.verticalLayout_3.addWidget(self.tabWidget)
        self.stackedWidget.addWidget(self.page_admin_staff)
        self.page_virtual_keyboard = QtWidgets.QWidget()
        self.page_virtual_keyboard.setObjectName("page_virtual_keyboard")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.page_virtual_keyboard)
        self.verticalLayout_8.setObjectName("verticalLayout_8")

        spacerItem13 = QtWidgets.QSpacerItem(619, 243, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_8.addItem(spacerItem13)

        self.Layout_keyboard_top = QtWidgets.QGridLayout()
        self.Layout_keyboard_top.setVerticalSpacing(36)
        self.Layout_keyboard_top.setObjectName("Layout_keyboard_top")
        self.lbl_vitrual_keyboard_info = QtWidgets.QLabel(self.page_virtual_keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_vitrual_keyboard_info.sizePolicy().hasHeightForWidth())
        self.lbl_vitrual_keyboard_info.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbl_vitrual_keyboard_info.setFont(font)
        self.lbl_vitrual_keyboard_info.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_vitrual_keyboard_info.setObjectName("lbl_vitrual_keyboard_info")
        self.Layout_keyboard_top.addWidget(self.lbl_vitrual_keyboard_info, 0, 0, 1, 3)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.Layout_keyboard_top.addItem(spacerItem14, 1, 0, 1, 1)
        self.btn_keyboard_home = QtWidgets.QPushButton(self.page_virtual_keyboard)
        self.btn_keyboard_home.setMinimumSize(QtCore.QSize(200, 80))

        self.btn_keyboard_home.setFont(font_btn)
        self.btn_keyboard_home.setObjectName("btn_keyboard_home")
        self.Layout_keyboard_top.addWidget(self.btn_keyboard_home, 1, 1, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.Layout_keyboard_top.addItem(spacerItem15, 1, 2, 1, 1)
        self.verticalLayout_8.addLayout(self.Layout_keyboard_top)
        spacerItem16 = QtWidgets.QSpacerItem(17, 243, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_8.addItem(spacerItem16)

        self.frame_keyboard = QtWidgets.QFrame(self.page_virtual_keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_keyboard.sizePolicy().hasHeightForWidth())
        self.frame_keyboard.setSizePolicy(sizePolicy)
        self.frame_keyboard.setStyleSheet("background-color: rgb(0, 102, 153);")
        self.frame_keyboard.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_keyboard.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_keyboard.setObjectName("frame_keyboard")

        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_keyboard)
        self.verticalLayout_7.setContentsMargins(-1, -1, -1, 30)
        self.verticalLayout_7.setSpacing(18)
        self.verticalLayout_7.setObjectName("verticalLayout_7")

        self.le_virtual_keyboard_input = QtWidgets.QLineEdit(self.frame_keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_virtual_keyboard_input.sizePolicy().hasHeightForWidth())
        self.le_virtual_keyboard_input.setSizePolicy(sizePolicy)

        font = QtGui.QFont()
        font.setPointSize(20)
        self.le_virtual_keyboard_input.setFont(font)

        self.le_virtual_keyboard_input.setMinimumSize(QtCore.QSize(0, 50))
        self.le_virtual_keyboard_input.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.le_virtual_keyboard_input.setObjectName("le_virtual_keyboard_input")
        self.le_virtual_keyboard_input.setReadOnly(True)
        self.verticalLayout_7.addWidget(self.le_virtual_keyboard_input)

        self.gridLayout_virtual_keyboard = QtWidgets.QGridLayout()
        self.gridLayout_virtual_keyboard.setObjectName("gridLayout_virtual_keyboard")

        ###
        ### Кнопки виртуальной клавиатуры
        ###

        ## Позиции в сетке
        row_grid = 0
        column_grid = 0
        for num in range(10):
            btn = QtWidgets.QPushButton(self.frame_keyboard)
            btn.setMinimumSize(QtCore.QSize(70, 70))
            btn.setFont(font_virtual_keyboard_num)
            btn.setObjectName(f"btn_virtual_keyboard_{num}")

            if num == 5:
                row_grid = 1
                column_grid = 0

            self.gridLayout_virtual_keyboard.addWidget(btn, row_grid, column_grid, 1, 1)
            column_grid += 1

            self.list_virtual_keyboard_buttons.append(btn)

        self.btn_keyboard_clear_all = QtWidgets.QPushButton(self.frame_keyboard)
        self.btn_keyboard_clear_all.setMinimumSize(QtCore.QSize(70, 70))
        self.btn_keyboard_clear_all.setFont(font_virtual_keyboard_action)
        self.btn_keyboard_clear_all.setObjectName("btn_keyboard_clear_all")
        self.gridLayout_virtual_keyboard.addWidget(self.btn_keyboard_clear_all, 1, 5, 1, 1)

        self.btn_keyboard_backspace = QtWidgets.QPushButton(self.frame_keyboard)
        self.btn_keyboard_backspace.setMinimumSize(QtCore.QSize(70, 70))
        self.btn_keyboard_backspace.setFont(font_virtual_keyboard_action)
        self.btn_keyboard_backspace.setObjectName("btn_keyboard_backspace")
        self.gridLayout_virtual_keyboard.addWidget(self.btn_keyboard_backspace, 0, 5, 1, 1)

        self.verticalLayout_7.addLayout(self.gridLayout_virtual_keyboard)
        self.verticalLayout_8.addWidget(self.frame_keyboard)
        self.stackedWidget.addWidget(self.page_virtual_keyboard)
        self.verticalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Postamat"))
        self.lbl_board_info.setText(_translate("MainWindow", "        TransNetIQ"))
        self.lbl_home_info.setText(
            _translate("MainWindow", "Приложите ключ-карту к считывателю или отсканируйте QR-код."))
        self.btn_home_admin.setText(_translate("MainWindow", "Админ"))
        self.lbl_user_status.setText(_translate("MainWindow", "?"))
        self.btn_user_close.setText(_translate("MainWindow", "Отмена"))
        self.lbl_admin_info_1.setText(_translate("MainWindow", "Для открытия ячейки нажмите на нужную кнопку."))
        self.btn_admin_home.setText(_translate("MainWindow", "На главную"))
        self.btn_admin_staff.setText(_translate("MainWindow", "Сотрудники"))
        self.lbl_admin_inf2.setText(_translate("MainWindow", "  Ячейки"))
        self.btn_cell1.setText(_translate("MainWindow", "Ячейка 1"))
        self.btn_cell7.setText(_translate("MainWindow", "Ячейка 7"))
        self.btn_cell10.setText(_translate("MainWindow", "Ячейка 10"))
        self.btn_cell13.setText(_translate("MainWindow", "Ячейка 13"))
        self.btn_cell16.setText(_translate("MainWindow", "Ячейка 16"))
        self.btn_cell2.setText(_translate("MainWindow", "Ячейка 2"))
        self.btn_server_room.setText(_translate("MainWindow", "Серверная"))
        self.btn_cell17.setText(_translate("MainWindow", "Ячейка 17"))
        self.btn_cell3.setText(_translate("MainWindow", "Ячейка 3"))
        self.btn_cell18.setText(_translate("MainWindow", "Ячейка 18"))
        self.btn_cell4.setText(_translate("MainWindow", "Ячейка 4"))
        self.btn_cell19.setText(_translate("MainWindow", "Ячейка 19"))
        self.btn_cell5.setText(_translate("MainWindow", "Ячейка 5"))
        self.btn_cell8.setText(_translate("MainWindow", "Ячейка 8"))
        self.btn_cell11.setText(_translate("MainWindow", "Ячейка 11"))
        self.btn_cell14.setText(_translate("MainWindow", "Ячейка 14"))
        self.btn_cell20.setText(_translate("MainWindow", "Ячейка 20"))
        self.btn_cell6.setText(_translate("MainWindow", "Ячейка 6"))
        self.btn_cell9.setText(_translate("MainWindow", "Ячейка 9"))
        self.btn_cell12.setText(_translate("MainWindow", "Ячейка 12"))
        self.btn_cell15.setText(_translate("MainWindow", "Ячейка 15"))
        self.btn_cell21.setText(_translate("MainWindow", "Ячейка 21"))
        self.btn_admin_staff_cells.setText(_translate("MainWindow", "Ячейки"))
        self.btn_tab_staff_add_new_key.setText(_translate("MainWindow", "Добавить новый ключ"))
        self.btn_tab_staff_delete_key.setText(_translate("MainWindow", "Удалить ключ"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_staff), _translate("MainWindow", "Сотрудники"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_log), _translate("MainWindow", "Журнал"))

        self.btn_keyboard_clear_all.setText(_translate("MainWindow", "Clear All"))
        self.btn_keyboard_backspace.setText(_translate("MainWindow", "Backspace"))
        self.lbl_vitrual_keyboard_info.setText(_translate("MainWindow", "Введите PIN-код администратора"))
        self.btn_keyboard_home.setText(_translate("MainWindow", "На главную"))

        for i in range(len(self.list_virtual_keyboard_buttons)):
            self.list_virtual_keyboard_buttons[i].setText(_translate("MainWindow", f"{i}"))
