def main():
    greet = input("You work at a bank.\nHow do you greet your customer\n").strip().lower()
    greetH = greet[0]
    if greet == "hello":
        print("0$ to you...anyways. What can i help you with?")
    elif greetH == "h":
        print("Aw fine. Here is your 20$")
    else:
        print("NO! I am not giving you 100$")
main()