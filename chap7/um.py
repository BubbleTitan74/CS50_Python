import re
import sys


def main():
    um_txt = input("Text: ")
    print(count(um_txt))

def count(um_txt):
    um_count = 0
    if matches := re.findall(r",( )?um(m)*", um_txt):

    #Forventa string og teller antall "um" i setningen
        num_matches = len(matches)
        
    return um_count + num_matches

if __name__ == "__main__":
    main()
