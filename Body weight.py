BMI = int(input("Enter the weight:"))

if BMI <18.5:
    print("You are under weight.")
elif BMI <= 18.5 and BMI < 24.9:
    print("you are in normal weight:")
elif BMI >= 25 and BMI < 29.9:
    print("You are in overweight.")
elif BMI >= 30:
    print("You are obese.")
else:
    print("Go to the hospital")