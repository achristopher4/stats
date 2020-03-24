"""
Create multiple functions that can find median, mode, and mean
in a set of numbers. Use main function to call these functions.
"""
def median(list):
    if list == 0:
        return 0 
    newList = []
    for element in list:
        newList.append(element)
    newList.sort()
    check = len(newList) / 2
    findCenter = len(newList) // 2

    if len(newList) % 2 == 1:
        median = newList[findCenter]
        return median
    else:
        value1 = newList[int(check)]
        value2 = newList[findCenter - 1]
        median = (value1 + value2) / 2
        return median


def mean(list):
    if list == 0:
        return 0
    count = len(list)
    trueValue = 0
    index = 0
    for element in list:
        value = list[index]
        trueValue += value
        index += 1
    mean = trueValue / count
    return mean


def mode(list):
    if list == 0:
        return 0
    modeList = []
    dic = {}

    for index in list:
        number = dic.get(index, None)
        if number == None:
            dic[index] = 1
        else:
            dic[index] = number + 1
    maxValue = max(dic.values())
    for key in dic:
        if dic[key] == maxValue:
            modeList.append(key)
    return modeList[0]


def main():
    user = input("Enter number: ")
    createList = []
    while True:
        if user == "":
            break
        changeInput = int(user)
        createList.append(changeInput)
        user = input("Enter number: ")
    print("List; ", createList)
    print("Median: ", median(createList))
    print("Mean: ", mean(createList))
    print("Mode: ", mode(createList))
