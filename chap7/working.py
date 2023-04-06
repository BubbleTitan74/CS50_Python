import re
import sys


def main():
    tyme = input("Hours: ")
    print(convert(tyme))
    #Value error om det ikkje er på riktig format eller om tida er feil

def convert_12_to_24(tyme, am_pm):
    hours, minutes = map(int, tyme.split(':'))
    if am_pm.upper() == 'AM' and hours == 12:
        hours = 0
    elif am_pm.upper() == 'PM' and hours != 12:
        hours += 12
    return '{:02d}:{:02d}'.format(hours, minutes)
def convert(tyme):
    #([0-1]?[0-9]|2[0-3]):[0-5]?[0-9]
    if matches := re.search(r"(1[0-2]|0?[1-9]):([0-5][0-9]) (AM|PM) to (1[0-2]|0?[1-9]):([0-5][0-9]) (AM|PM)", tyme):
    # Forventar enter 12 tima eller 24 tima klokke string
    # som 09:00 | 21:00 med AM og PM for 12 timar.
        start_time = matches.group(1) + ":" + matches.group(2)
        end_time = matches.group(4) + ":" + matches.group(5)
        start_time_24 = convert_12_to_24(start_time, matches.group(3))
        end_time_24 = convert_12_to_24(end_time, matches.group(6))
        return start_time_24 + " to " + end_time_24
    else:
        print("lol")

if __name__ == "__main__":
    main()
