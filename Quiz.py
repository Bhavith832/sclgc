correct_ans=0
wrong_ans=0
print("1.which is the capital city of india?")
user_inp=input("Enter the answer:").lower()
print(user_inp)
if user_inp == "delhi":
    correct_ans+=1
    print("correct answer.")
else:
    wrong_ans-=1
    print("worng answer.")
    
# print("percentage",((correct_ans/(correct_ans+wrong_ans))*100))
    

print("2.which is the capital city of karnataka?")
user_inp=input("Enter the answer:").lower()
print(user_inp)
if user_inp == "bengaluru":
    correct_ans+=1
    print("correct answer.")
else:
    wrong_ans-=1
    print("worng answer.")
# print("percentage",((correct_ans/(correct_ans+wrong_ans))*100))

print("3.who is the current prime minister of india?")
user_inp=input("Enter the answer:").lower()
print(user_inp)
if user_inp == "modi":
    correct_ans+=1
    print("correct answer.")
else:
    wrong_ans-=1
    print("worng answer.")
# print("percentage",((correct_ans/(correct_ans+wrong_ans))*100))

print("4.who is the founder of meta?")
user_inp=input("Enter the answer:").lower()
print(user_inp)
if user_inp == "markzukerburg":
    correct_ans+=1
    print("correct answer.")
else:
    wrong_ans-=1
    print("worng answer.")
# print("percentage",((correct_ans/(correct_ans+wrong_ans))*100))

print("5.who is the founder of openAI?")
user_inp=input("Enter the answer:").lower()
print(user_inp)
if user_inp == "samaltman":
    correct_ans+=1
    print("correct answer.")
else:
    wrong_ans-=1
    print("worng answer.")
print("percentage",((correct_ans/(correct_ans+wrong_ans))*100))