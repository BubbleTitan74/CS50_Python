from datetime import date
import regex, sys, inflect
#365 days x 24 hours X 60 minutes = 525,600 minutes
p = inflect.engine()
#@classmethod
# date.today()

def main():
    date_of_birth = input("When did you get born?\nWrite in this format: YYYY-MM-DD:\n")
    try:
        year, month, day = check_birthday(date_of_birth)

    except UnboundLocalError:
        sys.exit("Invalid date!")

    todays_date = date.today()
    


    diff = todays_date - date(int(year), int(month), int(day))
    diff_minutes = diff.days * 24 * 60
    output = p.number_to_words(diff_minutes, andword="")
    print(output.capitalize() + " minutes")
    #print how old they are in minutes but print it as text where it is assumed they are born on midnight00:00:00

def check_birthday(date_of_birth):
    if regex.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", date_of_birth):
        year, month, day = date_of_birth.split("-")
        print(type(month))
        if regex.search(r"^0[0-9]{1}$", month):
            month = month[1]
            print(month)

        if regex.search(r"^0[0-9]{1}$", day):
            day = day[1]
    return year, month, day

if __name__ == "__main__":
    main()
