import re

def main():
    file = "input.txt"
    print(part1(file))
    print(part2(file))

def getLists(line, part_1):
        elf1 = []
        elf2 = []
        numbers = re.findall("[0-9]+", line)

        elf1.clear()
        elf2.clear()
            
        elf1.extend(range(int(numbers[0]), int(numbers[1]) + 1))
        elf2.extend(range(int(numbers[2]), int(numbers[3]) + 1 ))

        ret = comp(elf1, elf2, part_1)
        return ret

def comp(elf1, elf2, part_1):
    ret = 0 
    if(part_1):
        if(all(item in elf1 for item in elf2) or (all(item in elf2 for item in elf1))):
            ret += 1
    else:
        if(any(item in elf1 for item in elf2) or (all(item in elf2 for item in elf1))):
            ret += 1
    return ret
    
def part1(file):
    sum = 0
    part_1 = True
    with open(file, 'r') as f:
        lines = [l.strip() for l in f.readlines()]

        for line in lines:
           sum += getLists(line, part_1)
        return sum            
        
def part2(file):
    sum = 0
    part_1 = False
    with open(file, 'r') as f:
        lines = [l.strip() for l in f.readlines()]
        
        for line in lines:
            sum += getLists(line, part_1)    
        return sum

if __name__ == "__main__":
    main()