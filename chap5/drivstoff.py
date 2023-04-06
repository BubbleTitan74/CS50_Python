#Programmet er i orden utenom logikken

def main():

    XnY = input("Drivstoff forholdet ditt\n")
    prosent = convert(XnY)
    print(gauge(prosent))

def convert(XnY):
    while True:
        try:
            teljar, nemnar = XnY.split("/")
            perc = int(teljar) / int(nemnar)
            if perc <=1:
                ny_perc = int(perc * 100)
                return ny_perc
            else:
                XnY = input("Drivstoff forholdet ditt\n")
        except (ValueError,ZeroDivisionError):
            raise

def gauge(prosent):
    # If som finner ut om den er tom eller full
    if prosent <= 1:
        print("E")
        return "E"
    elif prosent >= 100:
        print("F")
        return "F"
    else:
        print("Good 2 go!")
        return "G"
    return (None)


if __name__ == "__main__":
    main()