from .strsplit import split, SplitByStr
from .iterator import SplitIter


def main():
    input_file = "a,b,c,d,e,f"
    it: SplitIter = split(input_file, SplitByStr(","))
    print(list(it))


if __name__ == "__main__":
    main()
