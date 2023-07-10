import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QTextBrowser, QLineEdit, QPushButton, QLabel
from PyQt5.QtGui import QColor, QPixmap, QTextDocument, QTextImageFormat
from PyQt5.QtCore import QUrl


class ImageTextBrowser(QTextBrowser):
    def loadResource(self, type_, url):
        if type_ == QTextDocument.ImageResource and url.scheme() == "image":
            path = url.path()
            image_format = QTextImageFormat()
            image_format.setName(path)
            image_format.setWidth(200)  # Set the desired width of the image
            return image_format

        return super().loadResource(type_, url)


class ChatWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Chat Window")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.chat_layout = QVBoxLayout()
        self.central_widget.setLayout(self.chat_layout)

        self.message_browser = ImageTextBrowser()  # Use the custom QTextBrowser subclass
        self.message_browser.setReadOnly(True)
        self.chat_layout.addWidget(self.message_browser)

        self.input_layout = QHBoxLayout()
        self.chat_layout.addLayout(self.input_layout)

        self.input_box = QLineEdit()
        self.input_layout.addWidget(self.input_box)

        self.send_button = QPushButton("发送")
        self.send_button.setStyleSheet("background-color: green; color: white;")
        self.send_button.clicked.connect(self.send_message)
        self.input_layout.addWidget(self.send_button)

    def send_message(self):
        message = self.input_box.text()
        self.input_box.clear()
        self.display_message(message, "blue")

    def display_message(self, message, color):
        if message.startswith("image:"):
            image_path = message.split(":")[1]
            image_url = QUrl.fromLocalFile(image_path)

            # Insert the image URL into the message browser
            self.message_browser.append('<img src="{}">'.format(image_url.toString()))
        else:
            self.message_browser.append('<span style="color:{};">{}</span>'.format(color, message))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    chat_window = ChatWindow()
    chat_window.show()
    sys.exit(app.exec_())
