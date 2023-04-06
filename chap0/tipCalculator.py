def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))

    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(dollars):
    Rdollars = dollars.replace('$', '')
    Ndollars = float(Rdollars)
    return Ndollars


def percent_to_float(percent):
    Rpercent = percent.replace('%', '')
    Apercent = float(Rpercent)
    Npercent = Apercent/100
    return Npercent


main()
