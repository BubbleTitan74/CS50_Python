import sys

try:
    file = sys.argv[1]
    py = file.split(".")

except IndexError:
    print("Too few cmd lines in arg.")
    sys.exit()
count = 0
hash_count = 0

try:
    with open(f'{file}', 'r') as open_file:
        for line in open_file:
            if line.strip():
                count += 1
            if line[0] == "#":
                hash_count += 1


        open_file.close()

    if py[1] != "py":
        print("This is not a python file\n")
        sys.exit
    elif py[1] == None:
        sys.exit
    elif sys.argv[2]:
        print("Too many files")
        count = 0
        sys.exit

except FileNotFoundError:
    print("There is no such file")
    sys.exit

if count > 0:   
    print(f"Number of lines:\n{count - hash_count}")
    del count, hash_count