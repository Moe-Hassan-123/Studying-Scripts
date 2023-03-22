from io import TextIOWrapper


def generate_link(url: str, new_header: str) -> str:
    new_link: list = url.split("/")[1:]
    new_link.insert(0, new_header)
    return "/".join(new_link)


def write_header_to_file(file: TextIOWrapper, answers_file, num) -> None:
    file.write(f"number of questions: {num}\n")
    file.write(f"Add correct answers [[{answers_file}|Here]]\n")
    file.write(f"Score 0/{num}\n\n")
    file.write("## My Answers\n---\n")
