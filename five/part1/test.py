import intcode_computer as comp
import sys

if __name__ == "__main__":
    #assert(len(sys.argv) == 2)
    #program = [int(x) for x in open(sys.argv[1]).read().split(",")]
    program = [int(x) for x in open("input.txt").read().split(",")]
    system_id = input("Please provide the ID of the system to test: ")
    comp.calcOutput(int(system_id), program)