# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])

def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]

def find_mismatch(text):
    opening_brackets_stack = []
    for i, next_char in enumerate(text):
        if next_char in "([{":
            opening_brackets_stack.append(Bracket(next_char, i + 1))
        if next_char in ")]}":
            if not opening_brackets_stack:
                return i + 1
            top = opening_brackets_stack.pop()
            if not are_matching(top.char, next_char):
                return i + 1
    if opening_brackets_stack:
        top = opening_brackets_stack.pop()
        return top.position
    return "Success"

def main():
    source = input("Choose input (F for file, I for keyboard): ")
    if source == "F":
        file_name = input("Enter file name: ")
        with open(file_name, "r") as f:
            text = f.read().strip()
    elif source == "I":
        text = input("Enter brackets: ")
    else:
        print("Invalid input.")
        return
    
    mismatch = find_mismatch(text)
    if isinstance(mismatch, int):
        print(mismatch)
    else:
        print(mismatch)

if __name__ == "__main__":
    main()