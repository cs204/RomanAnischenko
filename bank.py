greeting = input("Приветствие: ")
if greeting.startswith("здравствуйте"):
    print("$20")
elif greeting.startswith("з"):
    print("$20")
else:
    print("$100")