import random as r

from ship import names


def creation():
    data = {r.choice(names): [r.randint(0, 50), r.randint(-10, 30),
                            r.choice(["Kriegsmarine", "Royal Navy"])] for x in
            range(r.randint(10, 20))}
    with open("input Data.txt", "w") as file:
        file.write("[Kriegsmarine:\n")
        for x in data:
            if data[x][2] == "Kriegsmarine":
                file.write(f"[{x} has armor amount: {data[x][0]} "
                           f"and hit power: {data[x][1]}]\n")
        file.write("]\n[Royal Navy:\n")
        for x in data:
            if data[x][2] == "Royal Navy":
                file.write(f"[{x} has armor amount: {data[x][0]} "
                           f"and hit power: {data[x][1]}]\n")
        file.write("]")
