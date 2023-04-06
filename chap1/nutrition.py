frukter = [
            {"namn": "apple", "cal": "112"},
            {"namn": "banana", "cal":"69"},
            {"namn": "kiwi", "cal": "101"}
]

val = str(input("write your desired fruit: "))

for frukt in frukter:
    x = "cal"
    if val == frukt["namn"]:
        print(f"Your desired friut contains {frukt[x]} calories")

        print("", end="")



