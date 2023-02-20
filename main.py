# python3


from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text, start=1):
        # add bracket to array
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i))

        if next in ")]}" and not are_matching(opening_brackets_stack.pop().char, next):
            return i
    return "Success"


def main():
    input_choice = input("[(F)ile/(I)nput]: ")
    if "F" in input_choice:
        pass
    elif "I" in input_choice:
        print(find_mismatch(input()))
    else:
        print("Invalid input.")


if __name__ == "__main__":
    main()