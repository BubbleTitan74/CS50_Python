def main():

    vowels = ["a", "e", "i", "o", "u", "y", "æ", "ø", "å"]
    tweet = input()


    for letter in tweet:
        if  letter.lower() in vowels:
            letter.replace("letter", "")
        else:
            print(letter, end="")

main()