from random import randint


def getCardValue():
    result = randint(2, 14)
    return result


def getCardStr(card, message=""):
    if message != "":
        print(message, end=' ')
    if card == 10:
        print("[T]")
    elif card == 11:
        print("[J]")
    elif card == 12:
        print("[Q]")
    elif card == 13:
        print("[K]")
    elif card == 14:
        print("[A]")
    else:
        card = str(card)
        print("[" + card + "]")


### Write your main program below ####
msg = """--- Welcome to High-Low ---
Start with 100 points.  Each round a card will be drawn and shown.
Select whether you think the 2nd card will be Higher or Lower than the 1st card.
Then enter the amount you want to bet.
If you are right, you win the amount you bet, otherwise you lose. 
Try to make it to 500 points within 10 tries."""

print(msg)
print("\n--------------------------------")


def main():
    # define a global variable
    global keepPlaying
    keepPlaying = True
    point = 100
    round = 0
    while keepPlaying:
        round = round + 1
        print("OVERALL POINT: " + str(point) + " ROUND " + str(round) + "/10")
        card_1 = getCardValue()
        getCardStr(card_1, "First card is a")

        guess = input("High or Low (H/L)?: ").upper()

        while guess != "H" and guess != "L":
            guess = input("High or Low (H/L)?: ").upper().strip()

        bet = int(input("Bet amount: "))

        while bet > point:
            bet = int(input("Bet amount: "))

        card_2 = getCardValue()

        if guess == "L":
            if card_2 < card_1:
                point = point + bet
                getCardStr(card_2, "Second card is a")
                print("Card1 {} Card2 {} - You bet 'LOW' for  {} - YOU WON".format(card_1, card_2, point))
                print("\n--------------------------------------------")
            else:
                point = point - bet
                getCardStr(card_2, "Second card is a")
                print("Card1 {} Card2 {} - You bet 'LOW' for  {} - YOU LOST".format(card_1, card_2, point))
                print("\n--------------------------------------------")

        if guess == "H":
            if card_2 > card_1:
                point = point + bet
                getCardStr(card_2, "Second card is a")
                print("Card1 {} Card2 {} - You bet 'HIGH' for  {} - YOU WON".format(card_1, card_2, point))
                print("\n--------------------------------------------")

            else:
                point = point - bet
                getCardStr(card_2, "Second card is a")
                print("Card1 {} Card2 {} - You bet 'HIGH' for  {} - YOU LOST".format(card_1, card_2, point))

        if point >= 500:
            print("\n---------------WIN--------------------------")
            print("YOU MADE IT TO *{}* POINTS IN {} Rounds!".format(str(point), str(round)))
            print("--------------------------------------------")
            keepPlaying = False
        if round == 9:
            print("\n-----------LOSE-----------------------------")
            print("ONLY *{}* POINTS IN 10 ROUNDS!")
            print("--------------------------------------------")
            keepPlaying = False

        if point <= 0:
            print("\n-----------LOSE-----------------------------")
            print("YOU HAVE *0* POINTS AFTER {} ROUNDS!".format(str(round)))
            print("--------------------------------------------")
            keepPlaying = False
    input("Press enter to exit ")

if __name__ == "__main__":
    main()
