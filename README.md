# Sanskrit Steganography System

## 📌 Overview

The **Sanskrit Steganography System** is a Python package that hides messages inside images using Sanskrit characters. It uses a novel encoding method inspired by the **Katapayadi system** to convert English text into Sanskrit characters before embedding them in an image using **LSB (Least Significant Bit) steganography**.

## ✨ Features

- 🔠 **Text to Sanskrit Encoding** – Converts English messages into Sanskrit characters using the Katapayadi system.
- 🖼 **Image Steganography** – Hides text inside an image using LSB encoding.
- 🖥 **GUI Support** – Includes a modern GUI using PyQt6.
- 📜 **Decoding Support** – Extracts hidden Sanskrit-encoded text and converts it back to English.
- 🐍 **Easy to Use** – Simple API for both CLI and GUI applications.

## 📥 Installation

### Install via pip (Local Development)

```bash
pip install .
```

### Dependencies

Ensure you have the required dependencies installed:

```bash
pip install opencv-python numpy pyqt6
```

## 🚀 Usage

### 🛠 Using the Python API

```python
from sanskrit_stegano import SanskritSteganoSystem

system = SanskritSteganoSystem()
message = "Hello, World!"
image_path = "input.png"
output_path = "output.png"

# Encoding
system.encode_message_to_image(message, image_path, output_path)
print("Message hidden inside image successfully!")

# Decoding
decoded_message = system.decode_message_from_image(output_path)
print("Decoded Message:", decoded_message)
```

### 🖥 Running the GUI

```bash
python -m sanskrit_stegano.gui
```

OR if installed as a package:

```bash
sanskrit-stegano
```

## 📸 GUI Preview

The graphical user interface (GUI) allows users to easily encode and decode messages within images.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙌 Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request.

## 📧 Contact

For questions or support, contact **Your Name** at **your.email@example.com** or visit [GitHub Repo](https://github.com/YashAPro1/kat_cipher.git).
