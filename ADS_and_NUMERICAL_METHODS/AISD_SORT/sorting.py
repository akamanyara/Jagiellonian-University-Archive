import matplotlib.pyplot as plt # for graphs 
import random # for randomized data
import time # for time measuring

# -- Sorting Algorithms -- #

def bubble_sort(array):
    #* simple algorithm - go through all elements and compare then until it's sorted 
    # https://www.youtube.com/watch?v=Cq7SMsQBEUw - for visual representation
    leng = len(array)

    # travel through all array elements ( rows - going through the array n times to sort it )
    for i in range(leng):
        # breaking point
        swapped = False
        # now we are moving through the elements to compare them 
        # we can see as well that the last elements are sorted at the end of every run so len-i-1
        for j in range(0, leng - i - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True # so it doesn't leave our loops 
        
        if swapped == False: 
            break # end of the algorithm 

def insertion_sort(array):
    #* Starting from second element -> compare 2nd to 1st and swap if needed then move to the 3rd 
    #* element and compare with first two and put it in correct position. Repeat. 
    # https://www.youtube.com/watch?v=8oJS1BMKE64 - visual representation
    leng = len(array)

    # we are starting from 2nd element ! 
    for i in range(1, leng):
        key = array[i] # key is our element we looking at right now 
        j = i - 1 # j is index for elements before the key
       
        # now we are comparing our key to elements below it and if they are greater than key
        # we move them one step ahead, ( we are moving throught all of those elements so we 
        # decrement j by one every step ), lastly we set our sorted value to key value 
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1 
        array[j + 1] = key

def selection_sort(array):
    #* we are looking for lowest element and swapping it with first one then we are doing same
    #* thing with other elements to be honest
    # https://www.youtube.com/watch?v=92BfuxHn2XE - for visual representation
    leng = len(array)
    # we are looking at len-1 so our j won't go over the array 
    for i in range(leng - 1):
        # set minimum element index for current element 
        minimum = i 
        # starting from i+1 because we are not looking at the current element to the end of array
        for j in range(i + 1, leng):
            if array[j] < array[minimum]:
                minimum = j
        # swap our current element with the minimal element in array        
        array[i], array[minimum] = array[minimum], array[i]

# Now the harder ones - we gonna split them into few functions ! 

# -- Quick Sort --
# visual representation - https://www.youtube.com/watch?v=8hEyhs3OV1w
        
#* Algorithm works on Divide and Conqueur rule. 1. wybieramy pivot ( rozne sposoby ) 2. partition 
#* the array around the pivot so: smaller elements are on the left, bigger elements are on the 
#* right. Then pivot is in the right place. 3. Recursively apply same thing until it's sorted 
#* (for L and R sub-arrays) Recursion stops when only one element is left in the sub-arrays
        
# let's choose the last element pivot option ( easiest to implement ) worst case scenario O(n^2)

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

def partition(array, low, high):

    # choose the pivot option
    pivot = array[high]
    # index for array beginning ( -1 )
    i = low - 1

    # move through the array[low..high] and move smaller elements to the left side of the pivot
    # that means right side of the pivot will have the greater ones. elements from low to i 
    # are smaller after every iteration
    for j in range(low, high):
        if array[j] < pivot: 
            i += 1
            swap(array, i, j)
    
    # move pivot after the smaller elements and return it's postition
    swap(array, i + 1, high) # 'cause i is the last element of those "smaller" ones ! 
    return i + 1

def quick_sort(array, low, high):
    if low < high: 
        # our pivot placement 
        pivot_index = partition(array, low, high)
        # implement quick sort alogrithm recurently
        quick_sort(array, low, pivot_index - 1) # for left side
        quick_sort(array, pivot_index + 1, high) # for right side

# -- Heap Sort -- 
# visual representation - https://www.youtube.com/watch?v=_bkow6IykGM
        
#* convert array into max heap ( tree like structure ) so 1. raarrange the array elements to create
#* the max heap form 2. repeat until heap contains one element: a) swap root element (largest one) 
#* with last one b) remove the last element of the heap ( it's in correct position ). We reduce
#* heap size and not remove element from actual array c) heapify remaining elements. And we done.
        
# heapify function for subtree rooted with node i which is an index in array[] 
def heapify(array, leng, i):

    # we initialze largest as the root 
    largest = i 
    # left index 
    left = 2 * i + 1
    # right index 
    right = 2 * i + 2 

    # if left child is larger than root 
    if left < leng and array[left] > array[largest]:
        largest = left
    # if right child is larger than largest one so far
    if right < leng and array[right] > array[largest]:
        largest = right
    # if largest is not root 
    if largest != i:
        array[i], array[largest] = array[largest], array[i] # swap it
        # now recursively heapify the affected sub-tree
        heapify(array, leng, largest)

def heap_sort(array):
    leng = len(array)

    # build heap ( reaarrange our array )
    for i in range(leng // 2 - 1, -1, -1):
        heapify(array, leng, i)

    # extract the elements one by one from heap 
    for i in range(leng - 1, 0, -1):
        array[0], array[i] = array[i], array[0] # move root to the end 
        # call max heapify on the reduced heap 
        heapify(array, i, 0)

# -- PRINTING THE RESULTS -- 
        
# create list of our sorting algorithms ( set )
sorting_algorithms = {
    "Bubble Sort": bubble_sort,
    "Insertion Sort": insertion_sort,
    "Selection Sort": selection_sort,
    "Quick Sort": quick_sort,
    "Heap Sort": heap_sort
}

# array with sizes to test 
array_sizes = [100, 250, 500, 750, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 6000, 7500, 10000, 15000]


# dictionary to store results 
time_results = {name: [] for name in sorting_algorithms.keys()}

# Run each sorting algorithm on each array size
for size in array_sizes:
    # Generate a random array of the current size
    original_array = [random.randint(0, 15000) for _ in range(size)]
    
    for name, sort_func in sorting_algorithms.items():
        # Make a copy of the array for each sort (to avoid re-sorting an already sorted array)
        array_copy = original_array.copy()
        
        # Measure the time taken to sort the array
        start_time = time.time()
        if name == "Quick Sort":
            sort_func(array_copy, 0, len(array_copy) - 1)  # Quick Sort needs additional arguments
        else:
            sort_func(array_copy)
        end_time = time.time()
        
        # Calculate the elapsed time and store it
        elapsed_time = end_time - start_time
        time_results[name].append(elapsed_time)

# Plotting the results
plt.figure(figsize=(10, 6))
for name, times in time_results.items():
    plt.plot(array_sizes, times, label=name)

# Adding labels and title to the graph
plt.xlabel("Array Size")
plt.ylabel("Time (seconds)")
plt.title("Sorting Algorithm Performance Comparison")
plt.legend()
plt.show()