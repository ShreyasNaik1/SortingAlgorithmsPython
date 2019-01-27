def swap(list, i, j):

    if i != j:
        list[i], list[j] = list[j], list[i]


def mergeSort(unsortedList, beg, last):
    
    if last <= beg:
        return

    mid = beg + ((last - beg + 1) // 2) - 1
    yield from mergeSort(unsortedList, beg, mid)
    yield from mergeSort(unsortedList, mid + 1, last)
    yield from merge(unsortedList, beg, mid, last)
    yield unsortedList


def merge(unsortedList, beg, mid, last):
    
    merged = []
    leftIndex = beg
    rightIndex = mid + 1

    while leftIndex <= mid and rightIndex <= last:
        if unsortedList[leftIndex] < unsortedList[rightIndex]:
            merged.append(unsortedList[leftIndex])
            leftIndex += 1
        else:
            merged.append(unsortedList[rightIndex])
            rightIndex += 1

    while leftIndex <= mid:
        merged.append(unsortedList[leftIndex])
        leftIndex += 1

    while rightIndex <= last:
        merged.append(unsortedList[rightIndex])
        rightIndex += 1

    for i, sorted_val in enumerate(merged):
        unsortedList[beg + i] = sorted_val
        yield unsortedList


def quickSort(unsortedList, beg, last):

    if beg >= last:
        return

    pivot = unsortedList[last]
    pivotIndex = beg

    for i in range(beg, last):
        if unsortedList[i] < pivot:
            swap(unsortedList, i, pivotIndex)
            pivotIndex += 1
        yield unsortedList
    swap(unsortedList, last, pivotIndex)
    yield unsortedList

    yield from quickSort(unsortedList, beg, pivotIndex - 1)
    yield from quickSort(unsortedList, pivotIndex + 1, last)


def insertionSort(unsortedList):

    for i in range(1, len(unsortedList)):
        j = i
        while j > 0 and unsortedList[j] < unsortedList[j - 1]:
            swap(unsortedList, j, j - 1)
            j -= 1
            yield unsortedList


def selectionSort(unsortedList):

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

        yield unsortedList


def bubbleSort(unsortedList):

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
                swapped = True
            yield unsortedList


 
def heapify(unsortedList, length, i): 
    largest = i        
    L = 2 * i + 1      
    R = 2 * i + 2      
    if L < length and unsortedList[i] < unsortedList[L]: 
        largest = L 
    if R < length and unsortedList[largest] < unsortedList[R]: 
        largest = R 
    if largest != i: 
        unsortedList[i],unsortedList[largest] = unsortedList[largest],unsortedList[i] 
  
        heapify(unsortedList, length, largest) 
  
def heapSort(unsortedList): 
    length = len(unsortedList) 
    for i in range(length, -1, -1): 
        heapify(unsortedList, length, i) 
    for i in range(length-1, 0, -1): 
        unsortedList[i], unsortedList[0] = unsortedList[0], unsortedList[i] 
        heapify(unsortedList, i, 0) 
        yield unsortedList


def shellSort(unsortedList):
    
    size = len(unsortedList)  
    midIndex = size // 2

    while midIndex > 0:

        for i in range(midIndex, size):
            temp = unsortedList[i]
            j = i

            while j >= midIndex and unsortedList[j - midIndex] > temp:
                unsortedList[j] = unsortedList[j - midIndex]
                j = j-midIndex

            unsortedList[j] = temp
            yield unsortedList

        midIndex = midIndex // 2