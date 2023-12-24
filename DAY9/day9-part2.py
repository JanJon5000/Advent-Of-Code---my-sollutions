def input_operations(input: str):
    return [[int(x) for x in line.split(' ')] for line in input.split('\n')]

def dx(f: list):
    return [f[i]-f[i+1] for i in range(0, len(f)-1)]

def predict_next(l: list):
    print(l)
    copy = dx(l)
    print(copy)
    ans = copy[0] + l[0]
    while len(set(copy)) != 1:
        copy = dx(copy)
        print(copy)
        ans += copy[0]
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