def input_operations(input: str): #only input changed B)
    input = [x.split(' ') for x in input.split('\n')]
    for i in range(2): input[i] = [x for x in input[i] if x != '']
    input = {int(''.join(input[0][1:])):int(''.join(input[1][1:]))}
    return input

def race_wins(races: dict):
    ans = 1
    for time in races:
        distance = races[time]
        for velocity in range(1, time-1):
            if velocity*(time-velocity) > distance:
                ans*=(time+1-2*velocity)
                break
    return ans




def main():
    with open('day6-input.txt', 'r') as file:
        races = input_operations(file.read())
        print(race_wins(races))

if __name__ == '__main__':
    main()