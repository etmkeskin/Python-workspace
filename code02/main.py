import random


def task1():
    print("\n")
    first_Name = input("Your first name: ")
    last_Name = input("Your last name: ")
    initial_funds = float(input("Initial funds to invest: $"))
    investment_total = float(input("Annual return percentage: "))
    print("Yearly return for {} {}".format(first_Name.capitalize().strip(), last_Name.upper().strip()))
    print("Initial deposit: ${:.2f}".format(initial_funds))

    for i in range(1, 6):
        initial_funds = initial_funds + initial_funds * investment_total / 100
        print("Year {}: ${:.2f}".format(i, initial_funds))


def task2():
    print("\n")
    print("Soda Vending Machine")
    total = 0
    print("Current amount ${:.2f} {}".format(total, str("out of $1.00")))
    print("Insert coin")
    print("1. Toonie   ($2.00) \n2. Loonie   ($1.00) \n3. Quarter  ($0.25) \n4. Dime     ($0.10)\n5. Nickel   ($0.05)")
    selection = int(input("Selection [1-5] ?"))
    if selection > 5 or selection < 1:
        print("Invalid selection")

    while total < 1:
        if selection == 1:
            total = total + 2.0
            break
        if selection == 2:
            total = total + 1.0
            break
        if selection == 3:
            total = total + 0.25
        if selection == 4:
            total = total + 0.10
        if selection == 5:
            total = total + 0.05

        print("Current amount ${:.2f} {}".format(total, str("out of $1.00")))
        if total < 1:
            print("Insert coin")
            print("1. Toonie   ($2.00) \n2. Loonie   ($1.00) \n3. Quarter  ($0.25) \n4. Dime     ($0.10)\n5. Nickel   "
                  "($0.05)")
            selection = int(input("Selection [1-5] ?"))
            if selection > 5 or selection < 1:
                print("Invalid selection")

    if total > 1:
        print("Total amount provided: $" + str(total))
        print("Thank you for your purchase.")
        print("Please take your change $" + str((total - 1.0).__round__(2)))
    elif total == 1:
        print("Total amount provided: ${:.2f}".format(total))
        print("Thank you for your purchase")

    else:
        print("Total amount provided: $1.00\nThank you for your purchase.")


def task3():
    print("\n")
    flag = True
    while flag:
        print("Dice Game\nRolling Die 10 times")

        total = 0
        counter = 0

        for i in range(1, 11):
            current = random.randint(1, 6)
            print("Roll " + str(i) + ": [" + str(current) + "]")
            total = total + current
            if current == 1:
                counter = counter + 1

        if counter == 2:
            total = total + 10

        if total > 35:
            print("Total " + str(total) + " -- OVER 35 POINTS [YOU WIN!]")
        else:
            print("Total " + str(total) + " -- TOO FEW POINTS [YOU LOSE!]")

        answer = input("Enter 'Y' to play again: ")

        if answer.upper() == "Y":
            flag = True

        else:
            flag = False


def task4():
    print("\n")

    def countCase(text):
        upper = 0
        lower = 0
        for char in text:
            if char.islower():
                lower += 1
            if char.isupper():
                upper += 1
        return upper, lower

    def flipCase(text):
        text_swapped = text.swapcase()
        return text_swapped

    def cutQuotedText(text):
        start_index = text.find('"')
        last_index = text.rfind('"')

        # if find() method cant find given value, it will return -1
        if start_index == -1 or last_index == -1:
            return "'ERROR! No quoted text.'"
        else:
            return text[0:start_index] + text[last_index + 1:len(text)]

    str_new = input("Enter string with one word with \"quotes\":")
    value = countCase(str_new)
    upper = value[0]
    lower = value[1]
    print("\nThis string has " + str(upper) + " uppercase characters.")
    print("This string has " + str(lower) + " lowercase characters.")
    print("Case flip: " + flipCase(str_new))
    print("Quote removed: " + cutQuotedText(str_new))


def main():
    print("\n----------Task 1-----------")
    task1()
    print("\n----------Task 2-----------")
    task2()
    print("\n----------Task 3-----------")
    task3()
    print("\n----------Task 4-----------")
    task4()
    input("\nPress enter to exit.")


if __name__ == "__main__":
    main()
