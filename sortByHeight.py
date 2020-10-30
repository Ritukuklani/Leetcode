# Some people are standing in a row in a park. There are trees 
# between them which cannot be moved. Your task is to rearrange the 
# people by their heights in a non-descending order without moving the trees. 
# People can be very tall!
def sortByHeight(a):
    arr = []
    for i in range(len(a)):
        if a[i]!=-1:
            arr.append(a[i])
    # b = sorted([i for i in a if i!=-1])
    # print("b",b)
    arr.sort()
    j=0
    for i in range(len(a)):
        if a[i]!=-1:
            a[i] = arr[j]
            j+=1
        i+=1
    return a
