import pytest
import os
import json
import pathAddtion
from main import readAndExecute as AUT, statistics


@pytest.mark.json
def test_JSON_creaction():
    """
    Test of if the report file is being created
    and of if is it create in correct format
    """
    AUT("input Data (Valid).txt")
    assert os.path.exists("Battle resulsts.json") is True
    # checking if file is json by trying to load it as one
    with open("Battle resulsts.json", 'r') as data:
        try:
            json.load(data)
        except ValueError:
            assert False == True
        finally:
            print(f"\nFile is Json")

    os.remove("Battle resulsts.json")


@pytest.mark.invalid_data
@pytest.mark.parametrize("a", [("input Data (-armor).txt"),
                               ("input Data (Valid).txt"),
                               ("input Data (-power).txt"),
                               ])
def test_invalid_data(a):
    """
    Test of how code will react to incorrect input

    :param a: is an input file for the test
    """
    assert AUT(a) == "Invalid Data"


@pytest.mark.eff
def test_efficiency():
    """
    compares amount of turns the battle took and the amount of participants
    """
    AUT("input Data (Valid).txt")
    assert statistics["numberOfShips"] > statistics["lastRoundNumber"]
    os.remove("Battle resulsts.json")
