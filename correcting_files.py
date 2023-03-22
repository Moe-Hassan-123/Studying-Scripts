import argparse
import pathlib
import re
import sys

import helper

vault_pos = pathlib.Path("/media/mohamed/Games/Studying")


def extract_answers(file: pathlib.Path) -> list[str]:
    answer = []
    with file.open("r") as f:
        for line in f.readlines():
            if line[0] != "-" or line == "---\n":
                continue
            for ans in get_ans_from_line(line):
                answer.append(ans)
    return answer


def get_ans_from_line(line: str) -> str:
    line = re.sub("mark|background|#.*;|style|<|>|/", "", line)
    for ind, c in enumerate(line.lower()):
        if c in ["a", "b", "c", "d", "?", "!"]:
            return line[ind].strip()

    return "?"


def parse_answers(answers: str) -> list[int]:
    converted_answers = []

    for c in answers.lower():
        converted_answers.append(c)
    return converted_answers


def main(url: str) -> None:
    solving_file: pathlib.Path = vault_pos / helper.generate_link(url, "Solving")
    answers_file: pathlib.Path = vault_pos / helper.generate_link(url, "Answers")
    # Read correct answers from the answers note.
    ans_str: str = answers_file.read_text()

    # Convert them into a more combarable format
    correct_answers: list[int] = parse_answers(ans_str)

    # Get my Own answers from the solving note.
    my_answers: list[int] = extract_answers(solving_file)
    print(my_answers)

    if len(my_answers) != len(correct_answers):
        raise ValueError(
            f"Correct answers length doesn't match the Solving Note's answers length.\nYour Solutions Length = {len(my_answers)}\nThe Answers Length = {len(correct_answers)}"
        )

    answer = []
    correct = 0
    for ind in range(len(my_answers)):
        if my_answers[ind] == correct_answers[ind]:
            answer.append(1)
            correct += 1
        else:
            answer.append(0)

    new_page = ""
    cur_ans = 0
    page = solving_file.open()
    for line in page:
        if line[0] != "-" or line == "---\n":
            new_page += line
            continue

        line = line.strip("- [x]")
        line = line.strip("- [ ]")
        new_line = f"- [{'x' if answer[cur_ans] == 1 else ' '}] {line}"
        new_page += new_line
        cur_ans += 1

    with solving_file.open("w") as f:
        f.write(new_page)


if __name__ == "__main__":
    args = sys.argv
    args.pop(0)
    parser = argparse.ArgumentParser(
        description="Correct a solutions page using answers page"
    )
    parser.add_argument("-u", type=str)
    args = parser.parse_args(args)
    main(args.u)
