# API Reference

## stegano Module

### `stegano.encode(input_path, output_path, message)`

Encode a message into an image.

**Parameters:**
- `input_path` (str): Path to the input image file
- `output_path` (str): Path to save the output image with the hidden message
- `message` (str): The secret message to encode

**Raises:**
- `ValueError`: If the message is too long to be encoded in the image
- `IOError`: If there's an error reading or writing image files

### `stegano.decode(image_path)`

Decode a message from an image.

**Parameters:**
- `image_path` (str): Path to the image containing the hidden message

**Returns:**
- str: The decoded message

**Raises:**
- `IOError`: If there's an error reading the image file
- `ValueError`: If no valid message is found in the image

## GUI Module

### `gui.main()`

Launch the KAT Cipher graphical user interface.

This function initializes and starts the PyQt6-based GUI application.
