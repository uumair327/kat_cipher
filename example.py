from kat_cipher import SanskritSteganoSystem

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