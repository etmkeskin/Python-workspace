from MinMaxList import MinMaxList
from random import randint


# Main function is given.
def main():
    aList = MinMaxList([10, 11, 99, 1, 34, 88])

    print("\nInsert Item")
    for i in range(30):
        x = randint(1, 100)
        aList.insertItem(x, True)

    print("\nGet Min")
    for i in range(10):
        print("Min item %d " % aList.getMin())
        aList.printList()

    print("\nGet Max")
    for i in range(10):
        print("Max item %d " % aList.getMax())
        aList.printList()


if __name__ == "__main__":
    main()
