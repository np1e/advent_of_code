import sys

def checkAdjacencyRule(pw):
    
    for i in range(len(pw[:-1])):
        if pw[i] == pw[i+1]:
            return True
    return False

def checkNotDecreasingRule(pw):
    cur_min = int(pw[0])
    for c in map(int, pw[1:]):
        if c < cur_min:
            return False

        cur_min = c
            
    return True

def getNumberOfPasswords(pwRange):
    # rules
    # 1. six digit
    # 2. in range
    # 3. Two adjacent values are the same
    # 4. left-to-right the digits never decrease
    amount = 0

    for pw in range(pwRange[0], pwRange[1]+1):
        if checkAdjacencyRule(str(pw)) and checkNotDecreasingRule(str(pw)):
            amount += 1

    return amount

if __name__ == "__main__":
    
    pwRange = [int(x) for x in open(sys.argv[1]).read().split("-")]
    amount = getNumberOfPasswords(pwRange)
    print(amount)
