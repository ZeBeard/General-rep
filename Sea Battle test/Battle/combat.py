import random as r
lastround=[]

def battle(allied_fleet, axis_fleet):
    lastround.clear()
    roundNumber = 1
    results = {}
    while len(axis_fleet) > 0 and len(allied_fleet) > 0:

        # fire but each ship into a random enemy ship
        for x in axis_fleet:
            r.choice(allied_fleet).takeDamage(x.fire())
        # fire but each ship into a random enemy ship
        for x in allied_fleet:
            r.choice(axis_fleet).takeDamage(x.fire())
        # casualty calculation
        for ship in axis_fleet:
            ship.cleanUp()
            if ship.timeTillSank <= 0:
                axis_fleet.remove(ship)
        for ship in allied_fleet:
            ship.cleanUp()
            if ship.timeTillSank <= 0:
                allied_fleet.remove(ship)

        results[f"Round number {roundNumber}"] = {
            "allies": {
                x.name: {"armore": round(x.armor, 2),
                         "power": round(x.power, 2)}
                for x in allied_fleet},
            "axis": {
                x.name: {"armore": round(x.armor, 2),
                         "power": round(x.power, 2)}
                for x in axis_fleet}
        }

        # print(f"\n             End of round {roundNumber}")
        #
        # print('Allied fleet look like this:')  # display of still alive ship
        # for x in allied_fleet:
        #     print(
        #         f'  {x.name} has {round(x.armor, 2) if x.armor > 0 else "No"}'
        #         f' armor and {x.power} power')
        # print('Axis fleet look like this: ')
        # for x in axis_fleet:
        #     print(
        #         f'  {x.name} has {round(x.armor, 2) if x.armor > 0 else "No"} '
        #         f' armor and {x.power} power')
        # print("")
        roundNumber += 1
        lastround.append(roundNumber)
    # if len(axis_fleet) > len(allied_fleet):  # final results
    #     print("\n                 Axis Victory")
    # else:
    #     print("\n                 Allied victory")
    return results
