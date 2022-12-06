FILE = "input.txt"

def solve(n):
    with open(FILE) as f:
        line = f.read()
        for i in range(len(line)):
            if(len(set(line[i:i+n]))) == n:
                return i + n

if __name__ == "__main__":
    print(solve(4))
    print(solve(14))
    