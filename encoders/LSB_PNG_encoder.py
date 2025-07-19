from PIL import Image
import numpy as np

# Configurations
output_image_path = "find_the_msg.png"        # Where to save the new image
message = "message goes here"     # Your secret message
stop_marker = "/0"     # Stop marker for decoding
full_message = message + stop_marker
binary_message = ''.join([format(ord(c), '08b') for c in full_message])

# Load image
image = Image.open('C:\\Users\\Fanzh\\OneDrive\\Pictures\\Screenshots\\Screenshot 2025-07-05 001646.png')
image = image.convert('RGB')  # Ensure no alpha channel
pixels = np.array(image)

height, width, _ = pixels.shape
flat_pixels = pixels.reshape(-1, 3)  # Flatten to 1D list of RGB triplets

if len(binary_message) > len(flat_pixels) * 3:
    raise ValueError("Message is too long to hide in this image.")

# embed the message
bit_index = 0
for i in range(len(flat_pixels)):
    for j in range(3):  # R, G, B
        if bit_index < len(binary_message):
            flat_pixels[i][j] = (flat_pixels[i][j] & ~1) | int(binary_message[bit_index])
            bit_index += 1

# save the encoded image
encoded_pixels = flat_pixels.reshape((height, width, 3))
encoded_image = Image.fromarray(encoded_pixels.astype(np.uint8))
encoded_image.save(output_image_path)

print("Message embedded successfully in", output_image_path)
