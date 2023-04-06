import re
import sys


def main():
    link = input("HTML: ")
    print(parse(link))

#Chatter'n 
def parse(iframe_html):
    youtube_link_regex = r'src="(https://www.youtube.com/embed/\w+)"'
    if match := re.search(youtube_link_regex, iframe_html):
        return match.group(1)

"""
def parse(embeded_link):
    #Vil ha en embedded input
    if link := re.search(r"<iframe(.)*(src="https?:\/\/www\.youtube\.com\/embed\/(.)\w*")><\/iframe>")
"""

...


if __name__ == "__main__":
    main()
