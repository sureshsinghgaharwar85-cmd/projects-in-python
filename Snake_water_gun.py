from random import choice
computer = choice(["snake", "gun", "water"])
you = input("enter your choice: ")


print(f"you choose {you}")
print(f"computer choose {computer}")

if computer == you:
  print("it's a draw")
else:
  # you to win
  if computer == "snake" and you == "gun":
    print("you won!")
  elif computer == "gun" and you == "water":
    print("you won!")
  elif computer == "water" and you == "snake":
    print("you won!")
  #computer to win
  elif computer == "gun" and you == "snake":
    print("computer won!")
  elif computer == "water" and you == "gun":
    print("computer won!")
  elif computer == "snake" and you == "water":
    print("computer won!")
  
  
  
