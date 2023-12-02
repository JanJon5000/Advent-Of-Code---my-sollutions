from pprint import pprint
def isGamePossible(listOfGames: list):
    for i in range(len(listOfGames)):
        listOfGames[i] = (listOfGames[i]['red'] <= 12 and listOfGames[i]['green'] <= 13 and listOfGames[i]['blue'] <= 14)
    return not (False in listOfGames)
def prepareString(string: str):
    string = string.replace('\n', '')
    string = string.replace(' ', '')
    gameNum = int(''.join([x for x in string[:string.find(':')] if x.isdigit()]))
    string = string.replace(string[:string.find(':')+1], '')
    string = string.split(';')
    string = [i.split(',') for i in string]
    stringDict = []
    for gameList in string:
        stringDict.append(dict())
        for element in gameList:
            borderIndex = [element.find(x) for x in ['blue', 'green', 'red'] if element.find(x) != -1][0]
            stringDict[-1][element[borderIndex:]] = int(element[:borderIndex])
            for key in ['blue', 'green', 'red']:
                if key not in stringDict[-1].keys():
                    stringDict[-1][key] = 0
    return gameNum, stringDict

sumOfGames = 0
with open("Day2-CubeConundrum-input.txt", 'r') as file:
    for _ in range(100):
        input = file.readline()
        if isGamePossible(prepareString(input)[-1]):
            sumOfGames += prepareString(input)[0]
print(sumOfGames)