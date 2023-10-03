class MinMaxList:

    def __init__(self, initializeList):
        self.listData = initializeList
        self.listData.sort()

    def insertItem(self, item, printResult):
        global index
        length = len(self.listData)
        if length == 0:
            self.listData.append(item)
        elif item >= self.listData[-1]:
            self.listData.append(item)
        else:
            index = 0
            while item > self.listData[index]:
                index = index + 1
            self.listData.insert(index, item)

        if printResult is True:
            print("Item ({}) inserted at location {}".format(str(item), str(index)))
            self.printList()

    def printList(self):
        print(self.listData)

    def getMin(self):
        result = self.listData[0]
        self.listData = self.listData[1:]
        return result

    def getMax(self):
        length = len(self.listData)
        result = self.listData[length - 1]
        self.listData = self.listData[:length - 1]
        return result
