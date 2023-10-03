import random
import time


class snail:
    animation_sequence = ["__~@", "_~_@", "~__@"]

    def __init__(self, name):
        #assert len(name) != 2, "Snail's initials must be 2 characters."

        self.name = name.upper()
        self.speed = (random.randint(1, 10)) / 10
        self.frame = 0
        self.pos = 0

    def move(self):
        self.pos = (self.pos + self.speed)
        self.frame = self.frame + 1
        if self.frame > 2:
            self.frame = 0

    def getIntPos(self):
        return int(self.pos)

    def getName(self):
        return self.name

    def getStr(self):
        animation = (" " * self.getIntPos())
        animation = animation + snail.animation_sequence[self.frame]
        animation = animation + (" " * (46 - self.getIntPos()))
        animation = animation + self.getName()
        return animation


def getSnailList():
    N = int(input("How many snails are racing? "))
    snail_list = []
    for i in range(N):
        snail_new = input("Snail {} two initials:".format(str(i + 1)))
        snail_list.append(snail(snail_new))
    return snail_list


def runRace(snails):
    input("Press enter to start the race!")
    time_step = 1
    while True:
        current_time_step = "{} Time {}".format((40 * "-"), str(time_step))
        print(current_time_step)
        for j in snails:
            print(j.getStr())
            j.move()
            pos = j.getIntPos()
            if pos > 39:
                print("Snail {} Won!".format(j.getName()))
                return
        time.sleep(0.2)
        time_step = time_step + 1


def main():
    print("Snail Race...")
    snails = getSnailList()
    runRace(snails)
    ans = input("Play again (Y)?").upper()
    if ans == "Y":
        main()


if __name__ == "__main__":
    main()
