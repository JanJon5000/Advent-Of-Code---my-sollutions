from pprint import pprint
def input_operations(string: str):
    string = [i for i in string.split('\n') if i != ''] # out of a whole file, we make a list of lines without the blank ones (the second one is blank)
    instructions = string[0]; string = string[1:] # extracting the LR instructions out of the rest of nodes
    stringDICT = dict()
    for i in range(len(string)):
        stringDICT[string[i][:3]] = {'L':string[i][7:10], 'R':string[i][12:15]} # we amke a huge map of directions ad a huge dict in which every string has its right and left continuation
    return instructions, stringDICT # returning fixed input

def bigest_divisor(a: int, b: int):
    while a != b:
        if a > b:
            a -= b
        elif a < b:
            b -= a
    return a

def smallest_multiple(a: int, b: int):
    return a*b/bigest_divisor(a, b)

def find_route(map: dict, dirs: str):
    routeCounter = []
    beg = [k for k in map.keys() if k[-1] == 'A']
    for start in beg:
        n = 0
        dirCounter = 0
        while start[-1] != 'Z':
            start = map[start][dirs[dirCounter]]
            n += 1
            if dirCounter < len(dirs)-1:
                dirCounter += 1
            else:
                dirCounter = 0
        routeCounter.append(n)
    ans = smallest_multiple(routeCounter[0], routeCounter[1])
    for i in routeCounter:
        ans = smallest_multiple(ans, i)
    return ans

def main():
    with open('day8-input.txt', 'r') as file:
        input = input_operations(file.read())
        instructions = input[1]
        directions = input[0]
        ans = find_route(instructions, directions)   
        print(ans)

if __name__ == '__main__':
    main()