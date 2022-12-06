FILE = "input.txt"
PART1 = True
#TODO parser for instead of hard coding stack

def part1(stacks):
    with open(FILE) as f:
        lines = [l.strip() for l in f.readlines()]
        for line in lines:
                m = map(int, line.replace('move ', '').replace(' from ', ' ').replace(' to ', ' ').split(' '))
                crates, _from, to = m
                for _ in range(crates):
                    stacks[to].append(stacks[_from].pop())
                    crates -= 1

        ret = []
        for i in stacks:
            ret.append(stacks[i][len(stacks[i]) - 1])   
        ret = ''.join([str(item) for item in ret]) 
    return ret


def part2(stacks):
    with open(FILE) as f:
        lines = [l.strip() for l in f.readlines()]
        for line in lines:
            m = map(int, line.replace('move', '').replace(' from', ' ').replace(' to', ' ').split(' '))
            crates, _from, to = m  
            stacks[to] += stacks[_from][-1*crates:]
            stacks[_from] = stacks[_from][:(-1*crates)]
    
        ret = []
        for i in stacks:
            ret.append(stacks[i][len(stacks[i]) - 1])    
        ret = ''.join([str(item) for item in ret]) 
    return ret

def main():
    
    stacks = {
        1: 'B V S N T C H Q'.split(),
        2: 'W D B G'.split(),
        3: 'F W R T S Q B'.split(),
        4: 'L G W S Z J D N'.split(),
        5: 'M P D V F'.split(),
        6: 'F W J'.split(),
        7: 'L N Q B J V'.split(),
        8: 'G T R C J Q S N'.split(),
        9: 'J S Q C W D M'.split()
    } 

    if(PART1):
        print(part1(stacks))
    else:
        print(part2(stacks))
    

if __name__ == "__main__":
    main()
