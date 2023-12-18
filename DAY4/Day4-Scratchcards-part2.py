from pprint import pprint
def prepare_string(string: str):
    string = string.replace('  ', ' ') #removing double spaces
    string = string.strip().split(' ') #removing the \n, spliting it into a list of nums
    string = [i for i in string if i != '']
    num = int(string[1].replace(':', ''))
    string = [string[:string.index('|')], string[string.index('|')+1:]] #spliting it in half where the | sign is - into two lists in a list
    string[0] = string[0][2:]
    return string, num

def which_copies_won(winning: list, have: list, numberOfCard: int):
    counter = 0
    for element in winning:
        if element in have:
            counter += 1
    ans = [i for i in range(numberOfCard + 1, numberOfCard + counter + 1)]
    return ans

def main():
    ans = [
        'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
        'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
        'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
        'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
        'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
        'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'
    ]

    dictOfCards = {i:1 for i in range(1, 209)}
    with open('Day4-Scratchcards-input.txt', 'r') as file:
        for _ in range(208):
            line = file.readline()
            line = prepare_string(line)
            print(line)
            cardsWon = which_copies_won(line[0][0], line[0][1], line[1])

            for element in cardsWon:
                dictOfCards[element] += dictOfCards[line[1]]

            # print(f'numer karty: {line[1]}')
            # print(f'wining nums: {line[0][0]} \nhave nums: {line[0][1]}')
            # print(f'wygrane kopie kart {cardsWon}\nich ilość: {ilekart}')

    pprint(sum(dictOfCards.values()))

if __name__ == "__main__":
    main()