from pprint import pprint
def input_operations(string: str):
    string = [i for i in string.split('\n') if i != ''] # out of a whole file, we make a list of lines without the blank ones (the second one is blank)
    instructions = string[0]; string = string[1:] # extracting the LR instructions out of the rest of nodes
    stringDICT = dict()
    for i in range(len(string)):
        stringDICT[string[i][:3]] = {'L':string[i][7:10], 'R':string[i][12:15]} # we amke a huge map of directions ad a huge dict in which every string has its right and left continuation
    return instructions, stringDICT # returning fixed input

def find_route(beg: str, end: str, map: dict, dirs: str):
    routeCounter = 0
    dirCounter = 0
    while beg != end: # follow the instructions while we are not in the end of our journey
        beg = map[beg][dirs[dirCounter]]
        routeCounter += 1
        if dirCounter < len(dirs)-1:
            dirCounter += 1
        else:
            dirCounter = 0
    return routeCounter

def main():
    with open('day8-input.txt', 'r') as file:
        input = input_operations(file.read())
        instructions = input[0]
        directions = input[1]
        ans = find_route('AAA', 'ZZZ', directions, instructions)     
        print(ans)

if __name__ == '__main__':
    main()