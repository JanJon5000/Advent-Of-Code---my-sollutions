def selectFL(string: str):
    ans = []
    for char in string:
        numsList = '1234567890'
        if char in numsList:
            ans.append(char)
    return int(ans[0] + ans[-1])

with open('Day1-Trebuchet-input.txt', 'r') as file:
    calibrationSum = 0
    for _ in range(1000):
        calibrationSum += selectFL(file.readline())
print(calibrationSum)