def allLongestStrings(inputArray):
    max_len = 0
    arr = []
    for i in range(len(inputArray)):
        length = len(inputArray[i])
        if max_len>len(inputArray[i]):
            continue
        elif max_len==len(inputArray[i]):
            arr.append(inputArray[i])
        elif max_len<len(inputArray[i]):
            arr=[]
            max_len = len(inputArray[i])
            arr.append(inputArray[i])
    return arr