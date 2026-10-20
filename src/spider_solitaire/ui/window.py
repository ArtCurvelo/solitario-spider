
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QWidget,
    QVBoxLayout,
)
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Solitário Spider")
        self.resize(1200, 800)
        self.setMinimumSize(900, 600)

        self.setStyleSheet("""
            QMainWindow {
                background-color: #123b2a;
            }

            QLabel {
                color: #ffffff;
                font-size: 28px;
                font-weight: bold;
            }
        """)

        container = QWidget()
        layout = QVBoxLayout(container)

        titulo = QLabel("SOLITÁRIO SPIDER")
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addStretch()
        layout.addWidget(titulo)
        layout.addStretch()

        self.setCentralWidget(container)


def create_application():
    app = QApplication.instance() or QApplication([])
    window = MainWindow()
    window.show()
    return app, window
