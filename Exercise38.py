print("Enter name of month to determine how many days in it.")
month = input("Enter month: ")

if "f" in month or "F" in month:
    print("There are 28 days in February.")
else:
    print("There 31 days in "+ month + ".")