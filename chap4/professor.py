import random

def main():
    print("\nWelcome! Here is the math game that will give you 10 exercises.\nDecide what level you want to play by chosing from 1(Easy), 2(Normal) and 3(Hard)\nCan you get a score of 10?")
    generate_integer(get_level())

########################################################
#Ved å lage funksjoner i main så bør programmet skrives#
#i starten for å så kalle funksjonene i etterkant.     #
#OG HUGS Å HA RIKTIG INPUT TIL FUNKSJONEN!             #
########################################################


#Prompt for level n. Krav er at det må vere 1,2,3
def get_level():
    level_list = ["1","2","3"]
    while True:
        level = input("Hvor mange siffer vil du spille med?\n")
        if level not in level_list:
            continue
        return level

def guess_ans(X, Y):
    score = 0
    strikes = 0
    while True:
        solwing = input(f"{X} + {Y} =")
        if solwing == str(X + Y):
            check = True
            break
        elif solwing != str(X + Y):
            strikes += 1
            print("Wrong!")

        if strikes == 3:
            print(f"Superwrong! The answear was: {X + Y}")
            check = False
            break
    return check
    

#Generere 10 stykk tilfeldige matteoppgåver med addering(+)
def generate_integer(level):
    score = 0
    for i in range(10):
        if level == "1":
            X = random.randint(1, 9)
            Y = random.randint(1, 9)
        if level == "2":
            X = random.randint(10, 99)
            Y = random.randint(10, 99)
        if level == "3":
            X = random.randint(100, 999)
            Y = random.randint(100, 999)
        point = guess_ans(X, Y)
        if point == True:
            score = score + 1
        elif point == False:
            score = score + 0
    print("\nFinished!\nYour final score was:", score)



if __name__ == "__main__":
    main()