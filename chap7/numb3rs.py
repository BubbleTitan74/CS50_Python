import re
import sys

# format: #.#.#.#, kan sikkert gjerast med .+\.+. osv

def main():
    ip = input("IPv4 Address: ")
    print(validate(ip))

def validate(ip):
    #if matches := re.search(r"(.+)\d\.(.+)\d\.(.+)\d\.(.+)\d", ip):
    if matches := re.search(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.)(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.)(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.)(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))$", ip):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
