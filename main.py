def riddle_game():
    riddles={
        "1. What is the capital of France?\n A) Paris\n B)London\n C)Berlin\n D)France": "A",
        "2. What does a butcher do for a living?\n A) Makes bread\n B)Sells meat\n C)Makes pencils\n D)Sells books" : "B",
        "3. Which of these is NOT a Pixar film?\n A) Wall-E\n B)Cloduy with a chance of meatballs\n C)Coco\n D)A bug's life " : "B",
        "4. Which of these animals is a marsupial?\n A) Wallaby\n B)Panda\n C)Penguin\n D)Woodpecker " : "A",
        "5. Which one of these was NOT a president of the United States of America?\n A) Donald Trump\n B)Barack Obama\n C)George Washington\n D)Arnold Schwarzenegger " : "D",
        "6. Which of these is a group of hills in the UK?\n A) The Alps\n B)The Andes\n C)The Pennines\n D)The Himalayas ":"C",
        "7. Who wrote Alice in Wonderland?\n A) JK Rowling\n B)CS Lewis\n C)Lewis Carroll\n D)Charles Dickens ":"C",
        "8. Who invented the telephone?\n A) Alexander Graham Bell\n B)Albert Einstein\n C)Thomas Edison\n D)Nikola Tesla" : "A",
        "9. Who won the Men's Football World Cup 2018?\n A) England\n B)Brazil\n C)France\n D)Germany " : "C",
        "10. Which year did WW2 end?\n A) 1939\n B)1942\n C)1944\n D)1945 " : "D",
        "11. 2020 was a leap year, but when was the next leap year?\n A) 2022\n B)2024\n C)2026\n D)2028 " : "B",
        "12. Which of these vegetables is technically a fruit?\n A) Potato\n B)Carrot\n C)Broccoli\n D)Tomato " : "D",
        "13. How many countries are there in the world?\n A) 194\n B)193\n C)195\n D)196 " : "C",
        "14. What does the word 'Reticent' mean?\n A) Being shy and not show your feelings\n B)Being ashamed\n C)Being Loved or seen\n D)Being hatred " : "A",
        "15. Which artist had the best selling single in the UK in 2019?\n A) Old town road\n B)Someone you loved\n C)I don't care\n D)Bad guy " : "B"
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
