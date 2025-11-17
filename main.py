def riddle_game():
    riddles={
        "1. What is always coming but never arrives? ": "Tomorrow",
        "2. What gets wetter the more it dries? " : "Towel",
        "3. What can be broken but never held? " : "Promise",
        "4. What word is spelled incorrectly in every single dictionary? " : "Incorrectly",
        "5. What is it that lives if it is fed, and dies if you give it a drink?" : "Fire",
        "6. What never asks a question but gets answered all the time?":"Cellphone",
        "7. What word would you use to describe a man who does not have all his fingers on one hand?":"Normal",
        "8. What goes up but never ever comes down?" : "Age",
        "9. What can one catch that is not thrown?" : "Cold",
        "10. If you have one, you want to share it. But once you share it, you do not have it. What is it?" : "Secret"
    }
    print("Welcome to the riddle game!")

    riddle_list = list(riddles.keys())
    points = 0

    i=0

    while i<10:
        riddle =riddle_list[i]
        right_answer = riddles[riddle]


        print(riddle)

        try:
            answer = input("Enter your answer: ").strip()
            if answer.lower() == right_answer.lower():
                print("Congrats. Next question.")
                points += 1
            else:
                raise ValueError(f"Wrong Answer Or NOT WRITTEN CORRECTLY. The answer was {right_answer.lower()}")
        except Exception as e:
            print(e)

        i+=1

    print("The questions are done. Game over!")
    print(f"Your total points: {points}/10")

riddle_game()