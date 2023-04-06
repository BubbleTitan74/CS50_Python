def main():
    try:
        ext = input("Please enter a file: \n")
        listOfWord = ext.split('.', 1)
        if len(listOfWord) > 0:
            ext = listOfWord[1]
    except:
        print("application/octet-stream")


    match ext:
        case "gif" | "jpeg" | "png" | "jpeg":
            print(f"image/{ext}")
        case "txt" | "png" | "zip":
            print(f"application/{ext}")
        case _:
            print("application/octet-stream")

main()