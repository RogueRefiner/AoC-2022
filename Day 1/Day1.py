def main():
    file = 'input.txt'
    print(part1(file))
    print(part2(file))

def part1(file):
    list = getSortedList(file)
    return list[0]

def part2(file):
    list = getSortedList(file)
    return list[0] + list[1] + list[2]

def getSortedList(file):
    sum = 0
    list= []
    
    f = open(file,'r')
    lines = f.readlines()

    for line in lines:
        if(line != '\n'):
            sum += int(line)
        else:
            list.append(sum)
            sum = 0
    
    list.sort(reverse = True)

    return list


if __name__ == "__main__":
    main()
