import math

cipher = [151146, 1158786, 1276344, 1360314, 1427490, 1377108, 1074816, 1074816, 386262, 705348, 0, 1393902, 352674, 83970, 1141992, 0, 369468, 1444284, 16794, 1041228, 403056, 453438, 100764, 100764, 285498, 100764, 436644, 856494, 537408, 822906, 436644, 117558, 201528, 285498]
test_cipher = [487026, 436644]
key = 54
text_key = "trudeau"

def decrypt_cipher(cipher, key):
    semi_cipher = []
    for int in cipher:
        new_int = math.floor(int/key/311)
        print(chr(new_int))
        semi_cipher.append(chr(new_int))
    return semi_cipher

semi_cipher = decrypt_cipher(cipher, key)
print(semi_cipher)

def decrypt_semi_cipher(semi_cipher, text_key):
    plaintext = ""
    key_length = len(text_key)
    for i, char in enumerate(semi_cipher[::1]):
        key_char = text_key[i % key_length]
        decrypted_char = chr(ord(char) ^ ord(key_char))
        plaintext += decrypted_char
    return plaintext

def reverse_string(s):
    reversed_s = ""
    for char in s:
        reversed_s = char + reversed_s
    return reversed_s

plaintext = reverse_string(decrypt_semi_cipher(semi_cipher, text_key))
print(plaintext)
