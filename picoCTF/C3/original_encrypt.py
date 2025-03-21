import sys
chars = "Hello"
# from fileinput import input
# for line in input('C3/custom'):
#   chars += line

print(chars)

lookup1 = "\n \"#()*+/1:=[]abcdefghijklmnopqrstuvwxyz"
lookup2 = "ABCDEFGHIJKLMNOPQRSTabcdefghijklmnopqrst"

out = ""

prev = 0
for char in chars:
  try:
      cur = lookup1.index(char)
  except ValueError:
      # Handle the case where the character is not found in lookup1
      print(f"Character '{char}' not found in lookup1, skipping.")
      continue  # Skip this character and move on to the next one
  out += lookup2[(cur - prev) % 40]
  prev = cur
  print(cur)

sys.stdout.write(out)
