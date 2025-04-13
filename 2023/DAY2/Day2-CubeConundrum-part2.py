def prepareString(string: str):
    string = string.replace('\n', '')
    string = string.replace(' ', '')
    string = string.replace(';', ',')
    string += ','
    string = string.replace(string[:string.find(':')+1], '')
    stringDict = {'blue':[0], 'green':[0], 'red':[0]}
    while string != '':
        num = int(''.join([x for x in string[:string.find(',')] if x.isdigit()]))
        stringDict[''.join([x for x in string[:string.find(',')] if not x.isdigit()])].append(num)
        string = string.replace(string[:string.find(',')+1], '', 1)
    stringDict = {key:max(stringDict[key]) for key in list(stringDict.keys())}
    mult = 1
    for val in list(stringDict.values()):
        mult *= val
    return mult

sumOfGames = 0
with open('Day2-CubeConundrum-input.txt', 'r') as file:
    for _ in range(100):
        sumOfGames += prepareString(file.readline())
print(sumOfGames)