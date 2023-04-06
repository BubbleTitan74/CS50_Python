import sys, csv, sub

#__________________________________TAKS________________________
#Forventer 2 filer i cmd line
#CSV filen skal gå fra (full_name, house) --> (first, last, house)
#Dette ved å splitte full_name til first og last.
#Unøyaktige spesifikasjoner skal resultere sys.exit.
#______________________________________________________________

Galtvort = []

try:
    pre_file, post_file = sys.argv[1], sys.argv[2]


except IndexError:
    print("Too few cmd lines in arg.")
    sys.exit()


with open(f'{pre_file}', 'r') as open_file:
    reader = csv.DictReader(open_file)
    for row in reader:
        split_name = row["name"].split(",")
        Galtvort.append({'first': split_name[1].lstrip(), 'last': split_name[0], "house": row["house"]})
    open_file.close()

with open(f'{post_file}', 'w') as newly_opend_file:
    writer = csv.DictWriter(newly_opend_file, fieldnames = ["first", "last", "house"])
    writer.writerow({"first": "first", "last": "last", "house": "house"})
    for row in Galtvort:
        writer.writerow ({"first": row["first"], "last": row["last"], "house": row["house"]})
    newly_opend_file.close()            

#Sjekk CS50 video for å filtrere ",  ," 

