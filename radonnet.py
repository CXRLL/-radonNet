import sys
from PySide6.QtCore import QUrl
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QToolBar
from PySide6.QtGui import QAction  # Corrected import for QAction
from PySide6.QtWebEngineWidgets import QWebEngineView

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('RadonNet')

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://www.google.com'))

        # Navigation toolbar
        self.nav_bar = QToolBar("Navigation")
        self.addToolBar(self.nav_bar)

        # Back button
        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        self.nav_bar.addAction(back_btn)

        # Forward button
        forward_btn = QAction('Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        self.nav_bar.addAction(forward_btn)

        # Refresh button
        refresh_btn = QAction('Refresh', self)
        refresh_btn.triggered.connect(self.browser.reload)
        self.nav_bar.addAction(refresh_btn)

        # Home button
        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        self.nav_bar.addAction(home_btn)

        # URL bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        self.nav_bar.addWidget(self.url_bar)

        self.setCentralWidget(self.browser)

    def navigate_home(self):
        self.browser.setUrl(QUrl('http://www.google.com'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    QApplication.setApplicationName('RadonNet')
    window = Browser()
    window.show()
    sys.exit(app.exec_())

