# contribution_dialog.py

from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtCore import Slot
from ui.contribution_dialog_ui import Ui_ContributionDialog
from database.session import get_db
from database.models import Contribution, Member


def parse_currency(value: str) -> float:
    try:
        return float(value.replace(',', '').strip())
    except ValueError as e:
        raise ValueError(f"Invalid currency format: '{value}'") from e


class ContributionDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ContributionDialog()
        self.ui.setupUi(self)

        # Load members into combo box
        self._load_members()

        # Connect signals
        self.ui.save_btn.clicked.connect(self._save_contribution)
        self.ui.cancel_btn.clicked.connect(self.reject)

    def _load_members(self):
        """Load members into combo box"""
        db = next(get_db())
        members = db.query(Member).order_by(Member.name).all()
        self.ui.member_combo.clear()
        for member in members:
            self.ui.member_combo.addItem(f"{member.id} - {member.name}", userData=member.id)

    @Slot()
    def _save_contribution(self):
        """Collect input and validate before saving"""
        member_id = self.ui.member_combo.currentData()
        amount_str = self.ui.amount_input.text()
        date = self.ui.date_input.date().toPython()
        interest = self.ui.interest_input.value()

        if not member_id:
            QMessageBox.warning(self, "Error", "Please select a member")
            return

        try:
            amount = parse_currency(amount_str)
        except ValueError as e:
            QMessageBox.critical(self, "Input Error", str(e))
            return

        try:
            db = next(get_db())

            contribution = Contribution(
                member_id=member_id,
                amount=amount,
                date=date,
                interest=interest
            )
            db.add(contribution)
            db.commit()
            db.refresh(contribution)

            QMessageBox.information(self, "Success", "Contribution saved!")
            self.accept()

            # Return contribution data
            return {
                'id': contribution.id,
                'member_id': contribution.member_id,
                'member_name': contribution.member.name if contribution.member else "",
                'amount': f"${contribution.amount:,.2f}",
                'date': str(contribution.date),
                'interest': f"{contribution.interest:.2f}%"
            }

        except Exception as e:
            db.rollback()
            QMessageBox.critical(self, "Database Error", f"Failed to save contribution:\n{str(e)}")
            return None