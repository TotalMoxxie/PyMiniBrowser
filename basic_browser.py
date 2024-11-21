import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl



class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My First Browser yay")
        self.setGeometry(100, 100, 1024, 768)  # Window size

        # Create a layout for the browser
        layout = QVBoxLayout()
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Web view (browser)
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com")) # Default page
        layout.addWidget(self.browser)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Browser()
    window.show()
    sys.exit(app.exec_())
