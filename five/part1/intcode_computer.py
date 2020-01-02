import copy
import sys

def get_pos_nums(num):
    pos_nums = []
    while num != 0:
        pos_nums.append(num % 10)
        num = num // 10
    return pos_nums

def get_value(array, index, default):
    try:
        return array[index]
    except IndexError:
        return default

def calcOutput(input, instructions):

    log_file = open("intcode_computer.log", "w+")

    opcodes = {99: 0, 1: 4, 2: 4, 3: 2, 4: 2, 5: 3, 6: 3, 7: 4, 8: 4}
    instruction_pointer = 0
    while instruction_pointer < len(instructions)-2:
        instruction = get_pos_nums(int(instructions[instruction_pointer])) # e.g. [1,0,0,2]
        opcode = int((str(get_value(instruction, 1, 0)) 
            + str(get_value(instruction, 0, 0))).strip("0"))
        mode_one = get_value(instruction, 2, 0)
        mode_two = get_value(instruction, 3, 0)
        mode_three = get_value(instruction, 4, 0)
        
        log_file.write("Instruction pointer: {} || ".format(instruction_pointer))

        param1 = instructions[instructions[instruction_pointer+1]] if mode_one == 0 else instructions[instruction_pointer+1]
        param2 = instructions[instructions[instruction_pointer+2]] if mode_two == 0 else instructions[instruction_pointer+2]
        pos = instructions[instruction_pointer+3]

        if opcode == 99:
            break
        elif opcode == 1:
            instructions[pos] = param1 + param2
            log_file.write("Adding {} and {} and writing it to {}\n".format(param1, param2, pos))
        elif opcode == 2:
            instructions[pos] = param1 * param2
            log_file.write("Multiplying {} and {} and writing it to {}\n".format(param1, param2, pos))
        elif opcode == 3:
            # take input and save it to position adress+1
            instructions[instructions[instruction_pointer+1]] = input    
            log_file.write("Writing {} to {}\n".format(input, instructions[instruction_pointer+1]))
        elif opcode == 4:
            # ouput the value at position adress+1
            output = instructions[instructions[instruction_pointer+1]] if mode_one == 0 else instructions[instruction_pointer+1]
            if output:
                print("error at instruction {}:".format(instruction_pointer))
            print(output)
            log_file.write("Code: {}\n".format(output))
        elif opcode == 5:
            if param1:
                instruction_pointer = param2
                continue
        elif opcode == 6:
            if not param1:
                instruction_pointer = param2
                continue
        elif opcode == 7:
            instructions[pos] = 1 if param1 < param2 else 0
        elif opcode == 8:
            instructions[pos] = 1 if param1 == param2 else 0
        else:
            break

        instruction_pointer += opcodes.get(opcode, 0)
    