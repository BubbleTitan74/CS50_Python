import sys
from PIL import Image, ImageOps

#__________________________________TAKS________________________
#Expects 2 cmds as shirt and models. (1st to read, 2nd to write)
#Use Image.open for resize og crop via Image.crop,
#dermed Image.paste og tilslutt Image.save.
#Løs ut sys.exit om:
#Feil cmds
#Ikkje bildefil med case sensivitet
#Ulik fil extention
#Ingen fil funnet.
#______________________________________________________________


your_pic, you_in_shirt = sys.argv[1], sys.argv[2]

if len(sys.argv) < 3:
    print("Too fo cmd lines")
    sys.exit()  
elif len(sys.argv) > 3:
    sys.exit("Too many lines in cmd")

file_format = ["png", "jpg", "jpeg"]
input_1 = sys.argv[1].rsplit(".")
input_2 = sys.argv[2].rsplit(".")
if input_1[1] not in file_format and input_2[1] not in file_format:
    print("Invalid file format.")
    sys.exit()

pic = Image.open(your_pic)

shirt = Image.open("shirt.png")
size = shirt.size

shirt_cropp = ImageOps.fit(your_pic, size)

shirt_cropp.paste(shirt, shirt)

shirt_cropp.save(sys.argv[2])

