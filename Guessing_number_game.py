from random import randint

num = randint(1,100)
print("guess the number between (1-100):-")
guess = 0

while True:
    you = int(input("guess the number: "))
    guess = guess + 1
    
    if you == num:
        print(f"you guessed the number {num}, in {guess}") 
        break

    elif you < num:
        print("higher number please!")

    elif you > num:
        print("lower number please!")
