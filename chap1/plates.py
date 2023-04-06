#Ikkje tenk for vanskelig ved at det finst tools som løysar programmet for deg.
# Tenk helle enkelt og grunnleggande med det ein har lært.
#Nytt skissering og skriving kva programmet skal utføre og fin enklast veg.
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if lengd(s) and feil(s) and twoNummer(s) and nullTull(s):
        return True

def feil(s):
    if not s.isalnum():
        return False
    return True

def lengd(s):
    if len(s) >= 2 and len(s) <= 6:
        return True
    
def twoNummer(s):
    if s[0].isalpha() == False and s[1].isalpha == False:
        return False
    else:
        return True
def nullTull(s):
    for i in s:
        if i.isnumeric():
            if int(i) == 0:
                return False
            break

    for i in s:
        if i.isnumeric():
            for j in s[s.find(i) :]:
                if j.isalpha():
                    return False
    return True



    #Må nytte løkker for å scanne gjennom string


    #Sjekke den har to bokstavar som ankommer på slutten
    #Innehalde max 6 char
    #First char kan ikkje vere 0
    #Ingen mellomrom, punktum osv er tillat

if __name__ == "__main__":
    main()
