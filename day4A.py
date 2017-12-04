def main():
    with open("day4_input.txt") as f:
        lines = f.readlines()
    valid_lines = filter(is_valid, lines)
    print(len(list(valid_lines)))

def is_valid(line):
    line = line.strip().split()
    return len(line) == len(set(line))


if __name__ == '__main__':
    main()