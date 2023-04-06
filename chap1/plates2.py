def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if lengd(s) and feil(s) and twoNummer(s) and nullTull(s):
        return True

def feil(s):
    if not s.isalnum():
        return False
    return True

def lengd(s):
    if len(s) >= 2 and len(s) <= 6:
        return True
    
def twoNummer(s):
    if s[0].isalpha() == False and s[1].isalpha == False:
        return False
    else:
        return True
def nullTull(s):
    for i in s:
        if i.isnumeric():
            if int(i) == 0:
                return False
            break

    for i in s:
        if i.isnumeric():
            for j in s[s.find(i) :]:
                if j.isalpha():
                    return False
    return True

if __name__ == "__main__":
    main()
