# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_LoginDialog(object):
    def setupUi(self, LoginDialog):
        if not LoginDialog.objectName():
            LoginDialog.setObjectName(u"LoginDialog")
        LoginDialog.resize(400, 500)
        self.verticalLayout = QVBoxLayout(LoginDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.logo_label = QLabel(LoginDialog)
        self.logo_label.setObjectName(u"logo_label")
        self.logo_label.setPixmap(QPixmap(u"static/logo.png"))
        self.logo_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.logo_label)

        self.title_label = QLabel(LoginDialog)
        self.title_label.setObjectName(u"title_label")
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.title_label.setFont(font)
        self.title_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.title_label)

        self.username_input = QLineEdit(LoginDialog)
        self.username_input.setObjectName(u"username_input")

        self.verticalLayout.addWidget(self.username_input)

        self.password_input = QLineEdit(LoginDialog)
        self.password_input.setObjectName(u"password_input")
        self.password_input.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.password_input)

        self.show_password_check = QCheckBox(LoginDialog)
        self.show_password_check.setObjectName(u"show_password_check")

        self.verticalLayout.addWidget(self.show_password_check)

        self.login_button = QPushButton(LoginDialog)
        self.login_button.setObjectName(u"login_button")

        self.verticalLayout.addWidget(self.login_button)


        self.retranslateUi(LoginDialog)

        QMetaObject.connectSlotsByName(LoginDialog)
    # setupUi

    def retranslateUi(self, LoginDialog):
        self.title_label.setText(QCoreApplication.translate("LoginDialog", u"Login", None))
        self.username_input.setPlaceholderText(QCoreApplication.translate("LoginDialog", u"Username", None))
        self.password_input.setPlaceholderText(QCoreApplication.translate("LoginDialog", u"Password", None))
        self.show_password_check.setText(QCoreApplication.translate("LoginDialog", u"Show Password", None))
        self.login_button.setText(QCoreApplication.translate("LoginDialog", u"Login", None))
        pass
    # retranslateUi

