# string method
# result = len(name)
# result = name.find("e")
# result = name.rfind("j")
#
# result = name.capitalize()
#
# result = name.upper()
# result = name.lower()
# result = name.isdigit()
# result = name.isalpha()
# name = input("Enter your name ::")
# print(result)

# number = input("Enter your phone number")
# # result = number.count("6")
# result = number.replace("-","   ")
# print(result)

username = input("Enter your name")

if len(username) > 12:
    print("Your username must not contain more than 12 characters")
elif not username.find(" ") == -1:
    print("Username must not contain spaces")
elif not username.isalpha():
    print("Username must not contain digits")
else:
    print(f"Hello {username}")
