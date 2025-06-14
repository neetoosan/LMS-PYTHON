# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'member_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTabWidget, QTableWidget, QTableWidgetItem,
    QTextEdit, QVBoxLayout, QWidget)
class Ui_MemberDialog(object):
    def setupUi(self, MemberDialog):
        if not MemberDialog.objectName():
            MemberDialog.setObjectName(u"MemberDialog")
        MemberDialog.resize(500, 400)
        self.verticalLayout = QVBoxLayout(MemberDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(MemberDialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.search_tab = QWidget()
        self.search_tab.setObjectName(u"search_tab")
        self.verticalLayout_2 = QVBoxLayout(self.search_tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.search_input = QLineEdit(self.search_tab)
        self.search_input.setObjectName(u"search_input")

        self.verticalLayout_2.addWidget(self.search_input)

        self.members_table = QTableWidget(self.search_tab)
        if (self.members_table.columnCount() < 3):
            self.members_table.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.members_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.members_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.members_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.members_table.setObjectName(u"members_table")

        self.verticalLayout_2.addWidget(self.members_table)

        self.tabWidget.addTab(self.search_tab, "")
        self.edit_tab = QWidget()
        self.edit_tab.setObjectName(u"edit_tab")
        self.formLayout = QFormLayout(self.edit_tab)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.edit_tab)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.name_input = QLineEdit(self.edit_tab)
        self.name_input.setObjectName(u"name_input")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.name_input)

        self.label_2 = QLabel(self.edit_tab)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.phone_input = QLineEdit(self.edit_tab)
        self.phone_input.setObjectName(u"phone_input")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.phone_input)

        self.label_3 = QLabel(self.edit_tab)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.address_input = QTextEdit(self.edit_tab)
        self.address_input.setObjectName(u"address_input")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.address_input)

        self.tabWidget.addTab(self.edit_tab, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.save_btn = QPushButton(MemberDialog)
        self.save_btn.setObjectName(u"save_btn")

        self.horizontalLayout.addWidget(self.save_btn)

        self.delete_btn = QPushButton(MemberDialog)
        self.delete_btn.setObjectName(u"delete_btn")

        self.horizontalLayout.addWidget(self.delete_btn)

        self.close_btn = QPushButton(MemberDialog)
        self.close_btn.setObjectName(u"close_btn")

        self.horizontalLayout.addWidget(self.close_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(MemberDialog)

        QMetaObject.connectSlotsByName(MemberDialog)
    # setupUi

    def retranslateUi(self, MemberDialog):
        MemberDialog.setWindowTitle(QCoreApplication.translate("MemberDialog", u"Member Management", None))
        self.search_input.setPlaceholderText(QCoreApplication.translate("MemberDialog", u"Search by name or ID...", None))
        ___qtablewidgetitem = self.members_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MemberDialog", u"IPPIS NO", None));
        ___qtablewidgetitem1 = self.members_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MemberDialog", u"Name", None));
        ___qtablewidgetitem2 = self.members_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MemberDialog", u"Contact", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.search_tab), QCoreApplication.translate("MemberDialog", u"Search Members", None))
        self.label.setText(QCoreApplication.translate("MemberDialog", u"Full Name:", None))
        self.label_2.setText(QCoreApplication.translate("MemberDialog", u"Phone:", None))
        self.label_3.setText(QCoreApplication.translate("MemberDialog", u"Address:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.edit_tab), QCoreApplication.translate("MemberDialog", u"Add/Edit", None))
        self.save_btn.setText(QCoreApplication.translate("MemberDialog", u"Save", None))
        self.delete_btn.setText(QCoreApplication.translate("MemberDialog", u"Delete", None))
        self.close_btn.setText(QCoreApplication.translate("MemberDialog", u"Close", None))
    # retranslateUi

