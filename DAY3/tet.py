def isNumAddable(l: list, string: str):
    stringSum = 0
    wholeNums = [x for x in string.split('.') if x != '']
    for num in wholeNums:
        x = ''.join([x for x in num if not x.isdigit()])
        if x != '':
            for char in x:
                if num.index(char) != 0 and num.index(char) != len(num)-1:
                    replacement = num.split(char)
                    index = wholeNums.index(num)
                    del wholeNums[wholeNums.index(num)]
                    for element in replacement[::-1]:
                        wholeNums.insert(index, element)
                else:
                    replacement = ''.join([i for i in num if i.isdigit()])
                    wholeNums[wholeNums.index(num)] = replacement
    wholeNums = [''.join(num) for num in wholeNums if ''.join(num) != '']
    for element in wholeNums:
        aroundIt = ''.join([l[l.index(string)-1][i] for i in range(string.find(element)-1, string.find(element)+len(element)+1) if i > -1 and i < len(string) if l.index(string)-1 > -1])
        aroundIt += ''.join([string[i] for i in range(string.find(element)-1, string.find(element)+len(element)+1) if i > -1 and i < len(string)])
        try:
            aroundIt += ''.join([l[l.index(string)+1][i] for i in range(string.find(element)-1, string.find(element)+len(element)+1) if i > -1 and i < len(string) if l.index(string)-1 < len(l)])
        except:
            pass
        aroundIt = aroundIt.replace('.', '')
        for i in '1234567890':
            aroundIt = aroundIt.replace(i, '')
        if aroundIt != '':
            stringSum += int(element)
    return stringSum

sample = [
    '467..114..',
    '...*......',
    '..35..633.',
    '......#...',
    '617*......',
    '.....+.58.',
    '..592.....',
    '......755.',
    '...$.*....',
    '.664.598..'
]

input = []
anssum = 0
with open("Day3-GearRatios-input.txt", 'r') as file:
    for _ in range(140):
        string = file.readline().replace('\n', '')
        input.append(string)

for line in input:
    anssum += isNumAddable(input, line)
print(anssum)