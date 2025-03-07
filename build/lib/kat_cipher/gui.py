import random
import string
import cv2
import numpy as np
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QTextEdit, QFileDialog, QVBoxLayout
from .stegano import SanskritSteganoSystem  # Import the class from the correct module

class SteganoGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.system = SanskritSteganoSystem()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Sanskrit Steganography System")
        self.setGeometry(200, 200, 500, 400)
        
        self.input_text = QTextEdit(self)
        self.encode_button = QPushButton("Encode & Save Image", self)
        self.decode_button = QPushButton("Decode from Image", self)
        self.result_label = QLabel("", self)
        
        self.encode_button.clicked.connect(self.encode_message)
        self.decode_button.clicked.connect(self.decode_message)
        
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Enter Message:"))
        layout.addWidget(self.input_text)
        layout.addWidget(self.encode_button)
        layout.addWidget(self.decode_button)
        layout.addWidget(self.result_label)
        
        self.setLayout(layout)
    
    def encode_message(self):
        message = self.input_text.toPlainText()
        if not message:
            self.result_label.setText("Please enter a message.")
            return
        
        image_path, _ = QFileDialog.getOpenFileName(self, "Select Image to Encode")
        if not image_path:
            return
        
        output_path, _ = QFileDialog.getSaveFileName(self, "Save Encoded Image", "", "PNG Files (*.png)")
        if not output_path:
            return
        
        self.system.encode_message_to_image(message, image_path, output_path)
        self.result_label.setText("Message successfully encoded into image!")
    
    def decode_message(self):
        image_path, _ = QFileDialog.getOpenFileName(self, "Select Image to Decode")
        if not image_path:
            return
        
        decoded_message = self.system.decode_message_from_image(image_path)
        self.result_label.setText(f"Decoded Message: {decoded_message}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = SteganoGUI()
    gui.show()
    sys.exit(app.exec())
