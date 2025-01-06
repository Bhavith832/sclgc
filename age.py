age = int(input("Enter the age:"))
if age >0 and age<=12:
    print("This is the age belong to Child.")
elif age>12 and age<=19:
    print("This is the age belong to teenager. ")
elif age>19 and age <=64:
    print("This is the age belong to adult.")
else:
    print("the entered age is senior.")
