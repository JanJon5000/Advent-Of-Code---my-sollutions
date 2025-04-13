from pprint import pprint
def input_operations(input: str):
    return [[int(x) for x in line.split(' ')] for line in input.split('\n')]

def dx(f: list):
    return [f[i+1]-f[i] for i in range(0, len(f)-1)]

def predict_next(l: list):
    copy = dx(l)
    ans = copy[-1] + l[-1]
    while len(set(copy)) != 1:
        copy = dx(copy)
        ans += copy[-1]
    return ans

def main():
    ans = 0
    with open('day9-input.txt', 'r') as file:
        input = input_operations(file.read())
        for line in input:
            ans += predict_next(line)
    print(ans)

if __name__ == '__main__':
    main()