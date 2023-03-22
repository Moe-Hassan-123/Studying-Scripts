import argparse
import pathlib
import sys

import helper

vault_pos = pathlib.Path("/media/mohamed/Games/Studying")


def main(url: str, num: int):
    solving_file: pathlib.Path = vault_pos / helper.generate_link(url, "Solving")
    answers_file: str = helper.generate_link(url, "Answers")

    solving_file.touch(exist_ok=True)

    with solving_file.open("w") as f:
        helper.write_header_to_file(f, answers_file, num)
        for n in range(1, num + 1):
            f.write(f"- [ ] {n:02d} --> \n")


if __name__ == "__main__":
    args = sys.argv
    args.pop(0)
    parser = argparse.ArgumentParser(description="Generate a solutions page")
    parser.add_argument("-u", type=str, required=True)
    parser.add_argument("-n", type=int, required=True)

    args = parser.parse_args(args)
    main(args.u, args.n)
