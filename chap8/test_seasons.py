from seasons import check_birthday
def main():
    test_check_birthday()

def test_check_birthday():
    assert check_birthday('2001-09-10') == ("2001", "9", "10")
    assert check_birthday('2001-15-01') == ("2001", "15", "1")

if __name__ == "__main__":
    main()