print(" ")
print("Wordle")
print("Guess word that have 5 letter")
print(" ")
import random
words = ["water", "tiger", "lemon", "happy", "snake", "mouse", "chair", "angel", "horse", "smile", "cloud", "music", "table", "beach", "plant", "ocean", "queen", "space", "apple", "earth", "sunny", "funny", "storm", "quiet", "bread", "grass", "stone", "piano", "fruit", "dance", "laugh", "honey", "pizza", "train", "ghost", "candy", "robot", "phone", "arrow", "magic", "maple", "foggy", "mango", "windy", "tulip", "hazel", "stark", "sleet", "wings", "torch", "frost", "chill", "creek", "globe", "giant", "wrist", "juice", "click", "cycle", "vivid", "crown", "guide", "bumpy", "plush", "vocal", "chest", "grain", "zoomy", "silky", "swift", "ample", "break", "champ", "drift", "funky", "glide", "jumbo", "mirth", "quota", "squad", "trace", "blend", "blitz", "delta", "forge", "gloom", "waive", "sweep", "whale", "forge", "brave", "jiffy", "joker", "diver", "forge", "grill", "bevel", "vault", "caddy", "radar", "flash", "joint", "joust", "razor", "quest", "quota", "woven", "stark", "vowel", "wager", "nifty", "lunar", "jelly", "ivory", "jumbo", "haste", "grasp", "giddy", "froth", "pluck", "douse", "bleat", "spore", "joust", "gears", "vivid", "quirk", "bison", "haiku", "sweep", "whale", "churn", "quota", "forge", "brave", "jiffy", "joker", "diver", "forge", "quota", "grill", "bevel", "vault", "caddy", "flash", "joint", "joust", "razor", "quest", "quota", "woven", "stark", "vowel", "wager", "nifty", "lunar", "jelly", "ivory", "haste", "giddy", "froth", "pluck", "douse", "bleat", "spore", "joust", "gears", "vivid", "quirk", "bison", "haiku", "sweep", "whale", "churn", "quota", "forge", "brave", "jiffy", "joker", "diver", "forge", "quota", "grill", "bevel", "vault", "caddy", "flash", "joint", "joust", "razor", "quest", "quota", "woven", "stark", "vowel", "wager", "nifty", "lunar", "jelly", "ivory", "haste", "giddy", "froth", "pluck", "douse", "bleat", "spore", "joust", "gears", "vivid", "quirk", "bison", "haiku", "sweep", "whale", "churn", "quota", "forge", "brave", "jiffy", "joker", "diver", "forge", "quota", "grill", "bevel", "vault", "caddy"]
answer_list =  []
print("Guess word:")
round = 0

while True:
 list1 =  []
 word_guess = random.choice(words)
 for pismeno1 in word_guess:
  list1.append(pismeno1)
 round += 1
 trys=1
 print(f"Round: {round}")
 chance = 6
 
 while chance > 0:
  chance -= 1
  answer_list =  []
  number = 0
  answer = input(f"{trys}. ")
  trys += 1
  
  for pismeno2 in answer:
          answer_list.append(pismeno2)
  answer_list.append("-")
  answer_list.append("-")
  answer_list.append("-")
  answer_list.append("-")
  answer_list.append("-")
  print(f" {answer_list[0]} {answer_list[1]} {answer_list[2]} {answer_list[3]} {answer_list[4]}")
  
  if answer != word_guess:
    if chance != 0: 
     if answer_list[0] == list1[0]:
          letter0 = "🟩"
     elif answer_list[0] == list1[1]:
          letter0="🟧"
     elif answer_list[0] == list1[2]:
          letter0="🟧"
     elif answer_list[0] == list1[3]:
          letter0="🟧"
     elif answer_list[0] == list1[4]:
          letter0="🟧"
     else :
          letter0= "⬜"





     if answer_list[1] == list1[1]:
          letter1 = "🟩"
     elif answer_list[1] == list1[0]:
          letter1="🟧"
     elif answer_list[1] == list1[2]:
          letter1="🟧"
     elif answer_list[1] == list1[3]:
          letter1="🟧"
     elif answer_list[1] == list1[4]:
          letter1="🟧"
     else :
          letter1= "⬜"
     
     
     
     
     
     
     if answer_list[2] == list1[2]:
          letter2 = "🟩"
     elif answer_list[2] == list1[1]:
          letter2="🟧"
     elif answer_list[2] == list1[0]:
          letter2="🟧"
     elif answer_list[2] == list1[3]:
          letter2="🟧"
     elif answer_list[2] == list1[4]:
          letter2="🟧"
     else :
          letter2= "⬜"








     if answer_list[3] == list1[3]:
          letter3 = "🟩"
     elif answer_list[3] == list1[1]:
          letter3="🟧"
     elif answer_list[3] == list1[2]:
          letter3="🟧"
     elif answer_list[3] == list1[0]:
          letter3="🟧"
     elif answer_list[3] == list1[4]:
          letter3="🟧"
     else :
          letter3= "⬜"



     if answer_list[4] == list1[4]:
          letter4 = "🟩"
     elif answer_list[4] == list1[1]:
          letter4="🟧"
     elif answer_list[4] == list1[2]:
          letter4="🟧"
     elif answer_list[4] == list1[3]:
          letter4="🟧"
     elif answer_list[4] == list1[0]:
          letter4="🟧"
     else :
          letter4= "⬜" 
     print(f"{letter0}{letter1}{letter2}{letter3}{letter4}")
    
    else :
        print(f"{letter0}{letter1}{letter2}{letter3}{letter4}")
        print(" ")
        print(f"Nice try, but right answer is: {word_guess}") 
        print(" ") 
  elif answer == word_guess:
   print("🟩🟩🟩🟩🟩")
   print(" ")
   print(f"Good job!! The answer is: {word_guess}" )
   print(" ")
   while chance != 0:
        chance -= 1

 