year = int(input("Enter the year:"))

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(year,"The entered year is leap year:")
else:
    print(year,"The entered year is not leap year: ")