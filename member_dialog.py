from PySide6.QtWidgets import QDialog, QMessageBox, QTableView, QTableWidgetItem
from PySide6.QtCore import Qt, Slot
from ui.member_dialog_ui import Ui_MemberDialog
from database.models import Member
from database.session import get_db


class MemberDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MemberDialog()
        self.ui.setupUi(self)

        self._current_member_id = None

        self._setup_table()
        self._connect_signals()
        self._refresh_members_table()

    def _setup_table(self):
        """Configure members table"""
        self.ui.members_table.setColumnCount(3)
        self.ui.members_table.setHorizontalHeaderLabels(["IPPIS NO", "Name", "Contact"])
        self.ui.members_table.setSelectionBehavior(QTableView.SelectRows)
        self.ui.members_table.setEditTriggers(QTableView.NoEditTriggers)

    def _connect_signals(self):
        """Connect UI signals"""
        self.ui.search_input.textChanged.connect(self._search_members)
        self.ui.members_table.itemSelectionChanged.connect(self._load_selected_member)
        self.ui.save_btn.clicked.connect(self._save_member)
        self.ui.delete_btn.clicked.connect(self._delete_member)
        self.ui.close_btn.clicked.connect(self.reject)

    @Slot()
    def _refresh_members_table(self, search_term=""):
        """Reload members from database"""
        db = next(get_db())
        query = db.query(Member)

        if search_term:
            query = query.filter(
                Member.name.ilike(f"%{search_term}%") |
                Member.contact.ilike(f"%{search_term}%")
            )

        members = query.all()

        self.ui.members_table.setRowCount(len(members))
        for row, member in enumerate(members):
            self.ui.members_table.setItem(row, 0, QTableWidgetItem(str(member.id)))
            self.ui.members_table.setItem(row, 1, QTableWidgetItem(member.name))
            self.ui.members_table.setItem(row, 2, QTableWidgetItem(member.contact))

    @Slot()
    def _search_members(self):
        """Filter members based on search input"""
        search_term = self.ui.search_input.text()
        self._refresh_members_table(search_term)

    @Slot()
    def _load_selected_member(self):
        """Load selected member into edit form"""
        selected = self.ui.members_table.selectedItems()
        if not selected:
            return
        member_id = int(selected[0].text())
        db = next(get_db())
        member = db.query(Member).get(member_id)
        if member:
            self._current_member_id = member_id
            self.ui.name_input.setText(member.name)
            self.ui.phone_input.setText(member.contact)
            self.ui.address_input.setPlainText(member.address or "")

    @Slot()
    def _save_member(self):
        """Save new or existing member"""
        name = self.ui.name_input.text().strip()
        phone = self.ui.phone_input.text().strip()
        address = self.ui.address_input.toPlainText().strip()

        if not name:
            QMessageBox.warning(self, "Error", "Name is required")
            return

        db = next(get_db())

        if self._current_member_id:
            # Update existing member
            member = db.query(Member).get(self._current_member_id)
            member.name = name
            member.contact = phone
            member.address = address
        else:
            # Create new member
            member = Member(name=name, contact=phone, address=address)
            db.add(member)

        db.commit()
        self._refresh_members_table()
        self._clear_form()
        QMessageBox.information(self, "Success", "Member saved successfully")

    @Slot()
    def _delete_member(self):
        """Delete selected member"""
        if not self._current_member_id:
            return

        confirm = QMessageBox.question(
            self,
            "Confirm Delete",
            "Delete this member permanently?",
            QMessageBox.Yes | QMessageBox.No
        )
        if confirm == QMessageBox.Yes:
            db = next(get_db())
            member = db.query(Member).get(self._current_member_id)
            db.delete(member)
            db.commit()
            self._refresh_members_table()
            self._clear_form()

    def _clear_form(self):
        """Reset the edit form"""
        self._current_member_id = None
        self.ui.name_input.clear()
        self.ui.phone_input.clear()
        self.ui.address_input.clear()