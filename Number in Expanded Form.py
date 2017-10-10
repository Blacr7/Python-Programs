def expanded_form(num):
    expandedList = []
    
    numList = [int(x) for x in str(num)]
    numList = numList[::-1]

    for i in range(len(numList)):
        if numList[i] != 0:
            expandedList.append(numList[i] * 10**i)

    return " + ".join((map(str, expandedList[::-1])))
