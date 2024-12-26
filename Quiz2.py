q=['1.What is the capital city of india?',
   '2.What is the national animal?',
   '3.Who is current prime minister of india?',
   '4.Who is the founder of facebook?',
   '5.When does facebook has launched?']

ans=['delhi','tiger','modi','markzukerburg','2004']
for x in q:
    print(x)
    user_ans=input('enter the answer:')
    if user_ans in ans:
        print("correct answer.")
    else:
        print("wrong answer.")