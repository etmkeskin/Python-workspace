import pytest

from typing import List


# Accepts a list of integers
def initializeMinMaxList(myList: List[int]) -> None:  # given
    myList.sort()


def insertItem(myList: List[int], item: int) -> None:  # given
    myList.append(item)
    myList.sort()


def getMinMax(myList: List[int], minormax: str) -> int:  # given -- but requires additional assert
    assert len(myList) != 0, "Empty List"
    assert minormax.upper() == "MAX" or minormax.upper() == "MIN", "2nd argument must be 'Min' or 'Max' "
    result: int
    if minormax == "MAX":
        result = myList[-1]
        del myList[-1]
    else:
        result = myList[0]
        del myList[0]
    return result


# Main function is given.
def main():
    aList = [10, 11, 99, 1, 55, 100, 34, 88]
    print("Starting List: ", aList)
    initializeMinMaxList(aList)
    min1 = getMinMax(aList, "MIN")
    print("1st min: %d" % (min1))
    min2 = getMinMax(aList, "MIN")
    print("2nd min: %d" % (min2))
    max1 = getMinMax(aList, "MAX")
    print("1st max: %d" % (max1))
    max2 = getMinMax(aList, "MAX")
    print("2nd max: %d" % (max2))

    print("Insert %d %d %d %d" % (min1 - 1, min2 - 1, max1 + 1, max2 + 1))
    insertItem(aList, min1 - 1)
    insertItem(aList, min2 - 1)
    insertItem(aList, max1 + 1)
    insertItem(aList, max2 + 1)

    min1 = getMinMax(aList, "MIN")
    print("1st min: %d" % min1)
    min2 = getMinMax(aList, "MIN")
    print("2nd min: %d" % min2)
    max1 = getMinMax(aList, "MAX")
    print("1st max: %d" % max1)
    max2 = getMinMax(aList, "MAX")
    print("2nd max: %d" % max2)

    print("DONE.  Type Enter to exit.")
    input()


if __name__ == "__main__":
    main()


#####
# WRITE YOUR TEST CASES BELOW HERE

def test_getMinMaxCase1():
    test1 = [45, 77]
    initializeMinMaxList(test1)
    min1 = getMinMax(test1, "MIN")
    assert min1 == 45, "MIN should be 45"
    max1 = getMinMax(test1, "MAX")
    assert max1 == 77, "MAX should be 77"


def test_getMinMaxCase2():
    test2 = [65]
    initializeMinMaxList(test2)
    min1 = getMinMax(test2, "MIN")
    assert min1 == 65, "MIN should be 65"
    insertItem(test2, 65)
    max1 = getMinMax(test2, "MAX")
    assert max1 == 65, "MAX should be 65"


def test_getMinMaxCase3():
    test3 = []
    initializeMinMaxList(test3)
    insertItem(test3, 34)
    insertItem(test3, 35)
    min1 = getMinMax(test3, "MIN")
    assert min1 == 34, "MIN should be 34"
    max1 = getMinMax(test3, "MAX")
    assert max1 == 35, "MAX should be 35"


def test_getMinMaxRequestError():
    test4 = [7, 17, 27]
    initializeMinMaxList(test4)
    with pytest.raises(AssertionError):
        assert getMinMax(test4, "MID") == "Should raise AssertionError"


def test_getMinMaxEmptyError():
    test5 = []
    initializeMinMaxList(test5)
    with pytest.raises(AssertionError):
        assert getMinMax(test5, "MIN") == "Should raise AssertionError"


