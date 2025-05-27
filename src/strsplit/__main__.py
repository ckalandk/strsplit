from strsplit.splitter import SplitByAnyChar
from .strsplit import split


def main():
    input_file = "a, b;c d"
    it = split(input_file, SplitByAnyChar(chars=" ,;"),)
    print(list(it))


if __name__ == "__main__":
    main()
