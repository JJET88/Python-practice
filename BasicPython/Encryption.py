# Encryption program
import random
import string

chars = " " +string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
random.shuffle(key)

# print(f"chars : {chars}")
# print(f"key : {key}")
# Encryption
plain_text = input("Enter a message::")
cipher=""

for letter in plain_text:
    index =chars.index(letter)
    cipher += key[index]

print(f"Original Message::{plain_text}")
print(f"Encrypted Message::{cipher}")    

# Decryption
cipher = input("Enter an Encrypted message::")
plain_text=""

for letter in cipher:
    index =key.index(letter)
    plain_text += chars[index]

print(f"Encrypted Message::{cipher}")
print(f"Original Message::{plain_text}")    