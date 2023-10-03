import random


def task1():
    list_Size = int(input("Input list size: "))
    max_Int = int(input("Input max int: "))

    def generateRandomList(list_size, max_int):
        rnd_list = []

        for i in range(list_size):
            num = random.randint(0, max_int)
            rnd_list.append(num)
        return rnd_list

    def computeAverage(list1):
        list_Size = len(list1)
        total = 0
        for i in list1:
            total += i

        average_total = total / list_Size
        return average_total

    list1 = generateRandomList(list_Size, max_Int)
    avg = computeAverage(list1)
    print(list1)
    print("Average value = {:.4f}".format(avg))


def task2():
    def stringToCharList(inputStr):
        list1 = list()
        for char in inputStr:
            list1.append(char)
        return list1

    def charsToWord(str_to_char):
        dict1 = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven',
                 '8': 'eight', '9': 'nine', '-': 'dash'}
        list2 = list()
        for i in str_to_char:
            list2.append(dict1[i])
        return list2

    print("Enter phone number as XXX-XXX-XXXX")
    phone_number = input("Type here: ")
    str_version = stringToCharList(phone_number)
    word_list = charsToWord(str_version)
    print(str_version)
    print(word_list)
    new_str = word_list[0]
    for j in word_list[1:]:
        new_str = new_str + "->" + j
    print(new_str)


def main():
    print("\n--------- TASK 1: Random List -------------")
    task1()

    print("\n--------- TASK 2: Phone number to text ---")
    task2()

    input("Press enter to exit.")


if __name__ == "__main__":
    main()
