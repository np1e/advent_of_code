import copy

def calcOutput(noun, verb, numbers):

    numbers[1] = noun
    numbers[2] = verb

    adress = 0
    for opcode in numbers[::4]:
        opcode = int(opcode)
        if opcode == 99:
            break
        elif opcode == 1:
            pos1 = numbers[adress+1]
            pos2 = numbers[adress+2]
            pos = numbers[adress+3]
            numbers[pos] = numbers[pos1] + numbers[pos2]
        elif opcode == 2:
            pos1 = numbers[adress+1]
            pos2 = numbers[adress+2]
            pos = numbers[adress+3]
            numbers[pos] = numbers[pos1] * numbers[pos2]
        else:
            break

        adress += 4
    
    return numbers[0]

def calcResult(input):

    for noun in range(0,100):
        for verb in range(0,100):
            output = calcOutput(noun, verb, copy.deepcopy(input))
            if output == 19690720:
                return 100 * noun + verb

if __name__ == '__main__':

    file = open("intcode.txt")
    input = [int(x) for x in file.read().rstrip().split(",")]
    

    print(calcResult(input))