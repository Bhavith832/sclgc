user_input=input("Enter the user name:")
plan=input("Enter the plan EX: Normal, prime?")
id=int(input("Enter the id:"))
lst=[111,222,333]

if plan=="prime" and id in lst:
    print("ur a prime number")
else:
    print("ur not prime number")