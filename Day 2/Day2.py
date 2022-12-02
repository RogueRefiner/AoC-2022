def main():
    file = 'input.txt'
    print(part1(file))
    print(part2(file))
    
def part1(file):
    sum = 0

    f = open(file,'r')
    lines = [l.strip() for l in f.readlines()]
    
    for line in lines:
        if(line[0] == 'A' and line[2] == 'Y'):
            sum += 6 + 2
        elif(line[0] == 'A' and line[2] == 'X'):
            sum += 3 + 1
        elif(line[0] == 'A'):
            sum += 0 + 3
            
        if(line[0] == 'B' and line[2] == "Z"):
            sum += 6 + 3
        elif(line[0] == 'B' and line[2] == "Y"):
            sum += 3 + 2
        elif(line[0] == 'B'):
            sum += 0 + 1

        if(line[0] == 'C' and line[2] == "X"):
            sum += 6 + 1
        elif(line[0] == 'C' and line[2] == "Z"):
            sum += 3 + 3
        elif(line[0] == 'C'):
            sum += 0 + 2 

    return sum

def part2(file):
    sum = 0

    f = open(file,'r')
    lines = [l.strip() for l in f.readlines()]

    for line in lines:
        if(line[0] == 'A' and line[2] == 'X'):
            sum += 0 + 3
        elif(line[0] == 'A' and line[2] == 'Y'):
            sum += 3 + 1
        elif(line[0] == 'A' and line[2] == 'Z'):
            sum += 6 + 2

        if(line[0] == 'B' and line[2] == 'X'):
            sum += 0 + 1
        elif(line[0] == 'B' and line[2] == 'Y'):
            sum += 3 + 2
        elif(line[0] == 'B' and line[2] == 'Z'):
            sum += 6 + 3

        if(line[0] == 'C' and line[2] == 'X'):
            sum += 0 + 2
        if(line[0] == 'C' and line[2] == 'Y'):
            sum += 3 + 3
        if(line[0] == 'C' and line[2] == 'Z'):
            sum += 6 + 1

    return sum

if __name__ == "__main__":
    main()
