def get_input():
    with open("day5_input.txt") as f:
        cont = f.readlines()
        return [int(x.strip()) for x in cont if x.strip()]

def run_maze(maze):
    steps = 0
    i = 0
    while True:
        try:
            j = i
            i += maze[i]
            maze[j] += 1
            steps += 1
        except IndexError:
            return steps

def main():
    maze = get_input()
    print(run_maze(maze))

if __name__ == '__main__':
    main()