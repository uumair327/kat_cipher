# KAT Cipher

A Python package for Sanskrit-based text steganography in images.

## Features

- Encode secret messages into images using Sanskrit-based steganography
- Decode messages from images
- Simple and intuitive API
- Command-line interface
- Graphical User Interface (GUI)

## Quick Start

```python
from kat_cipher import stegano

# Encode a message in an image
stegano.encode("input.png", "output.png", "Your secret message")

# Decode a message from an image
message = stegano.decode("output.png")
print(message)  # Output: Your secret message
```

## Getting Help

If you encounter any issues or have questions, please [file an issue](https://github.com/uumair327/kat_cipher/issues) on GitHub.
