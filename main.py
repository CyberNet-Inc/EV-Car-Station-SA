import sys
import folium
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTabWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QLineEdit, QPushButton, QMessageBox

API_URL = 'http://127.0.0.1:5000'  # Adjust this if your API has a different address

class EVChargerLocator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.token = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle('EV Charger Locator')
        self.setGeometry(100, 100, 1200, 800)

        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        self.map_tab = QWidget()
        self.login_tab = QWidget()
        self.tabs.addTab(self.login_tab, "Login")
        self.tabs.addTab(self.map_tab, "Map")

        self.initLogin()
        self.initMap()

    def initLogin(self):
        layout = QVBoxLayout(self.login_tab)

        self.username_input = QLineEdit(self.login_tab)
        self.username_input.setPlaceholderText("Enter username")
        layout.addWidget(self.username_input)

        self.password_input = QLineEdit(self.login_tab)
        self.password_input.setPlaceholderText("Enter password")
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_input)

        login_button = QPushButton("Login", self.login_tab)
        login_button.clicked.connect(self.login)
        layout.addWidget(login_button)

    def initMap(self):
        layout = QVBoxLayout(self.map_tab)

        self.map_view = QWebEngineView()
        layout.addWidget(self.map_view)

        self.loadMap()

    def loadMap(self):
        m = folium.Map(location=[-30.5595, 22.9375], zoom_start=6)

        # Example of adding a marker
        folium.Marker([-33.918861, 18.4233], popup='<i>Charging Station 1</i>').add_to(m)

        m.save("map.html")
        self.map_view.setHtml(open("map.html").read())

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        response = requests.post(f"{API_URL}/login", json={"username": username, "password": password})

        if response.status_code == 200:
            self.token = response.json()['access_token']
            QMessageBox.information(self, "Login Success", "Logged in successfully!")
            self.tabs.setCurrentWidget(self.map_tab)
        else:
            QMessageBox.warning(self, "Login Failed", "Incorrect username or password.")

def main():
    app = QApplication(sys.argv)
    main_window = EVChargerLocator()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
