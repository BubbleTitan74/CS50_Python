def main():
    whatTime = input("What time is it: ")
    #kalle på func som nyttar time
    time = convert(whatTime)
    #sjekke opp mot returnert value
    if 7 <= time >= 8:
    #printe i forhald til returnert variabel
        print("Its breakfast time")
    elif 11. <= time >= 12.5:
        print("Its lunsj time")
    elif 15.5 <= time >= 19:
        print("Its dinner time")
    else:
        print("")

    timeN = float(time)
    print(timeN)
def convert(whatTime):
    hour, minutt = whatTime.split(':')

    minuttN = float(minutt) / 60

    return float(hour) + minuttN



main()
