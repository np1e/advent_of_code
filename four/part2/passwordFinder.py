import sys

def hasDoubleDigits(pw):
    groups = [pw.count(ch) for ch in set(pw)]
    return any([x==2 for x in groups])

def checkNotDecreasingRule(pw):
    if len(pw) != 6 or any([pw[i] > pw[i+1] for i in range(5)]):
        return False
    return True

def getCriteriaMatch(pw):
    # rules
    # 1. six digit
    # 2. in range
    # 3. Two adjacent values are the same
    # 4. left-to-right the digits never decrease

    if checkNotDecreasingRule(str(pw)) and hasDoubleDigits(str(pw)):
        return 1

    return 0

if __name__ == "__main__":

    input = "input.txt"
    pw_from, pw_to = map(int, open(input).read().split("-"))
    #assert(len(sys.argv) == 2)
    #pw_from, pw_to = map(int, open(sys.argv[1]).read().split("-"))
    amount = sum([getCriteriaMatch(str(pw)) for pw in range(pw_from, pw_to+1)])
    print(amount)
