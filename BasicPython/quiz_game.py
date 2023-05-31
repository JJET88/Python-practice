# Quiz game
questions = ("1.How many elements are in the periodic table?:",
            "2.Which animal lays the largest egg?:",
            "3.What is the abundant gas in Earth's atmosphere?:",
            "4.How many bones are in the human body?:",
            "5.Which planet in the solar system is the hottest?:")
options =(("A.116","B.117","C.118","D.119"),
          ("A.Whale","B.Crocodile","C.Elephant","D.Ostrich"),
          ("A.Nitrogen","B.Oxygen","C.Carbon-Dioxide","D.Hydrogen"),
          ("A.206","B.207","C.208","D.209"),
          ("A.Mercury","B.Venus","C.Earth","D.Mars"))
answers =("C","D","A","A","B")
guesses =[]  #629 
score = 0
questions_index =0

for question in questions:
    print("---------------------")
    print(question)
    
    for option in options[questions_index]:
        print(option)

    guess = input("Enter (A,B,C,D)::").upper()
    guesses.append(guess) 
    if guess == answers[questions_index]:

        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[questions_index]} is the correct answer")    


    print(f"Your score is {score}")

    questions_index += 1

print("answer::",end=" ")
for answer in answers:
    print(answer,end=" ")    

print()
print("guess ::",end=" ")
for guess in guesses:
    print(guess,end=" ")