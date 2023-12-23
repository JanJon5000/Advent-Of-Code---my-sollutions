from pprint import pprint
def input_operations(input: str):
    input = [line.split(' ') for line in input.split('\n')]
    input = [{'hand':i[0], 'bid':int(i[1]), 'type':None} for i in input] # making every hand a dictionary - it will be easier to sort

    # giving every hand a type
    for num in range(len(input)):
        uniqueChars = set([x for x in input[num]['hand']])
        chars = tuple(uniqueChars)
        if len(uniqueChars) == 1:
            input[num]['type'] = 'Five of a kind'
        elif len(uniqueChars) == 2:
            if input[num]['hand'].count(chars[0]) == 2 or input[num]['hand'].count(chars[1]) == 2:
                input[num]['type'] = 'Full house'
            else:
                input[num]['type'] = 'Four of a kind'
        elif len(uniqueChars) == 3:
            if input[num]['hand'].count(chars[0]) == 3 or input[num]['hand'].count(chars[1]) == 3 or input[num]['hand'].count(chars[2]) == 3:
                input[num]['type'] = 'Three of a kind'
            else:
                input[num]['type'] = 'Two pair'
        elif len(uniqueChars) == 4:
            input[num]['type'] = 'One pair'
        else:
            input[num]['type'] = 'High card'

    return input

def camelSort():
    pass

def main():
    with open('day7-input.txt', 'r') as file:
        pprint(input_operations(file.read()))

if __name__ == '__main__':
    main()