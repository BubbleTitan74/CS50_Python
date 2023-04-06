import inflect 

p = inflect.engine()

navn = []
while True:
    try:
        navnet = input("Name:")
        navn.append(navnet)
    except:
        print()
        break

ut = p.join(navn)
print("Adieu, adieu, to", ut,".")