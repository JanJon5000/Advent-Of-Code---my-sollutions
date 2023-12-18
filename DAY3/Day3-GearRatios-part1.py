def isNumAddable(l, string):
    num = ''
    nums = []
    for s in string:
        if s.isdigit():
            num += s
        elif num:
            nums.append(num)
            num = ''
    if num:
        nums.append(num)
    ans = 0
    for n in nums:
        ans += int(n)
    return ans

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