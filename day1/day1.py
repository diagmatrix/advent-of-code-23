""""Day 1 solution"""
NUMBERS = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']


def num_to_digit(digit):
    match digit:
        case "one":
            return str(1)
        case "two":
            return str(2)
        case "three":
            return str(3)
        case "four":
            return str(4)
        case "five":
            return str(5)
        case "six":
            return str(6)
        case "seven":
            return str(7)
        case "eight":
            return str(8)
        case "nine":
            return str(9)
        case _:
            return str(0)


if __name__ == "__main__":
    problem_input = open("input.txt", "r").readlines()  # Add input.txt in the directory
    total = 0
    for line in problem_input:
        digits = []
        for i, c in enumerate(line):
            if c.isdigit():
                digits.append(c)
            else:
                for num in NUMBERS:
                    if line[i:].startswith(num):
                        digits.append(num_to_digit(num))
        total += int(digits[0] + digits[-1])

    print(f'Answer: {total}')
