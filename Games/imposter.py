import random
import msvcrt
import os
while True:
 amount = int(input("How many players are playing: "))

 players = []

 reset = False

 while reset == False:

  for i in range(amount):

   player = input(f"Enter player {i + 1}'s name: ")
   players.append(player)

 print(players)

 words_and_hints = {
   "Sonic": "Videogame", "Mario": "Videogame",
   "Spiderman": "Movie", "Batman": "Movie"
 }

 imposter = random.choice(players)

 word = random.choice(list(words_and_hints))
 hint = words_and_hints[word]

 for i in range(amount):
   if players[i] == imposter:
     print(f"{players[i]} You are the imposter. Hint: {hint}")
     print("Press any key to continue")
     msvcrt.getch()
     os.system("cls")
   else:
     print(f"{players[i]} The word is: {word}")
     print("Press any key to continue")
     msvcrt.getch()
     os.system("cls")

 print("The game has started, try to figure out who doesn't know the word.")
 print("Press any key to continue")
 msvcrt.getch()

 print(f"{imposter} was the imposter.")

 choice = input("Would you like to switch players? (Y/n)")

 if choice.lower == "y":
   reset = True

 else:
   reset = False



 # yolo swag