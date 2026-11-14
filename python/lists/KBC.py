

questions = [['which language are usefull to became a Data sacentitis?','python', 'java', 'c++', 'c', 1],
  ['which language are usefull to became a Software engineer?','python', 'java', 'c++', 'c', 2],
  ['which language was used to create fb?','python', 'java', 'none', 'php', 2],
  ['what is a captila of india ','Asssam', 'Sikkim', 'Agra', 'Delhi', 4],
  ['which soical media platfrom is usefull to earn money ','youtube', 'facebook', 'insatgram', 'none', 1],
  ['who is a presdint of india ','satyam', 'modi jii', 'rahul jhatu', 'none', 1],
]

level = [100,2000,5000,10000,50000,100000]

money = 0

for i in range(0, len(questions)):
    question = questions[i]
    print("Question for Rs.{level[i]}")
    print("a. {question[1]}              b. {question[2]} ")
    print("c. {question[3]}              d. {question[4]} ")
    reply = int(input("Enter your answer (1-4) : "))
    if(reply ==  question[-1]):
      print("Correct answer, you have won Rs.{level[i]}")
      if i == 1:
        money = 100
      elif i == 3:
        money = 5000
      elif i == 5:
        money = 50000
      elif i == 6:
        money = 100000

    else:
      print("wrong answer!")
      break
  
print(f"Your take total money is {money}")