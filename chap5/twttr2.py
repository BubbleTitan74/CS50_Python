
def main():

    tweet = input("Type in tweet:")
    tweet_uten_vokal =shorten(tweet)
    print("Your tweet:", tweet_uten_vokal)

def shorten(word):
    vowels = ["a", "e", "i", "o", "u", "y"]
    #En slik liste kan også skrivest som en string med bruk av char
    for ch in word:
        if ch.lower() in vowels:
            word = word[: word.find(ch)] + word[word.find(ch) + 1 :]
            #Kva betyr denne ^^?
    return word

if __name__ == "__main__":
    main()