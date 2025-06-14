# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'contribution_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QDoubleSpinBox, QFormLayout, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_ContributionDialog(object):
    def setupUi(self, ContributionDialog):
        if not ContributionDialog.objectName():
            ContributionDialog.setObjectName(u"ContributionDialog")
        ContributionDialog.resize(400, 300)
        self.verticalLayout = QVBoxLayout(ContributionDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.titleLabel = QLabel(ContributionDialog)
        self.titleLabel.setObjectName(u"titleLabel")

        self.verticalLayout.addWidget(self.titleLabel)

        self.member_combo = QComboBox(ContributionDialog)
        self.member_combo.setObjectName(u"member_combo")
        self.member_combo.setEditable(False)

        self.verticalLayout.addWidget(self.member_combo)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_amount = QLabel(ContributionDialog)
        self.label_amount.setObjectName(u"label_amount")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_amount)

        self.amount_input = QDoubleSpinBox(ContributionDialog)
        self.amount_input.setObjectName(u"amount_input")
        self.amount_input.setMinimum(1.000000000000000)
        self.amount_input.setMaximum(100000.000000000000000)
        self.amount_input.setValue(50.000000000000000)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.amount_input)

        self.label_date = QLabel(ContributionDialog)
        self.label_date.setObjectName(u"label_date")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_date)

        self.date_input = QDateEdit(ContributionDialog)
        self.date_input.setObjectName(u"date_input")
        self.date_input.setCalendarPopup(True)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.date_input)

        self.label_interest = QLabel(ContributionDialog)
        self.label_interest.setObjectName(u"label_interest")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_interest)

        self.interest_input = QDoubleSpinBox(ContributionDialog)
        self.interest_input.setObjectName(u"interest_input")
        self.interest_input.setMinimum(0.000000000000000)
        self.interest_input.setMaximum(20.000000000000000)
        self.interest_input.setValue(0.000000000000000)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.interest_input)


        self.verticalLayout.addLayout(self.formLayout)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.horizontalSpacer = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonLayout.addItem(self.horizontalSpacer)

        self.save_btn = QPushButton(ContributionDialog)
        self.save_btn.setObjectName(u"save_btn")

        self.buttonLayout.addWidget(self.save_btn)

        self.cancel_btn = QPushButton(ContributionDialog)
        self.cancel_btn.setObjectName(u"cancel_btn")

        self.buttonLayout.addWidget(self.cancel_btn)


        self.verticalLayout.addLayout(self.buttonLayout)


        self.retranslateUi(ContributionDialog)

        QMetaObject.connectSlotsByName(ContributionDialog)
    # setupUi

    def retranslateUi(self, ContributionDialog):
        ContributionDialog.setWindowTitle(QCoreApplication.translate("ContributionDialog", u"Manage Contribution", None))
        self.titleLabel.setText(QCoreApplication.translate("ContributionDialog", u"Select Member and Enter Contribution Details", None))
        self.label_amount.setText(QCoreApplication.translate("ContributionDialog", u"Amount ($):", None))
        self.label_date.setText(QCoreApplication.translate("ContributionDialog", u"Date:", None))
        self.label_interest.setText(QCoreApplication.translate("ContributionDialog", u"Interest (%):", None))
        self.save_btn.setText(QCoreApplication.translate("ContributionDialog", u"Save", None))
        self.cancel_btn.setText(QCoreApplication.translate("ContributionDialog", u"Cancel", None))
    # retranslateUi

