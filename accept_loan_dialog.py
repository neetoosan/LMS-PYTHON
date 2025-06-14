from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtCore import Slot
from ui.accept_loan_dialog_ui import Ui_AcceptLoanDialog
from database.session import get_db
from database.models import Loan


class AcceptLoanDialog(QDialog):
    def __init__(self, loan_data=None, parent=None):
        super().__init__(parent)
        self.ui = Ui_AcceptLoanDialog()
        self.ui.setupUi(self)

        if loan_data:
            self._populate_fields(loan_data)

        # Connect signals
        self.ui.approve_btn.clicked.connect(self._approve_loan)
        self.ui.reject_btn.clicked.connect(self._reject_loan)
        self.ui.cancel_btn.clicked.connect(self.reject)

    def _populate_fields(self, loan_data):
        """Fill fields with selected loan data"""
        self.ui.member_id_input.setText(loan_data.get('member_id', ''))
        self.ui.name_input.setText(loan_data.get('name', ''))
        self.ui.amount_label.setText(f"${loan_data.get('amount', 0):,.2f}")

    @Slot()
    def _approve_loan(self):
        """Handle approve button click"""
        member_id = self.ui.member_id_input.text().strip()
        batch_no = self.ui.batch_input.text().strip()
        cheque_no = self.ui.cheque_input.text().strip()

        if not batch_no:
            QMessageBox.warning(self, "Input Error", "Batch number is required.")
            return
        if not cheque_no:
            QMessageBox.warning(self, "Input Error", "Cheque number is required.")
            return

        try:
            db = next(get_db())
            loan = db.query(Loan).filter(Loan.member_id == member_id).first()
            if not loan:
                raise ValueError(f"No loan found for ID {member_id}")

            # Update loan details
            loan.status = 'Approved'
            loan.batch_number = batch_no
            loan.cheque_number = cheque_no
            loan.approval_date = self.ui.date_input.date().toPython()

            # Optional: update guarantor info if present
            guarantor_name = self.ui.guarantor_input.text().strip() if hasattr(self.ui, 'guarantor_input') else ""
            guarantor_phone = self.ui.guarantor_phone_input.text().strip() if hasattr(self.ui, 'guarantor_phone_input') else ""
            if guarantor_name:
                loan.guarantor = guarantor_name
            if guarantor_phone:
                loan.guarantor_phone = guarantor_phone

            db.commit()
            QMessageBox.information(self, "Success", "Loan approved successfully!")
            self.accept()

        except Exception as e:
            db.rollback()
            QMessageBox.critical(self, "Database Error", f"Failed to approve loan:\n{str(e)}")
            self.reject()

    @Slot()
    def _reject_loan(self):
        """Handle reject button click"""
        confirm = QMessageBox.question(
            self,
            "Confirm Rejection",
            "Are you sure you want to reject this loan?",
            QMessageBox.Yes | QMessageBox.No
        )
        if confirm == QMessageBox.Yes:
            self._update_status('Rejected')

    def _update_status(self, status):
        """Helper to update loan status"""
        member_id = self.ui.member_id_input.text().strip()
        try:
            db = next(get_db())
            loan = db.query(Loan).filter(Loan.member_id == member_id).first()
            if not loan:
                raise ValueError(f"No loan found for member ID {member_id}")

            loan.status = status
            db.commit()
            QMessageBox.information(self, "Updated", f"Loan {status.lower()}!")
            self.accept()

        except Exception as e:
            db.rollback()
            QMessageBox.critical(self, "Database Error", f"Failed to update loan:\n{str(e)}")
            self.reject()