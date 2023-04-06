import re
from validator_collection import validators
import sys

# format: #.#.#.#, kan sikkert gjerast med .+\.+. osv

def main():
    email = input("Hand over your email:")
    print(validate_email(email))

def validate_email(email):
    if validators.email(email):
        return "OKIDOKIE!"
    else:
        raise ValueError("Invalid email address.")


if __name__ == "__main__":
    main()
