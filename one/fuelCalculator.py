import math

def calcFuel(input):
    fuel = math.floor(input / 3) - 2
    return fuel

if __name__ == "__main__":
    file = open("input.txt")
    fuel_sum = 0

    for line in file.readlines():
        mass = int(line)
        fuel = calcFuel(mass)
        while fuel > 0:
            fuel_sum += fuel
            fuel = calcFuel(fuel)
        
    print(fuel_sum)
