from .strsplit import split, SplitByStr
from .iterator import SplitIter


def main():
    input_file = "a,b,c,d,e,f"
    it: SplitIter = split(input_file, SplitByStr(delimiter=",", maxsplit=2))
    print(list(it))


if __name__ == "__main__":
    main()
