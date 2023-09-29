num = int(input("Enter the number of hours: "))

if num >= 0 and num < 6:
    print("Good Night")
elif num >= 6 and num < 13:
    print("Good Morning")
elif num >= 13 and num < 17:
    print("Good Day")
elif num >= 17 and num < 24:
    print("Good Evening")
