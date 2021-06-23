import json
import re

from combat import battle, lastround
from dockyard import *

statistics = {}  # container for amount of ships and number of rounds


def readAndExecute(data):
    hulls = {}
    with open("../Battle/Data/" + data, 'r') as data:
        team = ''
        for line in data:
            if line == "[Kriegsmarine:\n":
                team = "Kriegsmarine"
            elif line == "[Royal Navy:\n":
                team = "Royal Navy"
            pattern = re.compile(
                r"([a-z-* a-z]+) has armor amount: (-*\d{1,2}) "
                r"and hit power: (-*\d{1,2})", re.I)
            matches = pattern.finditer(line)
            for match in matches:
                hulls[match[1]] = [int(match[2]), int(match[3]), team]
    dockyard(hulls)
    statistics["numberOfShips"] = len(hulls)  # number of ships
    try:
        if len(brokenShips) != 0:
            raise Exception(ValueError)
        else:

            # print('\n       Welcome to the Fleet, son'  # nice litle introduction
            #       '\n\nAt the moment Allied fleet look like this:')
            # for x in allied_fleet:  # prints out all the hips in on of the team
            #     print(f'    {x.name} has {x.armor} armor and {x.power} power')
            # print('Axis fleet look like this: ')
            # for x in axis_fleet:  # prints out all the hips in the other team
            #     print(f'    {x.name} has {x.armor} armor and {x.power} power')
            # print(
            #     '\n                Let the fight begin!\n')  # Start of combat mark

            open('Battle resulsts.json',
                 'w').close()  # file clean up before the start of the run

            results = battle(allied_fleet, axis_fleet)

            statistics["lastRoundNumber"] = len(lastround)  # number of rounds

            with open("Battle resulsts.json", "a") as file:
                json.dump(results, file, indent=4)
            return "Success"
    except:
        return "Invalid Data"
        print("Invalid Data")

