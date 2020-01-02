import math
import numpy as np
import sys
import itertools

def get_coord(start, dir, length):
    if dir == 'R':
        coord = [start[0] + length, start[1]]
    if dir == 'L':
        coord = [start[0] - length, start[1]]
    if dir == 'U':
        coord = [start[0], start[1] + length]
    if dir == 'D':
        coord = [start[0], start[1] - length]

    return np.array(coord)

def perp(a,b = np.array([])):
    if b.size == 0:
        b = np.empty_like(a)
        b[0] = -a[1]
        b[1] = a[0]
        return b

    return np.dot(perp(a), b)

def get_intersect(A, B, C, D):
    u = B - A
    v = D - C
    w = A - C
    D = perp(u,v)

    # parallel or same line 
    # coincidence is irrelevant so it is not checked
    if D == 0:
        return None

    t = perp(u, w) / D
    s = perp(v, w) / D
    if 0 <= t <= 1 and 0 <= s <= 1:
        return A + s * u
    
    return None


def get_distance(wire_one, wire_two):
    coord1_1 = coord2_1 = np.array([0.,0.])
    distances = []
    steps = {}

    steps_wireone = 0
    steps_wiretwo = 0
    for dir1 in wire_one:
        coord1_2 = get_coord(coord1_1, dir1[0], dir1[1])
        steps_wireone += dir1[1]
        print("wire1:", steps_wireone)
        for dir2 in wire_two:
            coord2_2 = get_coord(coord2_1, dir2[0], dir2[1])
            steps_wiretwo += dir2[1]
            print("wire2:", steps_wiretwo)
            point = get_intersect(coord1_1, coord1_2, coord2_1, coord2_2)

            if point is not None and not np.array_equal(point, [0., 0.]):
                print(point)
                
                if dir1[0] == "U":
                    steps_wireone -= coord1_1[1] - point[1]
                elif dir1[0] == "D":
                    steps_wireone -= point[1] - coord1_2[1]
                elif dir1[0] == "L":
                    steps_wireone -= point[0] - coord1_2[0]
                elif dir1[0] == "R":
                    steps_wireone -= coord1_1[0] - point[0]

                if dir2[0] == "U":
                    steps_wiretwo -= coord2_1[1] - point[1]
                elif dir2[0] == "D":
                    steps_wiretwo -= point[1] - coord2_2[1]
                elif dir2[0] == "L":
                    steps_wiretwo -= point[0] - coord2_2[0]
                elif dir2[0] == "R":
                    steps_wiretwo -= coord2_1[0] - point[0]

                print("steps:", steps_wireone + steps_wiretwo)
                distances.append(abs(point[0]) + abs(point[1]))
                steps[tuple(point)] = steps_wireone + steps_wiretwo
            
            coord2_1 = coord2_2
        steps_wiretwo = 0
        coord1_1 = coord1_2
        coord2_1 = np.array([0.,0.])

    return min(distances)

if __name__ == '__main__':    
    file = open("example.txt")
    #file = open(sys.argv[1])

    wire_one = [(x[:1], float(x[1:])) for x in file.readline().strip().split(",")]
    wire_two = [(x[:1], float(x[1:])) for x in file.readline().strip().split(",")]

    distance = get_distance(wire_one, wire_two)



