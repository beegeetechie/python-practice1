print("Enter your name : ")
name = input()
print("Enter your ATM pin : ")
pin = input()
if pin == "1234":
    print("Welcome Mr. " + name)
    print("Select your Account Type")
else:
    print("Invalid PIN. Enter the correct PIN")


