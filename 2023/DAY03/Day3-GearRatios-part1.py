from pprint import pprint
def input_operations(input: str):
     input = input.split('\n')
     return input
    
def find_the_num(cord: int, string: str):
    ans = string[cord]
    cords = [cord]
    i = cord - 1
    while i > -1 and string[i] in '1234567890':
        if string[i].isdigit():
            ans = string[i] + ans
            cords.append(i)
            i -= 1

    i = cord + 1
    while i < len(string) and string[i] in '1234567890':
        ans += string[i]
        cords.append(i)
        i += 1
    return ans, cords

def nums_near_symbol(input: list):
    ans = []
    directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    dontCheck = []
    for x in range(len(input)):
        for y in range(len(input[x])):
            if input[x][y] not in '.1234567890':
                nearbySQR = dict()
                for d in directions:
                    if x + d[0] > -1 and x + d[0] < len(input) and y + d[1] > -1 and y + d[1] < len(input[x]):
                        try:
                            nearbySQR(input[x + d[0]][y + d[1]]).append([x + d[0], y + d[1]])
                        except:
                            nearbySQR[input[x + d[0]][y + d[1]]] = [x + d[0], y + d[1]]
                nearbySQR = {k:nearbySQR[k] for k in nearbySQR.keys() if k in '0123456789'}
                valuesChecked = []
                for digit in nearbySQR.keys():
                    cords = find_the_num(nearbySQR[digit][1], input[nearbySQR[digit][0]])[1]
                    cords = [[nearbySQR[digit][0], c] for c in cords]
                    value = find_the_num(nearbySQR[digit][1], input[nearbySQR[digit][0]])[0]
                    if nearbySQR[digit] not in dontCheck and value not in valuesChecked:
                        try:
                            if value != ans[-1] and value != ans[-2] and value!= ans[-3]:
                                ans.append(value)              
                        except:                       
                            if value not in ans:                                   
                                ans.append(value)                                                                                                                                          
                    pprint(nearbySQR)
    return sum(([int(a) for a in ans]))

def main():
    with open('Day3-GearRatios-input.txt', 'r') as file:
    #     input = input_operations(file.read())
    #     print(nums_near_symbol(input))
        for line in input_operations(input=file.read()):
            line = [x for x in line]
            line = ''.join([f'  {x}' for x in line])
            print(line)
if __name__ == '__main__':
    main()