password=input()
l=len(password)
if 1<8:
    print("Invalid password.....")
digit=False
upper=False
lower=False
for i in password:
    if i.isdigit():
        digit=True
    elif i.isupper():
        upper=True
    elif i.islower():
        lower=True
if digit and upper and lower:
    print("valid password")
else:
    print("Innvalid password")
