def main():
    sum = 0
    print("total sum: ",sum)
    while True:
        add_mynt = input("Insert coin: ")



        mynt = int(add_mynt)

        if add_mynt == "5":
            sum = sum + mynt
        elif add_mynt == "10":
            sum = sum + mynt
        elif add_mynt == "25":
            sum = sum + mynt
        elif add_mynt == "break":
            break
        else:
            print("Try again")

        if sum >= 50:
            print("___")
            print("|C|")
            print("|O|")
            print("|K|")
            print("|E|")
            print("###\n")
            change = sum - 50
            print(f"Change owed: {change}")
            # reset sum
            del sum
            break





main()