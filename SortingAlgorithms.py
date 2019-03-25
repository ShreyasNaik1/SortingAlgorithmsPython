import random

def swap(list, i, j):
    if i != j:
        list[i], list[j] = list[j], list[i]


def mergeSort(unsortedList, beg, last, numOfSwaps):
    
    if last <= beg:
        return

    mid = beg + ((last - beg + 1) // 2) - 1
    yield from mergeSort(unsortedList, beg, mid, numOfSwaps)
    yield from mergeSort(unsortedList, mid + 1, last, numOfSwaps)
    yield from merge(unsortedList, beg, mid, last, numOfSwaps)
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
        heapify(unsortedList, length, i, numOfSwaps) 
        yield unsortedList
    for i in range(length-1, 0, -1): 
        swap(unsortedList, i, 0)
        numOfSwaps[0] += 1
        heapify(unsortedList, i, 0, numOfSwaps) 
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




def merge(unsortedList, beg, mid, last, numOfSwaps):
    
    merged = []
    leftIndex = beg
    rightIndex = mid + 1

    while leftIndex <= mid and rightIndex <= last:
        if unsortedList[leftIndex] < unsortedList[rightIndex]:
            merged.append(unsortedList[leftIndex])
            leftIndex += 1
        else:
            merged.append(unsortedList[rightIndex])
            numOfSwaps[0] += 1
            rightIndex += 1

    while leftIndex <= mid:
        merged.append(unsortedList[leftIndex])
        leftIndex += 1

    while rightIndex <= last:
        merged.append(unsortedList[rightIndex])
        rightIndex += 1

    for i, sorted_val in enumerate(merged):
        unsortedList[beg + i] = sorted_val
        numOfSwaps[0] += 1
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
        
        heapify(unsortedList, length, largest, numOfSwaps) 




def countingSort(unsortedList, exp1, numOfSwaps): 
  
    n = len(unsortedList) 
  
    # The output array elements that will have sorted unsortedList 
    output = [0] * (n) 
  
    # initialize count array as 0 
    count = [0] * (10) 
  
    # Store count of occurrences in count[] 
    for i in range(0, n): 
        index = (unsortedList[i]/exp1) 
        count[ (index)%10 ] += 1
  
    # Change count[i] so that count[i] now contains actual 
    #  position of this digit in output array 
    for i in range(1,10): 
        count[i] += count[i-1] 
        numOfSwaps += 1
  
    # Build the output array 
    i = n - 1
    while i >= 0: 
        index = (unsortedList[i]/exp1) 
        output[ count[ (index)%10 ] - 1] = unsortedList[i] 
        count[ (index)%10 ] -= 1
        i -= 1
  
    # Copying the output array to unsortedList[], 
    # so that unsortedList now contains sorted numbers 
    i = 0
    for i in range(0,len(unsortedList)): 
        unsortedList[i] = output[i] 
  

  
# Method to do Radix Sort 
def radixSort(unsortedList, numOfSwaps): 
  
    # Find the maximum number to know number of digits 
    max1 = max(unsortedList) 
  
    # Do counting sort for every digit. Note that instead 
    # of passing digit number, exp is passed. exp is 10^i 
    # where i is current digit number 
    exp = 1
    while max1/exp > 0: 
        countingSort(unsortedList, exp, numOfSwaps) 
        exp *= 10
        yield unsortedList


def gnomeSort(unsortedList, numOfSwaps): 
    i = 0
    while i < len(unsortedList):
        if i == 0: 
            i += 1
            yield unsortedList
        if unsortedList[i] >= unsortedList[i - 1]: 
            i += 1
            yield unsortedList
        else: 
            swap(unsortedList, i-1, i) 
            numOfSwaps[0] += 1
            i -= 1

            yield unsortedList

def bogoSort(unsortedList): 
    while not(inorder(unsortedList)): 
        random.shuffle(unsortedList)
        yield unsortedList 


def inorder(unsortedList):
    i = 0
    j = len(unsortedList)
    while i + 1 < j:
        if unsortedList[i] > unsortedList[i + 1]:
            return False
        i += 1
    return True
