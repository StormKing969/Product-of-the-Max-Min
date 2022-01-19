def maxMin(operations, x):
    tempArray = []
    resultArray = []
    i = 0

    while i < len(x):
        if operations[i] == "push":
            tempArray.append(x[i])
            tempArray.sort()
            minValue = x[0]
            maxValue = x[(len(tempArray) - 1)]

            resultValue = minValue * maxValue
            resultArray.append(resultValue)


        if operations[i] == "pop":
            removeValue = x[i]

            tempArray.remove(removeValue)
            print(tempArray)

            tempArray.sort()
            minValue2 = tempArray[0]
            print(minValue2)
            maxValue3 = tempArray[(len(tempArray) - 1)]
            print(maxValue3)

            resultValue = minValue2 * maxValue3
            resultArray.append(resultValue)

        i += 1

    print(resultArray)


maxMin(["push", "push", "push", "pop"], [1,2,3,1])

