import sys

class SpaceObject():

    def __init__(self, name, children=None):
        super().__init__()
        self._name = name
        self.orbitters = [] # children
        if children is not None:
            for child in children:
                self.addOrbitter(child)

    def addOrbitter(self, newOrbitter):
        assert(isinstance(newOrbitter, SpaceObject))
        self.orbitters.append(newOrbitter)

    def getName(self):
        return self._name

    def getNumberOfOrbitters(self):
        return len(self.orbitters)
    
    def getOrbitters(self):
        return self.orbitters

    # depth of node
    def getOrbits(self, amount):
        if self.orbitting is None:
            return amount
        return self.orbitting.getOrbits(amount+1)
    
    def getPossibleTransfers(self, origin):
        transfers = self.orbitters.append(self.orbitting)
        if origin in transfers:
            transfers.remove(origin)
        return transfers
    
    def __repr__(self):
        return "<{}>".format(self._name)

def getOrbits(space_objects):
    amount = 0

    for object in space_objects.values():
        amount += object.getOrbits(0)

    return amount

def getPath(origin, destination, path):
    path.append(origin)

    if origin.getName() == destination.getName():
        return True

    for node in origin.getOrbitters():
        if getPath(node, destination, path):
            return True
    
    path.pop()
    return False

def getPathBetween(root, origin, destination):

    # get paths from root to both nodes
    path1 = []
    path2 = []
    getPath(root, origin, path1)
    getPath(root, destination, path2)

    # get intersection
    i, j = 0, 0
    intersection = -1
    while i != len(path1) or j != len(path2):
        if i==j and path1[i] == path2[i]:
            i+=1
            j+=1
        else:
            intersection = j-1
            break

    path = list(reversed(path1[intersection:-1])) + path2[intersection+1:-1]
    return len(path)-1

if __name__ == "__main__":
    assert(len(sys.argv) == 2)

    with open(sys.argv[1]) as file:
        orbits = [x.rstrip() for x in file.readlines()]
 
    space_objects = {}

    for orbit in orbits:
        objects = orbit.split(")")
        orbitter = space_objects.get(objects[1], SpaceObject(objects[1]))
        center = space_objects.get(objects[0], SpaceObject(objects[0]))
        center.addOrbitter(orbitter)
        space_objects[center.getName()] = center
        space_objects[orbitter.getName()] = orbitter
    
    print(getPathBetween(space_objects.get("COM"), space_objects.get("YOU"), space_objects.get("SAN")))