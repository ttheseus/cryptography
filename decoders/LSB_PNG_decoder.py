import numpy as np
import PIL.Image

# Configurations
image = PIL.Image.open('encoded.png', 'r')    # enter path to the image to decode
img_arr = np.array(list(image.getdata()))

# Make sure channels match
channels = 4 if image.mode == 'RGBA' else 3
pixels = img_arr.size // channels

# Decode the message
secret_bits = [bin(img_arr[i][j])[-1] for i in range(pixels) for j in range(0,3)]
secret_bits = ''.join(secret_bits)
secret_bits = [secret_bits[i:i+8] for i in range(0, len(secret_bits), 8)]

secret_message = [chr(int(secret_bits[i], 2)) for i in range(len(secret_bits))]

secret_message = ''.join(secret_message)

stop_indicator = "\0"

if stop_indicator in secret_message:
    print(secret_message[:secret_message.index(stop_indicator)])
else:
    print("Couldn't find secret message")
