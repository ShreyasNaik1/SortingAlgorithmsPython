

def mergeSort(unsortedList, L, R, numOfSwaps):
    if (R > L): 
        M = (L + R) // 2
        yield from mergeSort(unsortedList, L, M, numOfSwaps)
        yield from mergeSort(unsortedList, M + 1, R, numOfSwaps)
        yield from merge(unsortedList, L, M + 1, R - M, numOfSwaps)
        yield unsortedList


def quickSort(unsortedList, beg, last, numOfSwaps):

    if beg >= last:
        return

    pivot = unsortedList[last]
    pivotIndex = beg

    for i in range(beg, last):
        if unsortedList[i] < pivot:
            swap(unsortedList, i, pivotIndex)
            numOfSwaps[0] += 1
            pivotIndex += 1
        yield unsortedList
    swap(unsortedList, last, pivotIndex)
    numOfSwaps[0] += 1
    yield unsortedList

    yield from quickSort(unsortedList, beg, pivotIndex - 1)
    yield from quickSort(unsortedList, pivotIndex + 1, last)


def insertionSort(unsortedList, numOfSwaps):

    for i in range(1, len(unsortedList)):
        j = i
        while j > 0 and unsortedList[j] < unsortedList[j - 1]:
            swap(unsortedList, j, j - 1)
            numOfSwaps[0] += 1
            j -= 1
            yield unsortedList


def selectionSort(unsortedList, numOfSwaps):

    if len(unsortedList) == 1:
        return

    for i in range(len(unsortedList)):

        minVal = unsortedList[i]
        minIndex = i
        for j in range(i, len(unsortedList)):
            if unsortedList[j] < minVal:
                minVal = unsortedList[j]
                minIndex = j
            yield unsortedList

        swap(unsortedList, i, minIndex)
        numOfSwaps[0] += 1

        yield unsortedList


def bubbleSort(unsortedList, numOfSwaps):

    if len(unsortedList) == 1:
        return

    swapped = True
    for i in range(len(unsortedList) - 1):
        if not swapped:
            break
        swapped = False
        for j in range(len(unsortedList) - 1 - i):
            if unsortedList[j] > unsortedList[j + 1]:
                swap(unsortedList, j, j + 1)
                numOfSwaps[0] += 1
                swapped = True
            yield unsortedList

  
def heapSort(unsortedList, numOfSwaps): 
    length = len(unsortedList) 
    for i in range(length, -1, -1): 
        heapify(unsortedList, length, i) 
    for i in range(length-1, 0, -1): 
        swap(unsortedList, i, 0)
        numOfSwaps[0] += 1
        heapify(unsortedList, i, 0) 
        yield unsortedList


def shellSort(unsortedList, numOfSwaps):
    
    size = len(unsortedList)  
    midIndex = size // 2

    while midIndex > 0:

        for i in range(midIndex, size):
            temp = unsortedList[i]
            j = i

            while j >= midIndex and unsortedList[j - midIndex] > temp:
                unsortedList[j] = unsortedList[j - midIndex]
                numOfSwaps[0] += 1
                j = j - midIndex

            unsortedList[j] = temp
            yield unsortedList

        midIndex = midIndex // 2




def merge(unsortedList, fir, sec, secsize, numOfSwaps):
    
    merged = []
    firsave = fir
    firend = sec
    secend = sec + secsize

    while fir < firend and sec < secend:
        if (unsortedList[fir] < unsortedList[sec]) : 
            merged.append(unsortedList[fir])
            fir += 1
            numOfSwaps[0] += 1
        else: 
            merged.append(unsortedList[sec])
            numOfSwaps[0] += 1
            sec += 1
    if fir == firend:
        while sec != secend:
            merged.append(unsortedList[sec])
            sec += 1
            numOfSwaps[0] += 1
    else: 
        while fir != firend: 
            merged.append(unsortedList[fir])
            fir += 1
            numOfSwaps[0] += 1
    for i in range(len(merged)):
        unsortedList[firsave] = merged[i] 
        yield unsortedList



def heapify(unsortedList, length, i, numOfSwaps): 
    largest = i        
    L = 2 * i + 1      
    R = 2 * i + 2      
    if L < length and unsortedList[i] < unsortedList[L]: 
        largest = L 
    if R < length and unsortedList[largest] < unsortedList[R]: 
        largest = R 
    if largest != i: 
        swap(unsortedList, i, largest)
        numOfSwaps[0] += 1
        
        heapify(unsortedList, length, largest, numOfSwaps[0]) 