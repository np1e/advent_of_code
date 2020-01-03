import sys

class SpaceObject():

    def __init__(self, name):
        super().__init__()
        self._name = name
        self.orbitters = []
        self.orbitting = None

    def addOrbitter(self, newOrbitter):
        self.orbitters.append(newOrbitter)

    def addOrbitting(self, orbitting):
        self.orbitting = orbitting

    def getName(self):
        return self._name

    def getNumberOfOrbitters(self):
        return len(self.orbitters)

    def getOrbitting(self):
        if self.orbitting:
            return self.orbitting
        return None

    def getOrbits(self, amount):
        if self.orbitting is None:
            return amount
        return self.orbitting.getOrbits(amount+1)
    
    def __repr__(self):
        return "<{}>".format(self._name)

def getOrbits(space_objects):
    amount = 0

    for object in space_objects.values():
        amount += object.getOrbits(0)

    return amount

if __name__ == "__main__":
    assert(len(sys.argv) == 2)

    with open(sys.argv[1]) as file:
        orbits = [x.rstrip() for x in file.readlines()]

    print(len(orbits))    
    space_objects = {}

    for orbit in orbits:
        objects = orbit.split(")")
        orbitter = space_objects.get(objects[1], SpaceObject(objects[1]))
        center = space_objects.get(objects[0], SpaceObject(objects[0]))
        center.addOrbitter(orbitter)
        orbitter.addOrbitting(center)
        space_objects[center.getName()] = center
        space_objects[orbitter.getName()] = orbitter
    
    print(getOrbits(space_objects)) 