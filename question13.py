# WAP to accept a name from a user. Raise and handle appropriate exception(s) if the
# text entered by the user contains digits and/or special characters
name=input("Enter Your Name : ")
if name.isalpha():
    print(name)
elif name.isdigit():
    print("Digits not allowed in name.")
elif name.isalnum():
    print("Name should not contain digits.")
else:
    print(f"Name should not contain special characters.")