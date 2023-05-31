# Encryption program
import string
import random

char =" "+ string.punctuation + string.digits + string.ascii_letters
char = list(char)
key = char.copy()
random.shuffle(key)

# print(f"The char is:: {char}")
# print(f"The key is:: {key}")

# Encryption
plain_text = input("Enter a message::")
cipher =""
for letter in plain_text:
    index = char.index(letter)
    cipher += key[index]

print(f"The orighinal message:{plain_text}")
print(f"The encrypted message::{cipher}")

# Decryption
cipher = input("Enter an encrypted message::")
plain_text = ""
for letter in cipher:
    index = key.index(letter)
    plain_text += char[index]

print(f"The encrypted message::{cipher}")
print(f"The original message::{plain_text}")    