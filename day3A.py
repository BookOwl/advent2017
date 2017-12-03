EAST, NORTH, WEST, SOUTH = range(4)

def move(pos, dir):
    x, y = pos
    if dir == EAST:
        return x + 1, y
    if dir == WEST:
        return x - 1, y
    if dir == NORTH:
        return x, y + 1
    if dir == SOUTH:
        return x, y - 1

def generate_spiral(n):
    g = {}
    x = 1
    direction = EAST
    pos= (0, 0)
    s = 1
    while x <= n:
        for i in range(2):
            for j in range(s):
                g[x] = pos
                pos = move(pos, direction)
                x += 1
            direction = (direction+1)%4
        s += 1
    return g

def num_steps_to(pos):
    x, y = pos
    return abs(x) + abs(y)

def main():
    n = int(input())
    g = generate_spiral(n)
    print(num_steps_to(g[n]))
    

if __name__ == '__main__':
    main()