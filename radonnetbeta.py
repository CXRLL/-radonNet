from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QPushButton, QTabWidget, QToolBar, QMenu, QMessageBox
from PySide6.QtWebEngineWidgets import QWebEngineView

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RadonNet 2.0 (Public Beta Release)")
        
        # Create central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Create layout for central widget
        layout = QVBoxLayout(central_widget)
        
        # Create address bar
        self.address_bar = QLineEdit()
        layout.addWidget(self.address_bar)
        
        # Create toolbar
        toolbar = QToolBar()
        self.addToolBar(toolbar)
        
        # Add navigation buttons to toolbar
        home_button = QPushButton("⌂")
        back_button = QPushButton("◄")
        forward_button = QPushButton("►")
        refresh_button = QPushButton("↺")
        toolbar.addWidget(home_button)
        toolbar.addWidget(back_button)
        toolbar.addWidget(forward_button)
        toolbar.addWidget(refresh_button)
        
        # Add add tab and remove tab buttons to toolbar
        add_tab_button = QPushButton("+")
        delete_tab_button = QPushButton("X")
        toolbar.addWidget(add_tab_button)
        toolbar.addWidget(delete_tab_button)
        
        # Add options menu
        options_menu = QMenu("Options", self)
        dark_mode_action = options_menu.addAction("Dark Mode")
        change_search_engine_menu = options_menu.addMenu("Change Default Search Engine")
        change_search_engine_menu.addAction("Google", self.change_search_engine_google)
        change_search_engine_menu.addAction("Bing", self.change_search_engine_bing)
        change_search_engine_menu.addAction("Yahoo", self.change_search_engine_yahoo)
        change_search_engine_menu.addAction("DuckDuckGo", self.change_search_engine_duckduckgo)
        options_button = QPushButton("Options")
        options_button.setMenu(options_menu)
        toolbar.addWidget(options_button)
        
        # Add extensions menu
        extensions_menu = QMenu("Extensions", self)
        qr_code_action = extensions_menu.addAction("QR Code Generator")
        qr_code_action.triggered.connect(self.open_qr_code_generator)
        extensions_button = QPushButton("Extensions")
        extensions_button.setMenu(extensions_menu)
        toolbar.addWidget(extensions_button)
        
        # Add tabs
        self.tabs = QTabWidget()
        layout.addWidget(self.tabs)
        
        # Add default tab with Google
        self.add_tab()
        self.load_url("https://www.google.com")
        
        # Connect button signals
        home_button.clicked.connect(self.go_home)
        back_button.clicked.connect(self.go_back)
        forward_button.clicked.connect(self.go_forward)
        refresh_button.clicked.connect(self.refresh)
        add_tab_button.clicked.connect(self.add_tab)
        delete_tab_button.clicked.connect(self.remove_tab)
        
    def add_tab(self):
        webview = QWebEngineView()
        self.tabs.addTab(webview, "New Tab")
        self.load_url("https://www.google.com", webview)
        
    def remove_tab(self):
        if self.tabs.count() > 1:
            self.tabs.removeTab(self.tabs.currentIndex())
        
    def load_url(self, url, webview=None):
        if not webview:
            webview = self.tabs.currentWidget()
        webview.load(url)
        
    def go_home(self):
        current_webview = self.tabs.currentWidget()
        current_webview.load("https://www.google.com")
        
    def go_back(self):
        current_webview = self.tabs.currentWidget()
        current_webview.back()
        
    def go_forward(self):
        current_webview = self.tabs.currentWidget()
        current_webview.forward()
        
    def refresh(self):
        current_webview = self.tabs.currentWidget()
        current_webview.reload()
        
    def change_search_engine_google(self):
        self.load_url("https://www.google.com")
        
    def change_search_engine_bing(self):
        self.load_url("https://www.bing.com")
        
    def change_search_engine_yahoo(self):
        self.load_url("https://www.yahoo.com")
        
    def change_search_engine_duckduckgo(self):
        self.load_url("https://www.duckduckgo.com")
        
    def open_qr_code_generator(self):
        QMessageBox.information(self, "Information", "QR Code Generator extension is not yet implemented.")

if __name__ == "__main__":
    app = QApplication([])
    window = Browser()
    window.show()
    app.exec()
