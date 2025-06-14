# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'export_report_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGroupBox,
    QHBoxLayout, QLabel, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_ExportReportDialog(object):
    def setupUi(self, ExportReportDialog):
        if not ExportReportDialog.objectName():
            ExportReportDialog.setObjectName(u"ExportReportDialog")
        ExportReportDialog.resize(400, 550)
        self.verticalLayout = QVBoxLayout(ExportReportDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.instruction_label = QLabel(ExportReportDialog)
        self.instruction_label.setObjectName(u"instruction_label")

        self.verticalLayout.addWidget(self.instruction_label)

        self.label_select = QLabel(ExportReportDialog)
        self.label_select.setObjectName(u"label_select")

        self.verticalLayout.addWidget(self.label_select)

        self.member_combo = QComboBox(ExportReportDialog)
        self.member_combo.setObjectName(u"member_combo")

        self.verticalLayout.addWidget(self.member_combo)

        self.format_group = QGroupBox(ExportReportDialog)
        self.format_group.setObjectName(u"format_group")
        self.horizontalLayout = QHBoxLayout(self.format_group)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pdf_radio = QRadioButton(self.format_group)
        self.pdf_radio.setObjectName(u"pdf_radio")
        self.pdf_radio.setChecked(True)

        self.horizontalLayout.addWidget(self.pdf_radio)

        self.excel_radio = QRadioButton(self.format_group)
        self.excel_radio.setObjectName(u"excel_radio")

        self.horizontalLayout.addWidget(self.excel_radio)


        self.verticalLayout.addWidget(self.format_group)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.horizontalSpacer = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.buttonLayout.addItem(self.horizontalSpacer)

        self.export_btn = QPushButton(ExportReportDialog)
        self.export_btn.setObjectName(u"export_btn")

        self.buttonLayout.addWidget(self.export_btn)

        self.cancel_btn = QPushButton(ExportReportDialog)
        self.cancel_btn.setObjectName(u"cancel_btn")

        self.buttonLayout.addWidget(self.cancel_btn)


        self.verticalLayout.addLayout(self.buttonLayout)


        self.retranslateUi(ExportReportDialog)

        QMetaObject.connectSlotsByName(ExportReportDialog)
    # setupUi

    def retranslateUi(self, ExportReportDialog):
        ExportReportDialog.setWindowTitle(QCoreApplication.translate("ExportReportDialog", u"Export Loan Report", None))
        self.instruction_label.setText(QCoreApplication.translate("ExportReportDialog", u"Select a member and choose export format:", None))
        self.label_select.setText(QCoreApplication.translate("ExportReportDialog", u"Select Borrower:", None))
#if QT_CONFIG(tooltip)
        self.member_combo.setToolTip(QCoreApplication.translate("ExportReportDialog", u"Select member or non-member to export report", None))
#endif // QT_CONFIG(tooltip)
        self.format_group.setTitle(QCoreApplication.translate("ExportReportDialog", u"Export Format", None))
        self.pdf_radio.setText(QCoreApplication.translate("ExportReportDialog", u"PDF", None))
        self.excel_radio.setText(QCoreApplication.translate("ExportReportDialog", u"Excel (.xlsx)", None))
        self.export_btn.setText(QCoreApplication.translate("ExportReportDialog", u"Export", None))
        self.cancel_btn.setText(QCoreApplication.translate("ExportReportDialog", u"Cancel", None))
    # retranslateUi

