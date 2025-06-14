# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCharts import QChartView
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QDateEdit, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 700)
        self.actionLogout = QAction(MainWindow)
        self.actionLogout.setObjectName(u"actionLogout")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionSettings = QAction(MainWindow)
        self.actionSettings.setObjectName(u"actionSettings")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionManageMembers = QAction(MainWindow)
        self.actionManageMembers.setObjectName(u"actionManageMembers")
        self.actionExportReport = QAction(MainWindow)
        self.actionExportReport.setObjectName(u"actionExportReport")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.main_tabs = QTabWidget(self.centralwidget)
        self.main_tabs.setObjectName(u"main_tabs")
        self.dashboard_tab = QWidget()
        self.dashboard_tab.setObjectName(u"dashboard_tab")
        self.verticalLayout_2 = QVBoxLayout(self.dashboard_tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.dashboard_tab)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.loans_chart = QChartView(self.frame)
        self.loans_chart.setObjectName(u"loans_chart")

        self.horizontalLayout.addWidget(self.loans_chart)

        self.contributions_chart = QChartView(self.frame)
        self.contributions_chart.setObjectName(u"contributions_chart")

        self.horizontalLayout.addWidget(self.contributions_chart)


        self.verticalLayout_2.addWidget(self.frame)

        self.contribution_chart_layout = QVBoxLayout()
        self.contribution_chart_layout.setObjectName(u"contribution_chart_layout")

        self.verticalLayout_2.addLayout(self.contribution_chart_layout)

        self.loan_chart_layout = QVBoxLayout()
        self.loan_chart_layout.setObjectName(u"loan_chart_layout")

        self.verticalLayout_2.addLayout(self.loan_chart_layout)

        self.summary_label = QLabel(self.dashboard_tab)
        self.summary_label.setObjectName(u"summary_label")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.summary_label.setFont(font)

        self.verticalLayout_2.addWidget(self.summary_label)

        self.frame_2 = QFrame(self.dashboard_tab)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.active_loans_label = QLabel(self.frame_2)
        self.active_loans_label.setObjectName(u"active_loans_label")

        self.horizontalLayout_2.addWidget(self.active_loans_label)

        self.total_contributions_label = QLabel(self.frame_2)
        self.total_contributions_label.setObjectName(u"total_contributions_label")

        self.horizontalLayout_2.addWidget(self.total_contributions_label)

        self.overdue_label = QLabel(self.frame_2)
        self.overdue_label.setObjectName(u"overdue_label")

        self.horizontalLayout_2.addWidget(self.overdue_label)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.main_tabs.addTab(self.dashboard_tab, "")
        self.loans_tab = QWidget()
        self.loans_tab.setObjectName(u"loans_tab")
        self.verticalLayout_3 = QVBoxLayout(self.loans_tab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_3 = QFrame(self.loans_tab)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.add_loan_btn = QPushButton(self.frame_3)
        self.add_loan_btn.setObjectName(u"add_loan_btn")

        self.horizontalLayout_3.addWidget(self.add_loan_btn)

        self.approve_loan_btn = QPushButton(self.frame_3)
        self.approve_loan_btn.setObjectName(u"approve_loan_btn")

        self.horizontalLayout_3.addWidget(self.approve_loan_btn)

        self.generate_report_btn = QPushButton(self.frame_3)
        self.generate_report_btn.setObjectName(u"generate_report_btn")

        self.horizontalLayout_3.addWidget(self.generate_report_btn)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.loans_table = QTableWidget(self.loans_tab)
        if (self.loans_table.columnCount() < 5):
            self.loans_table.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.loans_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.loans_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.loans_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.loans_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.loans_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.loans_table.setObjectName(u"loans_table")

        self.verticalLayout_3.addWidget(self.loans_table)

        self.main_tabs.addTab(self.loans_tab, "")
        self.contributions_tab = QWidget()
        self.contributions_tab.setObjectName(u"contributions_tab")
        self.verticalLayout_4 = QVBoxLayout(self.contributions_tab)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_4 = QFrame(self.contributions_tab)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.from_date_edit = QDateEdit(self.frame_4)
        self.from_date_edit.setObjectName(u"from_date_edit")

        self.horizontalLayout_4.addWidget(self.from_date_edit)

        self.to_date_edit = QDateEdit(self.frame_4)
        self.to_date_edit.setObjectName(u"to_date_edit")

        self.horizontalLayout_4.addWidget(self.to_date_edit)

        self.filter_contributions_btn = QPushButton(self.frame_4)
        self.filter_contributions_btn.setObjectName(u"filter_contributions_btn")

        self.horizontalLayout_4.addWidget(self.filter_contributions_btn)

        self.export_contributions_btn = QPushButton(self.frame_4)
        self.export_contributions_btn.setObjectName(u"export_contributions_btn")

        self.horizontalLayout_4.addWidget(self.export_contributions_btn)


        self.verticalLayout_4.addWidget(self.frame_4)

        self.contributions_table = QTableWidget(self.contributions_tab)
        if (self.contributions_table.columnCount() < 5):
            self.contributions_table.setColumnCount(5)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.contributions_table.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.contributions_table.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.contributions_table.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.contributions_table.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.contributions_table.setHorizontalHeaderItem(4, __qtablewidgetitem9)
        self.contributions_table.setObjectName(u"contributions_table")

        self.verticalLayout_4.addWidget(self.contributions_table)

        self.add_contribution_btn = QPushButton(self.contributions_tab)
        self.add_contribution_btn.setObjectName(u"add_contribution_btn")

        self.verticalLayout_4.addWidget(self.add_contribution_btn)

        self.main_tabs.addTab(self.contributions_tab, "")

        self.verticalLayout.addWidget(self.main_tabs)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuTools = QMenu(self.menubar)
        self.menuTools.setObjectName(u"menuTools")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionLogout)
        self.menuFile.addAction(self.actionExit)
        self.menuFile.addAction(self.actionExportReport)
        self.menuTools.addAction(self.actionManageMembers)
        self.menuTools.addAction(self.actionSettings)
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        self.main_tabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Loan and Contribution Management System", None))
        self.actionLogout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionSettings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionManageMembers.setText(QCoreApplication.translate("MainWindow", u"Manage Members", None))
        self.actionExportReport.setText(QCoreApplication.translate("MainWindow", u"Export Loan Report", None))
        self.summary_label.setText(QCoreApplication.translate("MainWindow", u"System Summary", None))
        self.active_loans_label.setText(QCoreApplication.translate("MainWindow", u"Active Loans: 0", None))
        self.total_contributions_label.setText(QCoreApplication.translate("MainWindow", u"Total Contributions: $0.00", None))
        self.overdue_label.setText(QCoreApplication.translate("MainWindow", u"Overdue Payments: 0", None))
        self.main_tabs.setTabText(self.main_tabs.indexOf(self.dashboard_tab), QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.add_loan_btn.setText(QCoreApplication.translate("MainWindow", u"Add New Loan", None))
        self.approve_loan_btn.setText(QCoreApplication.translate("MainWindow", u"Approve Loan", None))
        self.generate_report_btn.setText(QCoreApplication.translate("MainWindow", u"Generate Report", None))
        ___qtablewidgetitem = self.loans_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.loans_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Borrower", None));
        ___qtablewidgetitem2 = self.loans_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Amount", None));
        ___qtablewidgetitem3 = self.loans_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem4 = self.loans_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Due Date", None));
        self.main_tabs.setTabText(self.main_tabs.indexOf(self.loans_tab), QCoreApplication.translate("MainWindow", u"Loan Management", None))
        self.filter_contributions_btn.setText(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.export_contributions_btn.setText(QCoreApplication.translate("MainWindow", u"Export to Excel", None))
        ___qtablewidgetitem5 = self.contributions_table.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Contribution ID", None));
        ___qtablewidgetitem6 = self.contributions_table.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Member", None));
        ___qtablewidgetitem7 = self.contributions_table.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Amount", None));
        ___qtablewidgetitem8 = self.contributions_table.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem9 = self.contributions_table.horizontalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Interest", None));
        self.add_contribution_btn.setText(QCoreApplication.translate("MainWindow", u"Add Contribution", None))
        self.main_tabs.setTabText(self.main_tabs.indexOf(self.contributions_tab), QCoreApplication.translate("MainWindow", u"Contributions", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuTools.setTitle(QCoreApplication.translate("MainWindow", u"Tools", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

