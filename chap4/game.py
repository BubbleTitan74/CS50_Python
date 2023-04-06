import random

#Promt user for n level (x, xx, xxx) siffer
while True:
    level = input("Hvor mange siffer vil du gjette med?  ")
    level = int(level)
    if level == 1 or level == 2 or level == 3:
        break
    else:
        print("try again")

#Generate random int mellom 1 og n med random modul
if level == 1:
    n = random.randint(1, 9)
elif level == 2:
    n = random.randint(1, 99)
elif level == 3:
    n = random.randint(1, 999)

#prompter brukaren til å¨gjette tallet med tre forsøk med tampenn brenner.
tries = 0
while True:
    tries = tries + 1
    print(tries)
    guess = input("Kva trur du tallet er?\n")
    guess = int(guess)
    if guess == n:
        print("Just right!")
        break
    if tries == 3:
        print(f"Wrong. The integer was {n}")
        break
    elif guess > n:
        print("Too hot...")
    elif guess < n:
        print("Too cold...")
    else:
        print("No!")
    

    
