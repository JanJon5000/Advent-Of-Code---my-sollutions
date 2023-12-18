def prepare_string(string: str):
    string = string.replace('  ', ' ') #removing double spaces
    string = string.strip().split(' ')[2:] #removing the \n, spliting it into a list of nums
    string = [string[:string.index('|')], string[string.index('|')+1:]] #spliting it in half where the | sign is - into two lists in a list
    return string

def how_many_same(winning: list, have: list):
    counter = -1 #defining the counter variable - index of the later used pow function
    for element in winning:
        if element in have:
            counter += 1 #if the element of winning list is in the other list - its a point!
    
    if counter != -1:
        return pow(2, counter) #all of the points which you can get for a card besides 0 are powers of 2
    else:
        return 0

def main():
    counterOfTotalPoints = 0
    with open('Day4-Scratchcards-input.txt', 'r') as file:
        for _ in range(208):
            line = file.readline()
            line = prepare_string(line)
            counterOfTotalPoints += how_many_same(line[0], line[1])
    print(counterOfTotalPoints)

if __name__ == "__main__":
    main()