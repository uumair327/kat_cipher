# Examples

## Basic Example

```python
from kat_cipher import stegano

# Encode a message
stegano.encode("input.png", "secret_image.png", "This is a secret message!")

# Decode the message
decoded = stegano.decode("secret_image.png")
print(f"Decoded message: {decoded}")
```

## Using with Different Image Formats

KAT Cipher supports various image formats including PNG, JPG, and BMP:

```python
from kat_cipher import stegano

# Encode to JPG
stegano.encode("photo.jpg", "secret_photo.jpg", "Hidden in JPG")

# Decode from JPG
message = stegano.decode("secret_photo.jpg")
print(message)  # Output: Hidden in JPG
```

## Error Handling

```python
from kat_cipher import stegano

try:
    # Try to encode a message that's too long
    with open("long_message.txt", "r") as f:
        long_message = f.read()
    stegano.encode("input.png", "output.png", long_message)
except ValueError as e:
    print(f"Error: {e}")
```
