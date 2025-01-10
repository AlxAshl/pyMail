import re
def validate_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(pattern, email):
        return True
    return False
email = input("Enter your email: ")
if validate_email(email):
    print("Email is valid")
else :
    print("Email is not valid")