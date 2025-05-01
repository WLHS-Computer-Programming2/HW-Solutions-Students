from pathlib import Path


def problem_ten_one():
    path = Path("Unit3HW1\learning_python.txt")
    contents = path.read_text()
    print(contents)
    print("In a list...")
    lines = contents.splitlines()
    for line in lines:
        print(line)

def problem_ten_two():
    path = Path("Unit3HW1\learning_python.txt")
    contents = path.read_text()
    final_output = ''
    for line in contents.splitlines():
        final_output += f"{line.replace('Python','Rust')}\n"
    print(final_output)
    
    
def main():
    problem_ten_one()
    print("Replacing Python with Rust")
    print()
    problem_ten_two()
    



if __name__ == "__main__":
    main()