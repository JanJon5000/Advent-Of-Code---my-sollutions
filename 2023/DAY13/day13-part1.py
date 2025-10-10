from pprint import pprint
def analize(pattern: list) -> int:
    rowNumber = len(pattern)
    colNumber = len(pattern[0])
    for bitweenRow in range(1, rowNumber):
        begin = min(bitweenRow, rowNumber-bitweenRow)
        reference = pattern[bitweenRow-begin:bitweenRow]
        reflection = pattern[bitweenRow:bitweenRow+begin][::-1]
        if(reference == reflection):
            return 100 * bitweenRow
    for bitweenCol in range(1, colNumber):
        begin = min(bitweenCol, colNumber-bitweenCol)
        reference = [line[bitweenCol-begin:bitweenCol] for line in pattern]
        reflection = [line[bitweenCol:bitweenCol+begin][::-1] for line in pattern]
        if reference == reflection:
            return bitweenCol
    return 0

def main():
    sum = 0
    with open("day13-input.txt", "r") as file:
        sum = 0
        pattern = []
        for _ in range(1312):
            line = file.readline()
            if('.' not in line and '#' not in line):
                sum += analize(pattern)
                pattern = []
            else:
                pattern.append(line.strip())
    print(sum)

if __name__ == "__main__":
    main()