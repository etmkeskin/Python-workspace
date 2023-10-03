import random
import time
from utilities import students
from utilities import studentsInfo
from utilities import SeaLife


# import the approriate items from utilities.py and other modules may you require

def task0():
    print("Name: Ibrahim Etem Keskin\nStudent ID: 219076074\nemail: etmkeskin@outlook.com\nSection A")


def task1():
    flag = True
    while flag:
        def printOutcome(user, comp):
            if user == 1 and comp == 3:
                print("You win!")
            elif user == 2 and comp == 1:
                print("You Win!")
            elif user == 3 and comp == 2:
                print("You Win!")
            if comp == 3 and user == 2:
                print("HAL Win!")
            elif comp == 2 and user == 1:
                print("HAL Win!")
            elif comp == 1 and user == 3:
                print("HAL Win")
            else:
                print("A tie!")

        dict_opt = {1: "rock", 2: "paper", 3: "scissors"}
        print("Make your selection...")
        user = int(input("(1)Rock, (2)Paper, (3)Scissors ? "))
        print(f"You: {dict_opt[user]}")
        comp = random.randint(1, 3)
        print(f"HAL: {dict_opt[comp]}")
        printOutcome(user, comp)
        answer = input("Play again (Y/N)? ").upper()

        if answer == "Y":
            flag = True
        else:
            flag = False


def task2():
    def swapAdjacentElements(list1):
        assert len(list1) >= 2, "Must enter two or more characters"
        length = len(list1)
        if length != 0:
            length = length - 1
        for i in range(0, length, 2):
            list1[i], list1[i + 1] = list1[i + 1], list1[i]

    sequence = input("Input two or more chars separated by spaces: ")
    chars = sequence.split()
    print(f"Initial list \n{chars}")
    print(f"String version:", "".join(chars))
    swapAdjacentElements(chars)
    print(f"Initial list \n{chars}")
    print("String version:", "".join(chars))


def task3():
    def unPacking(info, index):
        for value in info:
            if value == index:
                return value

    dict_1 = {}

    for i in range((len(students))):
        year = ""
        if unPacking(studentsInfo["Year 1"], i):
            year = "Year 1"
        elif unPacking(studentsInfo["Year 2"], i):
            year = "Year 2"
        if unPacking(studentsInfo["Year 3"], i):
            year = "Year 3"
        elif unPacking(studentsInfo["Year 4"], i):
            year = "Year 4"

        program = ""
        if unPacking(studentsInfo["CS"], i):
            program = "CS"
        elif unPacking(studentsInfo["DM"], i):
            program = "DM"
        if unPacking(studentsInfo["BZ"], i):
            program = "BZ"
        elif unPacking(studentsInfo["SE"], i):
            program = "SE"

        campus = ""

        if unPacking(studentsInfo["On Campus"], i):
            campus = "On Campus"
        elif unPacking(studentsInfo["Off Campus"], i):
            campus = "Off Campus"

        dict_1[students[i]] = f"{students[i]:>10} ({year}) Program: {program} Housing: {campus}"

    for key in sorted(dict_1):
        print(dict_1[key])


def task4():
    input("Press enter to start aquarium...")
    anim1 = SeaLife(random.randint(0, 1), random.randint(5, 30))
    anim2 = SeaLife(random.randint(0, 1), random.randint(5, 30))
    anim3 = SeaLife(random.randint(0, 1), random.randint(5, 30))
    anim4 = SeaLife(random.randint(0, 1), random.randint(5, 30))
    anim5 = SeaLife(random.randint(0, 1), random.randint(5, 30))

    for currentTime in range(1, 51):
        print("-" * 40 + "Time: " + str(currentTime))
        print(anim1.getStr())
        anim1.move()
        print(anim2.getStr())
        anim2.move()
        print(anim3.getStr())
        anim3.move()
        print(anim4.getStr())
        anim4.move()
        print(anim5.getStr())
        anim5.move()
        time.sleep(0.3)


def main():
    print("\n--------- Task0: Submission Info       ------------")
    task0()
    print("\n--------- Task1: Rock, Paper, Scissors ------------")
    task1()
    print("\n--------- Task2: Swap List Elements    ------------")
    task2()
    print("\n--------- Task3: Student Info          ------------")
    task3()
    print("\n--------- Task4: Aquarium              ------------")
    task4()

    input("Press enter to quit.")


if __name__ == "__main__":
    main()
