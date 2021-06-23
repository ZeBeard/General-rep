from ship import Ship
allied_fleet = []
axis_fleet = []

brokenShips = []

def check(some_function):
    """
    This decorator checks if the input data is valid for the ship creation and
    in case it is not prints out about the ship collapsing during construction
    While skipping creation of the Ship object
    """

    def wrapper(*args):
        validArgs = {}
        for z in args:
            for key in z:
                if z[key][0] > 0 and z[key][1] > 0:
                    validArgs[key] = z[key]
                else:
                    print(f"{key} collapsed during construction")

        return some_function(validArgs)

    return wrapper


def testReq(some_function):
    """
    This decorator checks if the input data is valid for the ship creation and
    in case it is stops the code and return 0
    """

    def wrapper(*args):
        brokenShips.clear()
        validArgs = {}
        for z in args:
            for key in z:
                if z[key][0] <= 0 or z[key][1] <= 0:
                    brokenShips.append(z[key])

                else:
                    validArgs[key] = z[key]

        return some_function(validArgs)

    return wrapper

@testReq
# @check
def dockyard(hulls):
    for y in hulls.keys():
        y = Ship(y, hulls[y][0], hulls[y][1], hulls[y][2])
        if y.team == "Kriegsmarine":  # spliting ships into teams
            axis_fleet.append(y)
        else:
            allied_fleet.append(y)