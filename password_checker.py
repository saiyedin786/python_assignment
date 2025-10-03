import re
user_password = input("Please Enter a strong password\n")

def check_password_strength(password):

    if len(password)<8:
        return [False,"Password Length should be more than 8 characters"]
    
    if not  re.search(r"[A-Z]",password):
        return [False,"Password should contain atleast on Uppercase Character"]
    
    if not  re.search(r"[a-z]",password):
        return [False,"Password should contain atleast on Lowercase Character"]
    
    if not  re.search(r"[0-9]",password):
        return [False,"Password should contain atleast one digit"]
    
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return [False,"Password should contain at least one special character"]
    
    return [True,"Strong Password"]
    
l = check_password_strength(user_password)
if l[0]:
    print(l[1])
else:
    error = check_password_strength(user_password)
    print(error[1])
