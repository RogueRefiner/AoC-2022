def main():
    file =  "input.txt"
    print(part1(file))
    print(part2(file))

def part1(file):
    sum = 0
    with open(file, 'r') as f:
        lines = [l.strip() for l in f.readlines()]
        for line in lines:
            half  = len(line) // 2

            res = []
            for element in line[:half]:
                if(element.islower()):
                    res.extend(ord(num) - 96 for num in element)
                else:
                    res.extend(ord(num) - 38 for num in element)
                    
            res2 = []
            for element in line[half:]:
                if(element.islower()):
                    res2.extend(ord(num) - 96 for num in element)
                else:
                    res2.extend(ord(num) - 38 for num in element)
                       
            for x in res:
                if res2.__contains__(x):
                    sum += x
                    break
    return sum

def part2(file):
    sum = 0
    counter = 1

    with open(file, 'r') as f:
        lines = [l.strip() for l in f.readlines()]
        res = []
        res2 = [] 
        res3 = []

        for line in lines:
            if(counter == 1):
                for element in line:
                    if(element.islower()):
                        res.extend(ord(num) - 96 for num in element)
                    else:
                        res.extend(ord(num) - 38 for num in element)
            if(counter == 2):
                for element in line:
                    if(element.islower()):
                        res2.extend(ord(num) - 96 for num in element)
                    else:
                        res2.extend(ord(num) - 38 for num in element)
            if(counter == 3):
                for element in line:
                    if(element.islower()):
                        res3.extend(ord(num) - 96 for num in element)
                    else:
                        res3.extend(ord(num) - 38 for num in element)
            
            if(counter == 3):
                counter = 0
                for x in res:
                    if(res2.__contains__(x) and res3.__contains__(x)):
                        sum += x
                        break
                res = []
                res2 = []
                res3 = []    

            counter += 1
    return sum

if __name__ == "__main__":
    main()
