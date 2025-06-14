import sys
from PySide6.QtWidgets import QDialog, QMessageBox, QLineEdit
from PySide6.QtGui import QIcon
from ui.login_ui import Ui_LoginDialog
import sys  # Generated file
from main_window import MainWindow  # Import the main window class

class LoginWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LoginDialog()
        self.ui.setupUi(self)
        import os
        current_dir = os.path.dirname(os.path.abspath(__file__))
        styles_path = os.path.join(current_dir, 'static', 'styles.qss')
        with open(styles_path, 'r') as f:
            self.setStyleSheet(f.read())
        
        # Set window properties
        self.setWindowTitle("Loan System - Login")
        self.setWindowIcon(QIcon("static/logo.png"))
        self.setFixedSize(400, 500)
        
        # Connect signals
        self.ui.show_password_check.stateChanged.connect(self.toggle_password)
        self.ui.login_button.clicked.connect(self.authenticate)
    
    def toggle_password(self, state):
        """Toggle password visibility"""
        if state:
            self.ui.password_input.setEchoMode(QLineEdit.Normal)
        else:
            self.ui.password_input.setEchoMode(QLineEdit.Password)
    
    def authenticate(self):
        """Validate credentials"""
        username = self.ui.username_input.text()
        password = self.ui.password_input.text()

       
        # Replace with real database check later
        if username == "admin" and password == "admin123":
            QMessageBox.information(self, "Success", "Login successful!")
            self.accept()  # Close dialog on success
            self.main_window = MainWindow()
            self.main_window.show()
            self.close()  # Close login window
        else:
            QMessageBox.warning(self, "Error", "Invalid credentials")
        

if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())

    