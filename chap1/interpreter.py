def main():
    print("X can be any number\nY can either be '+','-','*' or '/'\nZ can be any number, but remember you can't divide with null")
    print("You must write you calculation int the following format: 'x y z'")

    try:
        text = input("Expression: ")
        x,y,z = text.split(' ')
        xN = float(x)
        zN = float(z)

        if y =="/" and z =="0":
            print("NO!")

        if y == "+":
            answer = xN + zN
            print(answer)
        elif y == "-":
            answer = xN - zN
            print(answer)
        elif y == "*":
            answer = xN * zN
            print(answer)

        elif y == "/":
            answer = xN/zN
            print(answer)




    except:
        print("Try again")










main()