# string indexing = [start:end:step]
credit = "12-344-676-2323-32-3"
print(credit[0])
print(credit[5])
print(credit[0:5])
print(credit[-1])
print(credit[::2])
print(credit[::-1])
print(credit[-5:])

# email slice
email = input("Enter your Email::")
index = email.index("@")
username = email[:index]
domain =email[index+1:]
print(f"username is {username} and domain is {domain}")
