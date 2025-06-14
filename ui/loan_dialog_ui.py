# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loan_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QDoubleSpinBox,
    QFormLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_LoanDialog(object):
    def setupUi(self, LoanDialog):
        if not LoanDialog.objectName():
            LoanDialog.setObjectName(u"LoanDialog")
        LoanDialog.resize(349, 527)
        self.verticalLayout = QVBoxLayout(LoanDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.borrower_group = QGroupBox(LoanDialog)
        self.borrower_group.setObjectName(u"borrower_group")
        self.formLayout = QFormLayout(self.borrower_group)
        self.formLayout.setObjectName(u"formLayout")
        self.label_type = QLabel(self.borrower_group)
        self.label_type.setObjectName(u"label_type")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_type)

        self.type_combo = QComboBox(self.borrower_group)
        self.type_combo.addItem("")
        self.type_combo.addItem("")
        self.type_combo.setObjectName(u"type_combo")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.type_combo)

        self.label_name = QLabel(self.borrower_group)
        self.label_name.setObjectName(u"label_name")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_name)

        self.name_input = QLineEdit(self.borrower_group)
        self.name_input.setObjectName(u"name_input")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.name_input)

        self.label_phone = QLabel(self.borrower_group)
        self.label_phone.setObjectName(u"label_phone")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label_phone)

        self.phone_input = QLineEdit(self.borrower_group)
        self.phone_input.setObjectName(u"phone_input")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.phone_input)

        self.label_guarantor = QLabel(self.borrower_group)
        self.label_guarantor.setObjectName(u"label_guarantor")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.label_guarantor)

        self.guarantor_input = QLineEdit(self.borrower_group)
        self.guarantor_input.setObjectName(u"guarantor_input")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.guarantor_input)

        self.label_guarantor_phone = QLabel(self.borrower_group)
        self.label_guarantor_phone.setObjectName(u"label_guarantor_phone")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.LabelRole, self.label_guarantor_phone)

        self.guarantor_phone_input = QLineEdit(self.borrower_group)
        self.guarantor_phone_input.setObjectName(u"guarantor_phone_input")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.FieldRole, self.guarantor_phone_input)

        self.label_form = QLabel(self.borrower_group)
        self.label_form.setObjectName(u"label_form")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.LabelRole, self.label_form)

        self.member_id_input = QLineEdit(self.borrower_group)
        self.member_id_input.setObjectName(u"member_id_input")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.member_id_input)

        self.label_ippis = QLabel(self.borrower_group)
        self.label_ippis.setObjectName(u"label_ippis")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_ippis)

        self.form_number_input = QLineEdit(self.borrower_group)
        self.form_number_input.setObjectName(u"form_number_input")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.form_number_input.sizePolicy().hasHeightForWidth())
        self.form_number_input.setSizePolicy(sizePolicy)
        self.form_number_input.setReadOnly(True)

        self.formLayout.setWidget(8, QFormLayout.ItemRole.FieldRole, self.form_number_input)


        self.verticalLayout.addWidget(self.borrower_group)

        self.loan_group = QGroupBox(LoanDialog)
        self.loan_group.setObjectName(u"loan_group")
        self.formLayout_2 = QFormLayout(self.loan_group)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_3 = QLabel(self.loan_group)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.amount_input = QDoubleSpinBox(self.loan_group)
        self.amount_input.setObjectName(u"amount_input")
        self.amount_input.setMinimum(100.000000000000000)
        self.amount_input.setMaximum(1000000.000000000000000)

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.amount_input)

        self.label_4 = QLabel(self.loan_group)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.rate_input = QDoubleSpinBox(self.loan_group)
        self.rate_input.setObjectName(u"rate_input")
        self.rate_input.setMinimum(1.000000000000000)
        self.rate_input.setMaximum(25.000000000000000)
        self.rate_input.setValue(5.000000000000000)

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.rate_input)

        self.label_5 = QLabel(self.loan_group)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_5)

        self.term_input = QSpinBox(self.loan_group)
        self.term_input.setObjectName(u"term_input")
        self.term_input.setMinimum(1)
        self.term_input.setMaximum(60)
        self.term_input.setValue(12)

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.FieldRole, self.term_input)


        self.verticalLayout.addWidget(self.loan_group)

        self.payment_group = QGroupBox(LoanDialog)
        self.payment_group.setObjectName(u"payment_group")
        self.formLayout_3 = QFormLayout(self.payment_group)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_6 = QLabel(self.payment_group)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_6)

        self.payment_label = QLabel(self.payment_group)
        self.payment_label.setObjectName(u"payment_label")

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.FieldRole, self.payment_label)


        self.verticalLayout.addWidget(self.payment_group)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.calculate_btn = QPushButton(LoanDialog)
        self.calculate_btn.setObjectName(u"calculate_btn")

        self.horizontalLayout.addWidget(self.calculate_btn)

        self.submit_btn = QPushButton(LoanDialog)
        self.submit_btn.setObjectName(u"submit_btn")

        self.horizontalLayout.addWidget(self.submit_btn)

        self.cancel_btn = QPushButton(LoanDialog)
        self.cancel_btn.setObjectName(u"cancel_btn")

        self.horizontalLayout.addWidget(self.cancel_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(LoanDialog)

        QMetaObject.connectSlotsByName(LoanDialog)
    # setupUi

    def retranslateUi(self, LoanDialog):
        LoanDialog.setWindowTitle(QCoreApplication.translate("LoanDialog", u"New Loan Application", None))
        self.borrower_group.setTitle(QCoreApplication.translate("LoanDialog", u"Borrower Information", None))
        self.label_type.setText(QCoreApplication.translate("LoanDialog", u"Type:", None))
        self.type_combo.setItemText(0, QCoreApplication.translate("LoanDialog", u"Member", None))
        self.type_combo.setItemText(1, QCoreApplication.translate("LoanDialog", u"Non-Member", None))

#if QT_CONFIG(tooltip)
        self.type_combo.setToolTip(QCoreApplication.translate("LoanDialog", u"Select if this is a member or new non-member", None))
#endif // QT_CONFIG(tooltip)
        self.label_name.setText(QCoreApplication.translate("LoanDialog", u"Full Name:", None))
        self.label_phone.setText(QCoreApplication.translate("LoanDialog", u"Phone Number:", None))
        self.label_guarantor.setText(QCoreApplication.translate("LoanDialog", u"Guarantor Name:", None))
        self.label_guarantor_phone.setText(QCoreApplication.translate("LoanDialog", u"Guarantor Phone:", None))
        self.label_form.setText(QCoreApplication.translate("LoanDialog", u"Form Number:", None))
        self.label_ippis.setText(QCoreApplication.translate("LoanDialog", u"IPPIS NO:", None))
        self.loan_group.setTitle(QCoreApplication.translate("LoanDialog", u"Loan Details", None))
        self.label_3.setText(QCoreApplication.translate("LoanDialog", u"Amount ($):", None))
        self.label_4.setText(QCoreApplication.translate("LoanDialog", u"Interest Rate (%):", None))
        self.label_5.setText(QCoreApplication.translate("LoanDialog", u"Term (months):", None))
        self.payment_group.setTitle(QCoreApplication.translate("LoanDialog", u"Payment Calculation", None))
        self.label_6.setText(QCoreApplication.translate("LoanDialog", u"Monthly Payment:", None))
        self.payment_label.setText(QCoreApplication.translate("LoanDialog", u"$0.00", None))
        self.calculate_btn.setText(QCoreApplication.translate("LoanDialog", u"Calculate", None))
        self.submit_btn.setText(QCoreApplication.translate("LoanDialog", u"Submit Application", None))
        self.cancel_btn.setText(QCoreApplication.translate("LoanDialog", u"Cancel", None))
    # retranslateUi

