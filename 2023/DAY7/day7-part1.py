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

def sort_criteria(x: list):
    # we change the hand to a base 15 number and compare it
    # T -> A
    # J -> B
    # Q -> C
    # K -> D
    # A -> E - need to be performend first as it is the only char actually used to present numbers in the base 15
    ans = x['hand'].replace('A', 'E').replace('K', 'D').replace('Q', 'C').replace('J', 'B').replace('T', 'A')
    return int(ans, 15)

def camel_sort(input: list):
    names = ['Four of a kind', 'Full house', 'Three of a kind', 'Two pair', 'One pair', 'High card']
    SevenLists = [[element for element in input if element['type'] == 'Five of a kind']]
    for n in names:
        lToAppend = [element for element in input if element['type'] == n]
        lToAppend.sort(key=sort_criteria, reverse=True)
        SevenLists.append(lToAppend)
    ans = []
    for l in SevenLists:
        ans.extend(l)
    return ans

def camel_sum(x: list):
    ans = 0
    rank = 1000
    for camel in x:
        ans += camel['bid']*rank
        rank -= 1
    return ans


def main():
    with open('day7-input.txt', 'r') as file:
        input = input_operations(file.read())
        input = camel_sort(input)
        print(camel_sum(input))

if __name__ == '__main__':
    main()