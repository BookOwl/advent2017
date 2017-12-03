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

def sum_neighbors(g, pos):
    return sum(g.get(p, 0) for p in neighbors(pos))

def neighbors(pos):
    x, y = pos
    return ((x+i, y+j) for i in range(-1, 2) for j in range(-1, 2))

def generate_spiral(n):
    g = {}
    x = 1
    direction = EAST
    pos= (0, 0)
    s = 1
    while True:
        for i in range(2):
            for j in range(s):
                q = sum_neighbors(g, pos) or 1
                if q > n:
                    return q
                g[pos] = q
                pos = move(pos, direction)
            direction = (direction+1)%4
        s += 1

def main():
    n = int(input())
    g = generate_spiral(n)
    print(g)
    

if __name__ == '__main__':
    main()