import sys, csv
from tabulate import tabulate

#table_S = [["Sicilian Pizza","Small","Large"],["Cheese","$25.50","$39.95"],["1 item","$27.50","$41.95"],["2 items","$29.50","$43.95"],["3 items","$31.50","$45.95"],["Special","$33.50","$47.95"]]
#table_R = [["Regular Pizza","Small","Large"],["Cheese","$15.50","29.95"],["1 item","$17.50","$31.95"],["2 items","$19.50","$33.95"],["3 items","$21.50","$35.95"],["Special","$23.50","$37.95"]]
#Dette skal ikkje gjerast. Fila skal leses som .csv!!



try:
    file = sys.argv[1]
    py = file.split(".")


except IndexError:
    print("Too few cmd lines in arg.")
    sys.exit()
count = 0
hash_count = 0

dict_sicilian = []
try:
    with open(f'{file}', 'r') as open_file:
        reader = csv.reader(open_file)
        for first, secound, third in reader:
            dict_sicilian.append({"Item": first, "Small_size": secound, "Large_size": third})

        open_file.close()

except FileNotFoundError:
    print("There is no such file")
    sys.exit

print(tabulate(dict_sicilian, tablefmt="pretty"))