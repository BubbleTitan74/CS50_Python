#__________Lib_____________________
import random

#______________Logikk______________
tall = input("Fra en skala til 1-10. Hva velger du?\n")
rand_tall = random.randint(1, 10)
print(rand_tall)
if tall == rand_tall:
    print("BOOM!. Oddsen traff.")
else:
    print("Kanskje neste gang")

#LMG