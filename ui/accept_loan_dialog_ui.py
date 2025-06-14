# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'accept_loan_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QDialog, QFormLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_AcceptLoanDialog(object):
    def setupUi(self, AcceptLoanDialog):
        if not AcceptLoanDialog.objectName():
            AcceptLoanDialog.setObjectName(u"AcceptLoanDialog")
        AcceptLoanDialog.resize(400, 500)
        self.verticalLayout = QVBoxLayout(AcceptLoanDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.loan_info_group = QGroupBox(AcceptLoanDialog)
        self.loan_info_group.setObjectName(u"loan_info_group")
        self.formLayout = QFormLayout(self.loan_info_group)
        self.formLayout.setObjectName(u"formLayout")
        self.label_ippis = QLabel(self.loan_info_group)
        self.label_ippis.setObjectName(u"label_ippis")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_ippis)

        self.member_id_input = QLineEdit(self.loan_info_group)
        self.member_id_input.setObjectName(u"member_id_input")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.member_id_input)

        self.label_name = QLabel(self.loan_info_group)
        self.label_name.setObjectName(u"label_name")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_name)

        self.name_input = QLineEdit(self.loan_info_group)
        self.name_input.setObjectName(u"name_input")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.name_input)

        self.label_amount = QLabel(self.loan_info_group)
        self.label_amount.setObjectName(u"label_amount")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_amount)

        self.amount_label = QLabel(self.loan_info_group)
        self.amount_label.setObjectName(u"amount_label")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.amount_label)

        self.label_batch = QLabel(self.loan_info_group)
        self.label_batch.setObjectName(u"label_batch")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_batch)

        self.batch_input = QLineEdit(self.loan_info_group)
        self.batch_input.setObjectName(u"batch_input")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.batch_input)

        self.label_cheque = QLabel(self.loan_info_group)
        self.label_cheque.setObjectName(u"label_cheque")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_cheque)

        self.cheque_input = QLineEdit(self.loan_info_group)
        self.cheque_input.setObjectName(u"cheque_input")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.cheque_input)


        self.verticalLayout.addWidget(self.loan_info_group)

        self.guarantor_group = QGroupBox(AcceptLoanDialog)
        self.guarantor_group.setObjectName(u"guarantor_group")
        self.formLayout_2 = QFormLayout(self.guarantor_group)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_guarantor = QLabel(self.guarantor_group)
        self.label_guarantor.setObjectName(u"label_guarantor")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_guarantor)

        self.guarantor_input = QLineEdit(self.guarantor_group)
        self.guarantor_input.setObjectName(u"guarantor_input")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.guarantor_input)

        self.label_guarantor_phone = QLabel(self.guarantor_group)
        self.label_guarantor_phone.setObjectName(u"label_guarantor_phone")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_guarantor_phone)

        self.guarantor_phone_input = QLineEdit(self.guarantor_group)
        self.guarantor_phone_input.setObjectName(u"guarantor_phone_input")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.guarantor_phone_input)


        self.verticalLayout.addWidget(self.guarantor_group)

        self.approval_details = QGroupBox(AcceptLoanDialog)
        self.approval_details.setObjectName(u"approval_details")
        self.formLayout_3 = QFormLayout(self.approval_details)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_date = QLabel(self.approval_details)
        self.label_date.setObjectName(u"label_date")

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_date)

        self.date_input = QDateEdit(self.approval_details)
        self.date_input.setObjectName(u"date_input")
        self.date_input.setCalendarPopup(True)

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.FieldRole, self.date_input)


        self.verticalLayout.addWidget(self.approval_details)

        self.button_layout = QHBoxLayout()
        self.button_layout.setObjectName(u"button_layout")
        self.horizontalSpacer = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.button_layout.addItem(self.horizontalSpacer)

        self.approve_btn = QPushButton(AcceptLoanDialog)
        self.approve_btn.setObjectName(u"approve_btn")

        self.button_layout.addWidget(self.approve_btn)

        self.reject_btn = QPushButton(AcceptLoanDialog)
        self.reject_btn.setObjectName(u"reject_btn")

        self.button_layout.addWidget(self.reject_btn)

        self.cancel_btn = QPushButton(AcceptLoanDialog)
        self.cancel_btn.setObjectName(u"cancel_btn")

        self.button_layout.addWidget(self.cancel_btn)


        self.verticalLayout.addLayout(self.button_layout)


        self.retranslateUi(AcceptLoanDialog)

        QMetaObject.connectSlotsByName(AcceptLoanDialog)
    # setupUi

    def retranslateUi(self, AcceptLoanDialog):
        AcceptLoanDialog.setWindowTitle(QCoreApplication.translate("AcceptLoanDialog", u"Approve Loan Application", None))
        self.loan_info_group.setTitle(QCoreApplication.translate("AcceptLoanDialog", u"Loan Information", None))
        self.label_ippis.setText(QCoreApplication.translate("AcceptLoanDialog", u"IPPIS NO:", None))
        self.label_name.setText(QCoreApplication.translate("AcceptLoanDialog", u"Borrower Name:", None))
        self.label_amount.setText(QCoreApplication.translate("AcceptLoanDialog", u"Amount ($):", None))
        self.amount_label.setText(QCoreApplication.translate("AcceptLoanDialog", u"$0.00", None))
        self.label_batch.setText(QCoreApplication.translate("AcceptLoanDialog", u"Batch Number:", None))
        self.label_cheque.setText(QCoreApplication.translate("AcceptLoanDialog", u"Cheque Number:", None))
        self.guarantor_group.setTitle(QCoreApplication.translate("AcceptLoanDialog", u"Guarantor Information", None))
        self.label_guarantor.setText(QCoreApplication.translate("AcceptLoanDialog", u"Guarantor Name:", None))
        self.label_guarantor_phone.setText(QCoreApplication.translate("AcceptLoanDialog", u"Guarantor Phone:", None))
        self.approval_details.setTitle(QCoreApplication.translate("AcceptLoanDialog", u"Approval Details", None))
        self.label_date.setText(QCoreApplication.translate("AcceptLoanDialog", u"Approval Date:", None))
        self.approve_btn.setText(QCoreApplication.translate("AcceptLoanDialog", u"Approve", None))
        self.reject_btn.setText(QCoreApplication.translate("AcceptLoanDialog", u"Reject", None))
        self.cancel_btn.setText(QCoreApplication.translate("AcceptLoanDialog", u"Cancel", None))
    # retranslateUi

