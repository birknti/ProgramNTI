import random

x = -7
lista = [
    "apple", "bread", "breakfast", "car", "chair", "cheese", "coffee", "moa",
    "computer", "door", "family", "friend", "garden", "house", "jacket", "liam",
    "kitchen", "market", "money", "morning", "music", "phone", "school", "filip",
    "shoes", "sister", "street", "table", "teacher", "water", "window", "jose",
    "animal", "beach", "book", "bottle", "dinner", "doctor", "evening", "isak",
    "flower", "food", "game", "letter", "lunch", "mother", "movie", "kean",
    "office", "park", "picture", "rain", "room", "shirt", "shop", "otto",
    "store", "summer", "ticket", "town", "travel", "weather", "weekend", "birk",
]
gissningar = []
max_fel = 6
fel = 0
lifeline = [
r"""
 ♥ ♥ ♥ ♥ ♥ ♥
      O
     /|\
     / \
""",
r"""
 ♥ ♥ ♥ ♥ ♥
      O
     /|
     / \
""",
r"""
 ♥ ♥ ♥ ♥
      O
      |
     / \
""",
r"""
 ♥ ♥ ♥
      O
      |
     / 
""",
r"""
 ♥ ♥
      O
      |
     / 
""",
r"""
 ♥
      O
      |
     
""",
r"""
 DEAD 
      
      |
     
"""
]

word = random.choice(lista)

while fel < max_fel:
 display = ""
 print(lifeline[x])
 print("Amount of guesses:", gissningar)
 
 for letter in word:
    if letter in gissningar:
        display += letter + " "
    else:
        display += "_ "
 if "_ " not in display:
     print(f"You won! the word was {word}!")
     print(f"Your guesses: {gissningar}")
     break
 
 print("Ord:", display)

 gissning = input("Type a letter: ").lower()
 
 if gissning in gissningar:
  print("You have already guessed that letter.")
 
 else:
  gissningar.append(gissning)

  if gissning not in word:
      print("You lost one life!")
      x += 1
  
      if x == -1:
       print(lifeline[-1])
       break
 
  

  
