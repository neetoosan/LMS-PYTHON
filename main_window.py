from PySide6.QtWidgets import (
    QMainWindow, QTableWidgetItem, QTableView, QDialog, QVBoxLayout
)
from PySide6.QtCharts import QChart, QChartView, QBarSeries, QBarSet, QValueAxis, QCategoryAxis, QPieSeries
from PySide6.QtCore import Qt
from sqlalchemy import extract
from datetime import datetime
from ui.main_window_ui import Ui_MainWindow
from loan_dialog import LoanDialog
from member_dialog import MemberDialog
from contribution_dialog import ContributionDialog
from accept_loan_dialog import AcceptLoanDialog
from database.session import get_db
from database.models import Loan
from export_report_dialog import ExportReportDialog
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Window setup
        self.setWindowTitle("Loan Manager v1.0")
        self.setMinimumSize(800, 600)

        # Initialize components
        self._setup_tables()
        self._connect_signals()
        self._setup_charts()  # Add this to initialize charts on startup

        # Load initial data
        self._refresh_loans_table()
        self._update_system_summary()

    def _setup_tables(self):
        """Configure table columns"""
        self.ui.loans_table.setColumnCount(9)  # Increased from 5 to 9
        self.ui.loans_table.setHorizontalHeaderLabels([
            "Type", "IPPIS NO", "Name", "Amount", "Status", "Due Date", "Guarantor", "Guarantor Phone", "Batch Number"
        ])
        self.ui.loans_table.setSelectionBehavior(QTableView.SelectRows)

    def _connect_signals(self):
        """Connect buttons and menu actions to functions"""
        self.ui.add_loan_btn.clicked.connect(self._add_loan)
        self.ui.approve_loan_btn.clicked.connect(self._open_accept_loan_dialog)
        self.ui.actionLogout.triggered.connect(self._logout)
        self.ui.actionExit.triggered.connect(self.close)
        self.ui.generate_report_btn.clicked.connect(self._open_export_dialog)

        # Tools menu
        self.ui.actionManageMembers.triggered.connect(self._open_member_dialog)
        self.ui.add_contribution_btn.clicked.connect(self._open_contribution_dialog)

    def _add_loan(self):
        """Open loan creation dialog"""
        dialog = LoanDialog(self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            self._refresh_loans_table()
            self._update_system_summary()

    def _refresh_loans_table(self):
        """Reload loans from database and populate table"""
        db = next(get_db())
        loans = db.query(Loan).all()

        self.ui.loans_table.setRowCount(len(loans))
        for row, loan in enumerate(loans):
            self.ui.loans_table.setItem(row, 0, QTableWidgetItem("Member" if loan.is_member else "Non-Member"))
            self.ui.loans_table.setItem(row, 1, QTableWidgetItem(str(loan.member_id)))
            self.ui.loans_table.setItem(row, 2, QTableWidgetItem(loan.name))
            self.ui.loans_table.setItem(row, 3, QTableWidgetItem(f"${loan.amount:,.2f}"))
            self.ui.loans_table.setItem(row, 4, QTableWidgetItem(loan.status or "Pending"))
            self.ui.loans_table.setItem(row, 5, QTableWidgetItem(str(loan.due_date) if loan.due_date else ""))
            self.ui.loans_table.setItem(row, 6, QTableWidgetItem(loan.guarantor or ""))
            self.ui.loans_table.setItem(row, 7, QTableWidgetItem(loan.guarantor_phone or ""))
            self.ui.loans_table.setItem(row, 8, QTableWidgetItem(loan.batch_number or ""))

    def _update_system_summary(self):
        """Fetch latest stats from database and update labels"""
        db = next(get_db())
        try:
            active_loans = db.query(Loan).filter(Loan.status == 'Approved').count()
            overdue_loans = db.query(Loan).filter(Loan.status == 'Overdue').count()
            total_contributions = 0  # Replace with real query later

            self.ui.active_loans_label.setText(f"Active Loans: {active_loans}")
            self.ui.overdue_label.setText(f"Overdue Payments: {overdue_loans}")
            self.ui.total_contributions_label.setText(f"Total Contributions: ${total_contributions:,.2f}")

        except Exception as e:
            from PySide6.QtWidgets import QMessageBox
            QMessageBox.critical(self, "Database Error", f"Failed to load summary data:\n{str(e)}")

    def _logout(self):
        """Close current window and show login again"""
        self.close()
        from login import LoginWindow
        login = LoginWindow()
        login.show()
        login.exec()

    def _open_member_dialog(self):
        """Open member management dialog"""
        dialog = MemberDialog(self)
        dialog.exec()

    def _open_contribution_dialog(self):
        """Open contribution management dialog"""
        dialog = ContributionDialog(self)
        dialog.exec()

    def _open_accept_loan_dialog(self):
        """Open dialog to accept selected loan"""
        selected_row = self.ui.loans_table.currentRow()
        if selected_row < 0:
            from PySide6.QtWidgets import QMessageBox
            QMessageBox.warning(self, "Selection Required", "Please select a loan to approve.")
            return

        try:
            member_id = self.ui.loans_table.item(selected_row, 1).text()
            name = self.ui.loans_table.item(selected_row, 2).text()
            amount = float(self.ui.loans_table.item(selected_row, 3).text()[1:].replace(',', ''))  # Remove $ and ,

            loan_data = {
                'member_id': member_id,
                'name': name,
                'amount': amount
            }

            dialog = AcceptLoanDialog(loan_data, self)
            if dialog.exec() == dialog.DialogCode.Accepted:
                self._refresh_loans_table()
                self._update_system_summary()

        except (AttributeError, IndexError, ValueError) as e:
            from PySide6.QtWidgets import QMessageBox
            QMessageBox.critical(self, "Data Error", "Failed to retrieve loan data.\n\nDetails: " + str(e))

    def _open_export_dialog(self):
        """Open dialog to export reports"""
        dialog = ExportReportDialog(self)
        dialog.exec()

    def _setup_charts(self):
        """Initialize Matplotlib charts in the dashboard"""
        self._setup_loan_chart()
        self._setup_contribution_chart()

    def _setup_loan_chart(self):
        """Create a bar chart showing approved vs pending loans"""
        fig = Figure(figsize=(4, 3))
        ax = fig.add_subplot(111)
        
        db = next(get_db())
        current_month = datetime.now().month
        loans = db.query(Loan).filter(extract('month', Loan.approval_date) == current_month).all()

        approved_count = len([l for l in loans if l.status == 'Approved'])
        pending_count = len([l for l in loans if l.status != 'Approved'])

        if approved_count + pending_count == 0:
            ax.text(0.5, 0.5, "No Loans This Month", ha='center', va='center', fontsize=12, color='gray')
        else:
            ax.bar(["Approved", "Pending"], [approved_count, pending_count], color=["#4CAF50", "#F44336"])
            ax.set_ylabel("Number of Loans")
            ax.set_title("Monthly Loan Analysis")
            ax.grid(True)

        canvas = FigureCanvas(fig)
        layout = self.ui.loan_chart_layout  # Should be a QVBoxLayout in your UI
        if layout.count() > 0:
            layout.itemAt(0).widget().deleteLater()  # Remove previous chart
        layout.addWidget(canvas)

    def _setup_contribution_chart(self):
        """Create a pie chart for contribution summary"""
        fig, ax = plt.subplots(figsize=(4, 3))

        from database.models import Contribution
        db = next(get_db())
        contributions = db.query(Contribution).all()
        total_amount = sum(c.amount for c in contributions)
        count = len(contributions)

        # Handle case where there is no data
        if total_amount == 0 and count == 0:
            ax.text(0.5, 0.5, "No Contributions", ha='center', va='center', fontsize=12, color='gray')
            ax.axis('off')  # Hide axes
        else:
            labels = ["Total Amount", "Total Contributions"]
            sizes = [total_amount, count]
            colors = ['#FF9800', '#FFC107']
            ax.pie(
                sizes,
                labels=labels,
                autopct='%1.1f%%' if total_amount > 0 else '',
                startangle=90,
                colors=colors
            )
            ax.set_title("Contribution Summary")

        canvas = FigureCanvas(fig)
        layout = self.ui.contribution_chart_layout  # QVBoxLayout inside QWidget container
        if layout.count() > 0:
            layout.itemAt(0).widget().deleteLater()
        layout.addWidget(canvas)