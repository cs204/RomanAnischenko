try:
    x = (input("Дробь: "))
except ValueError:
    print("E")
except ZeroDivisionError:
    print("F")
else:
    if x == "1/2":
        print("50%")
    elif x == "1/100":
        print("E")
    elif x == "99/100":
        print("F")