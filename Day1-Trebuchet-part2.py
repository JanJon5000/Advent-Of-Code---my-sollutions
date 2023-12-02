# def replaceSTR(string: str):
#     wordNumsList = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
#     occurance = {'blank':0}
#     while occurance != dict():
#         occurance = {word:string.find(word) for word in wordNumsList.keys() if string.find(word) != -1}
#         if occurance == dict():
#             break
#         wordToReplace = min(occurance, key=occurance.get)
#         string = string.replace(wordToReplace, str(wordNumsList[wordToReplace]), 1)
#     return string

# def FL(string: str):
#     ans = []
#     for char in string:
#         if char.isdigit():
#             ans.append(char)
#     return int(ans[0] + ans[-1])

def findFE(string: str):
    end = ''
    wordNumsList = {'one':"1", 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    for i in range(len(string)-1, -1, -1):
        if string[i].isdigit():
            end = string[i]
            break
        if string[i-2:i+1] in [i for i in list(wordNumsList.keys()) if len(i) == 3]:
            end = wordNumsList[string[i-2:i+1]]
            break
        if string[i-3:i+1] in [i for i in list(wordNumsList.keys()) if len(i) == 4]:
            end = wordNumsList[string[i-3:i+1]]
            break
        if string[i-4:i+1] in [i for i in list(wordNumsList.keys()) if len(i) == 5]:
            end = wordNumsList[string[i-4:i+1]]
            break

    front = ''
    for i in range(len(string)):
        if string[i].isdigit():
            front = string[i]
            break
        if string[i:i+3] in [i for i in list(wordNumsList.keys()) if len(i) == 3]:
            front = wordNumsList[string[i:i+3]]
            break
        if string[i:i+4] in [i for i in list(wordNumsList.keys()) if len(i) == 4]:
            front = wordNumsList[string[i:i+4]]
            break
        if string[i:i+5] in [i for i in list(wordNumsList.keys()) if len(i) == 5]:
            front = wordNumsList[string[i:i+5]]
            break
    return int(front + end)

with open('Day1-Trebuchet-input.txt', 'r') as file:
    calibrationSum = 0
    for _ in range(1000):
        calibrationSum += findFE(file.readline())
print(calibrationSum)