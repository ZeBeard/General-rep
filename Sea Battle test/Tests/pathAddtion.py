import sys
from pathlib import Path


def theWay():
    paths = (
        f"{Path().absolute().parent}/Battle")
    sys.path.append(paths)

# Now I know DA WAY
theWay()
