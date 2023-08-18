def reverse_lines(input_lines):
    reversed_lines = []

    for line in input_lines:
        reversed_line = line.strip()[::-1]
        reversed_lines.append(reversed_line)

    return reversed_lines

def main():
    input_lines = []
    while True:
        try:
            line = input()
            input_lines.append(line)
        except EOFError:
            break

    reversed_lines = reverse_lines(input_lines)

    for line in reversed_lines:
        print(line)

if __name__ == "__main__":
    main()
