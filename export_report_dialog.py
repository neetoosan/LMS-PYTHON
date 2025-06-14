# export_report_dialog.py
from PySide6.QtWidgets import QDialog, QMessageBox, QFileDialog, QComboBox
from PySide6.QtCore import Slot
from ui.export_report_dialog_ui import Ui_ExportReportDialog
from database.session import get_db
from database.models import Loan


class ExportReportDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ExportReportDialog()
        self.ui.setupUi(self)

        # Load both members and non-members
        self._load_borrowers()

        # Connect signals
        self.ui.export_btn.clicked.connect(self._export_report)
        self.ui.cancel_btn.clicked.connect(self.reject)

    def _load_borrowers(self):
        """Load all borrowers with loans"""
        db = next(get_db())
        loans = db.query(Loan).all()
        self.ui.member_combo.clear()

        seen = set()
        for loan in loans:
            display_name = f"{loan.name} ({'Member' if loan.is_member else 'Non-Member'})"
            if display_name not in seen:
                self.ui.member_combo.addItem(display_name, userData=loan.member_id)
                seen.add(display_name)

        if not seen:
            self.ui.member_combo.addItem("No borrowers found", userData=None)

    @Slot()
    def _export_report(self):
        """Handle export button click"""
        selected_index = self.ui.member_combo.currentIndex()
        if selected_index < 0:
            QMessageBox.warning(self, "Selection Required", "Please select a borrower.")
            return

        member_id = self.ui.member_combo.itemData(selected_index)
        if not member_id or str(member_id) == "None":
            QMessageBox.critical(self, "Error", "Invalid borrower selection")
            return

        try:
            db = next(get_db())
            loans = db.query(Loan).filter(Loan.member_id == str(member_id)).all()
            if not loans:
                QMessageBox.information(self, "No Data", "No loans found for this borrower.")
                return

            file_format = "pdf" if self.ui.pdf_radio.isChecked() else "xlsx"
            file_path, _ = QFileDialog.getSaveFileName(
                self,
                f"Save Report As {file_format.upper()}",
                f"{loans[0].name}_{file_format}.{file_format}",
                f"{file_format.upper()} Files (*.{file_format});;All Files (*)"
            )
            if not file_path:
                return

            if file_format == "pdf":
                self._generate_pdf(file_path, loans)
            elif file_format == "xlsx":
                self._generate_excel(file_path, loans)

            QMessageBox.information(self, "Success", f"Report exported to:\n{file_path}")
            self.accept()

        except Exception as e:
            QMessageBox.critical(self, "Export Error", f"Failed to generate report:\n{str(e)}")

    def _generate_pdf(self, file_path, loans):
        """Generate PDF report using reportlab"""
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
        from reportlab.lib.styles import getSampleStyleSheet

        doc = SimpleDocTemplate(file_path)
        styles = getSampleStyleSheet()
        elements = []

        title = Paragraph(f"Loan Report - {loans[0].name}", styles['Title'])
        elements.append(title)
        elements.append(Spacer(1, 24))

        data = [
            ["Form No", "Status", "Amount", "Rate", "Term", "Due Date", "Batch", "Cheque No", "Approval Date", "Guarantor", "Guarantor Phone"]
        ]

        for loan in loans:
            data.append([
                loan.form_number or "",
                loan.status or "",
                f"${loan.amount:,.2f}" if loan.amount else "",
                f"{loan.rate:.2f}%" if loan.rate else "",
                f"{loan.term} months" if loan.term else "",
                str(loan.due_date) if loan.due_date else "",
                loan.batch_number or "",
                loan.cheque_number or "",
                str(loan.approval_date) if loan.approval_date else "",
                loan.guarantor or "",
                loan.guarantor_phone or ""
            ])

        table = Table(data)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), '#cccccc'),
            ('TEXTCOLOR', (0, 0), (-1, 0), '#000000'),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('GRID', (0, 0), (-1, -1), 1, '#000000')
        ]))

        elements.append(table)
        doc.build(elements)

    def _generate_excel(self, file_path, loans):
        """Generate Excel report using openpyxl"""
        from openpyxl import Workbook

        wb = Workbook()
        ws = wb.active
        ws.title = "Loan History"

        headers = ["Form No", "Status", "Amount", "Rate", "Term", "Due Date", "Batch", "Cheque No", "Approval Date", "Guarantor", "Guarantor Phone"]
        ws.append(headers)

        for loan in loans:
            ws.append([
                loan.form_number or "",
                loan.status or "",
                loan.amount or "",
                loan.rate or "",
                loan.term or "",
                str(loan.due_date) if loan.due_date else "",
                loan.batch_number or "",
                loan.cheque_number or "",
                str(loan.approval_date) if loan.approval_date else "",
                loan.guarantor or "",
                loan.guarantor_phone or ""
            ])

        wb.save(file_path)