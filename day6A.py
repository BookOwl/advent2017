import functools
import math
def pick_bank(banks):
    @functools.cmp_to_key
    def comp(a, b):
        if a[1] == b[1]:
            if a[0] < b[0]:
                return 1
            else:
                return -1*(a[0] > b[0])
        else:
            if a[1] > b[1]:
                return 1
            else:
                return -1
    return max(enumerate(banks), key=comp)[0]

def distribute(banks):
    index = pick_bank(banks)
    new_banks = banks[:]
    blocks = new_banks[index]
    new_banks[index] = 0
    change = math.ceil(blocks/len(banks))
    i = 1
    while blocks:
        new_banks[(index+i)%len(banks)] += 1
        blocks -= 1
        i += 1
    return new_banks

def realloc(banks):
    seen = [banks[:]]
    while True:
        banks = distribute(banks)
        if banks in seen:
            return len(seen)
        else:
            seen.append(banks[:])

def main():
    banks = [int(i) for i in input().split()]
    i = realloc(banks)
    print(i)

if __name__ == '__main__':
    main()
    # 4 10 4 1 8 4 9 14 5 1 14 15 0 15 3 5
