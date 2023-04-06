def main():
    
    greet = input("You work at a bank.\nHow do you greet your customer\n").strip().lower()
    value(greet)

def value(greet):
    greetH = greet[0]
    if greet == "hello":
        print("0$ to you...anyways. What can i help you with?")
        return 0
    elif greetH == "h":
        print("Aw fine. Here is your 20$")
        return 20
    else:
        print("NO! I am not giving you 100$")
        return 100

if __name__ == "__main__":
    main()
