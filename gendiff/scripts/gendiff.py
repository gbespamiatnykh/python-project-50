import argparse
import json


def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("-f", "--format", help="set format of output")
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    args = parser.parse_args()
    first_file = json.load(open(args.first_file))
    second_file = json.load(open(args.second_file))
    print(f"first_file: {first_file}\nsecond_file: {second_file}")


if __name__ == "__main__":
    main()
