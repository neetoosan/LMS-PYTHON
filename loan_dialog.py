# loan_dialog.py
from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtCore import Slot
from ui.loan_dialog_ui import Ui_LoanDialog
import math
from database.session import get_db
from database.models import Member, Loan
from datetime import datetime


class LoanDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_LoanDialog()
        self.ui.setupUi(self)

        # Set window title and initial behavior
        self.setWindowTitle("New Loan Application")
        self.setMinimumSize(400, 500)

        # Generate form number
        self._form_number = self._generate_form_number()
        self.ui.form_number_input.setText(self._form_number)

        # Connect signals
        self.ui.calculate_btn.clicked.connect(self.calculate_payment)
        self.ui.submit_btn.clicked.connect(self.submit_loan)
        self.ui.cancel_btn.clicked.connect(self.reject)
        self.ui.type_combo.currentIndexChanged.connect(self._on_type_changed)

        # Initialize fields
        self._on_type_changed(self.ui.type_combo.currentIndex())

        # Set placeholder texts for validation
        self.ui.name_input.setPlaceholderText("Required")
        self.ui.phone_input.setPlaceholderText("Required")
        self.ui.guarantor_input.setPlaceholderText("Required")

    def _generate_form_number(self):
        """Generate a unique form number like LN-2025-0001"""
        year = datetime.now().year
        db = next(get_db())
        count = db.query(Loan).count()
        return f"LN-{year}-{str(count + 1).zfill(4)}"

    def _generate_non_member_code(self):
        """Generate unique non-member code like NM-0001"""
        db = next(get_db())
        count = db.query(Loan).filter(Loan.member_id.like("NM-%")).count()
        return f"NM-{str(count + 1).zfill(4)}"

    def _on_type_changed(self, index):
        """Toggle input fields based on user type"""
        is_member = index == 0
        self.ui.member_id_input.setEnabled(is_member)
        self.ui.name_input.setEnabled(not is_member)
        self.ui.phone_input.setEnabled(not is_member)

        if is_member:
            self.ui.name_input.clear()
            self.ui.phone_input.clear()

    @Slot()
    def calculate_payment(self):
        """Calculate monthly payment using PMT formula"""
        try:
            amount = self.ui.amount_input.value()
            rate = self.ui.rate_input.value() / 100 / 12  # Monthly rate
            term = self.ui.term_input.value()
            payment = (amount * rate) / (1 - math.pow(1 + rate, -term))
            self.ui.payment_label.setText(f"${payment:,.2f}")
        except Exception as e:
            QMessageBox.warning(self, "Calculation Error", str(e))

    @Slot()
    def submit_loan(self):
        """Validate and submit loan application"""
        is_member = self.ui.type_combo.currentIndex() == 0
        name = self.ui.name_input.text().strip()
        phone = self.ui.phone_input.text().strip()
        guarantor = self.ui.guarantor_input.text().strip()
        guarantor_phone = self.ui.guarantor_phone_input.text().strip()

        if is_member:
            member_id = self.ui.member_id_input.text().strip()
            if not member_id:
                QMessageBox.warning(self, "Error", "Member ID is required")
                return

            db = next(get_db())
            member = db.query(Member).filter(Member.id == int(member_id)).first()
            if not member:
                QMessageBox.critical(self, "Database Error", "Member not found")
                return

            name = member.name
            phone = member.contact

        else:
            member_id = self._generate_non_member_code()
            if not name:
                QMessageBox.warning(self, "Error", "Full name is required")
                return
            if not phone:
                QMessageBox.warning(self, "Error", "Phone number is required")
                return

        if not guarantor:
            QMessageBox.warning(self, "Error", "Guarantor name is required")
            return

        # Save to DB
        db = next(get_db())
        try:
            loan = Loan(
                form_number=self._form_number,
                is_member=is_member,
                member_id=member_id,
                name=name,
                contact=phone,
                guarantor=guarantor,
                guarantor_phone=guarantor_phone,
                amount=self.ui.amount_input.value(),
                rate=self.ui.rate_input.value(),
                term=self.ui.term_input.value()
            )
            db.add(loan)
            db.commit()
            db.refresh(loan)

            QMessageBox.information(self, "Success", "Loan application submitted!")
            self.accept()

        except Exception as e:
            db.rollback()
            QMessageBox.critical(self, "Database Error", f"Failed to save loan:\n{str(e)}")