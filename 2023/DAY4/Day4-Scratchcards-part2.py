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
    dictOfCards = {i:1 for i in range(1, 209)}
    with open('Day4-Scratchcards-input.txt', 'r') as file:
        for _ in range(208):
            line = file.readline()
            line = prepare_string(line)
            print(line)
            cardsWon = which_copies_won(line[0][0], line[0][1], line[1])

            for element in cardsWon:
                dictOfCards[element] += dictOfCards[line[1]]

    print(sum(dictOfCards.values()))

if __name__ == "__main__":
    main()