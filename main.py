import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animate
from sortingAlgorithms import mergeSort, quickSort, bubbleSort, insertionSort, selectionSort, heapSort, shellSort
import sys


if __name__ == "__main__":
    N = int(input("Enter the size of the list: "))
    selectAlg = " Choose a particular sorting algorithm: \
                 \n 1. Merge \
                 \n 2. Quick \
                 \n 3. Insertion \
                 \n 4. Selection \
                 \n 5. Heap \
                 \n 6. Shell \
                 \n 7. Bubble \
                 \n"

    alg = input(selectAlg)


    unsortedList = [x + 1 for x in range(N)]
    random.seed(time.time())
    random.shuffle(unsortedList)

    colour = "blue"
    description = "Unselected Sorting Algorithm"


    if alg == "M" or alg == "m" or alg == "1" or alg == "1.":
        sortingMethod = "Merge Sort"
        singleSort = mergeSort(unsortedList, 0, N - 1)
        description = "\n \n Merge sort is a sorting technique based \
                    \n on divide and conquer technique. With worst-case \
                    \n time complexity being O(n x log(n)), it is one of \
                    \n the most respected algorithms. Merge sort first \
                    \n divides the array into equal halves and then \
                    \n combines them in a  sorted manner.  \
                    \n \n Read More at (right click): https://www.tutorialspoint.com/data_structures_algorithms/merge_sort_algorithm.htm"

    elif alg == "Q" or alg == "q" or alg == "2" or alg == "2.":
        sortingMethod = "Quick Sort"
        singleSort = quickSort(unsortedList, 0, N - 1)
        colour = "gold"
        description = "\n \n \n QuickSort is a Divide and Conquer algorithm. \
                    \n It picks an element as pivot and partitions  \
                    \n the given array around the picked pivot.  \
                    \n There are many different versions of quickSort  \
                    \n that pick pivot in different ways. \n \
                    \n Read More at (right click): https://www.geeksforgeeks.org/quick-sort/"

    elif alg == "I" or alg == "i" or alg == "3" or alg == "3.":
        sortingMethod = "Insertion Sort"
        singleSort = insertionSort(unsortedList)
        colour = "red"
        description = "\n \n \n Insertion sort is based on the idea that one \
                    \n element from the input elements is consumed  \
                    \n in each iteration to find its correct position \
                    \n i.e, the position to which it belongs in a \
                    \n sorted array. It iterates the input elements \
                    \n by growing the sorted array at each iteration. \
                    \n \n Read More at (right click): https://www.hackerearth.com/practice/algorithms/sorting/insertion-sort/tutorial/"

    elif alg == "Se" or alg == "se" or alg == "4" or alg == "4.":
        sortingMethod = "Selection Sort"
        singleSort = selectionSort(unsortedList)
        colour = "green"
        description = "\n \n \n Selection sort is a simple sorting algorithm. \
                    \n This sorting algorithm is an in-place \
                    \n comparison-based algorithm in which the list is \
                    \n divided into two parts, the sorted part at the \
                    \n left end and the unsorted part at the right end. \
                    \n \n Read More at (right click): https://www.tutorialspoint.com/data_structures_algorithms/selection_sort_algorithm.htm"

    elif alg == "H" or alg == "h" or alg == "5" or alg == "5.":
        sortingMethod = "Heap Sort"
        singleSort = heapSort(unsortedList)
        colour = "silver"
        description = "\n \n \n Heaps can be used in sorting an array. \
                    \n In max-heaps, maximum element will always \
                    \n be at the root. Heap Sort uses this \
                    \n property of heap to sort the array. \
                    \n Read More at (right click): https://www.hackerearth.com/practice/algorithms/sorting/heap-sort/tutorial/"

    elif alg == "Sh" or alg == "sh" or alg == "6" or alg == "6.":
        sortingMethod = "Shell Sort"
        singleSort = shellSort(unsortedList)
        colour = "darkmagenta"
        description = "\n \n \n Shell sort is a highly efficient sorting \
                    \n algorithm and is based on insertion sort \
                    \n algorithm. This algorithm avoids large  \
                    \n shifts as in case of insertion sort, if \
                    \n the smaller value is to the far right and \
                    \n has to be moved to the far left. \
                    \n \n Read more at (right click): https://www.tutorialspoint.com/data_structures_algorithms/shell_sort_algorithm.htm"

    elif alg == "B" or alg == "b" or alg == "7" or alg == "7.":
        sortingMethod = "Bubble Sort"
        singleSort = bubbleSort(unsortedList)
        colour = "black"
        description = "\n \n \n Bubble sort is a simple sorting algorithm. \
                    \n This sorting algorithm is comparison-based \
                    \n algorithm in which each pair of adjacent  \
                    \n elements is compared and the elements are \
                    \n swapped if they are not in order. \
                    \n \n Read more at (right click): https://www.tutorialspoint.com/data_structures_algorithms/bubble_sort_algorithm.htm"

    else:
        print("\n \n Invalid input, please select one of either \
                        \n M/m/1/1., \
                        \n Q/q/2/2., \
                        \n I/i/3/3., \
                        \n Se/se/4/4,, \
                        \n H/h/5/5., \
                        \n Sh/sh/6/6., \
                        \n B/b/7/7. \
                        \n for the different sorting methods. \n\n\n")
        sys.exit(0)
  



    figure, axis = plt.subplots()
    cols = axis.bar(range(len(unsortedList)), unsortedList, align = "edge", color = colour)
    axis.set_title(sortingMethod)

    ylim = 1.15 * N
    axis.set_xlim(0, N)
    axis.set_ylim(0, ylim)


    numOfSwitches = axis.text(0.02, 0.95, "", transform = axis.transAxes)


    iters = [0]
    def addToFigure(unsortedList, singleBar, iters):

        for col, val in zip(singleBar, unsortedList):
            col.set_height(val)

        iters[0] += 1
        numOfSwitches.set_text("Number of switches: {}".format(iters[0]))

        

    anim = animate.FuncAnimation(figure, func = addToFigure, 
                                         fargs = (cols, iters), 
                                         frames = singleSort, 
                                         interval = 1, 
                                         repeat = False)

    print(description)

    plt.show()
