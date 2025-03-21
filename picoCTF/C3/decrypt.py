#WORK IN PROGRESS

import sys

encrypt = "SHAD"

lookup1 = "\n \"#()*+/1:=[]abcdefghijklmnopqrstuvwxyz"
lookup2 = "ABCDEFGHIJKLMNOPQRSTabcdefghijklmnopqrst"

decrypt = ""

prev = 0

for char in encrypt:
    try:
        cur = lookup2.index(char)
    except ValueError:
        print(f"Character '{char}' not found in lookup2, skipping.")
    decrypt += lookup1[(cur - prev) % 40]
    prev = cur

sys.stdout.write(decrypt)
