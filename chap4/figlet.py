from pyfiglet import Figlet
import sys
import random

if len(sys.argv) == 1:
    randi = True
elif len(sys.argv) == "-f" or "--font":
    randi = False

inp = input("Make a cool text:")

figlet = Figlet()

if randi == False:
    figlet.setFont(font=sys.argv[2])  
    ut = figlet.renderText(inp)
    print(ut)

elif randi == True:
    font = random.choice(figlet.getFonts())
    ut = figlet.renderText(inp)
    print(ut)

sys.exit(1)