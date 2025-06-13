# Usage

## Basic Usage

### Encoding a Message

```python
from kat_cipher import stegano

# Encode a message into an image
stegano.encode("input.png", "output.png", "Your secret message")
```

### Decoding a Message

```python
from kat_cipher import stegano

# Decode a message from an image
message = stegano.decode("output.png")
print(f"Decoded message: {message}")
```

## Command Line Interface

You can also use KAT Cipher from the command line:

### Encode a message

```bash
kat_cipher encode input.png output.png "Your secret message"
```

### Decode a message

```bash
kat_cipher decode output.png
```

## GUI Application

Launch the graphical user interface with:

```bash
kat_cipher
```

The GUI provides a user-friendly way to encode and decode messages.
