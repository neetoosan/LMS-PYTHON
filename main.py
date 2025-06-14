# main.py
from PySide6.QtWidgets import QApplication
from login import LoginWindow
from database.session import init_db, engine
from database.models import Base

# Create all tables if not exist
Base.metadata.create_all(engine)

if __name__ == "__main__":
    import sys
    init_db()  # Create tables if not exists

    app = QApplication(sys.argv)
    login = LoginWindow()
    login.show()
    sys.exit(app.exec())
