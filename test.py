#
# Test driver from Program 5
#
import random
import sort
# Function to return random list of a given size
def randList(size):
    random.seed(1009)
    the_list = []
    for i in range(size):
        the_list.append(random.randint(0,size))
    return the_list
def testSort(sort_function, size):
    l = randList(size)
    l_sorted = l[:]
    l_sorted.sort()
    sort_function(l)
    return l == l_sorted
score = 30
#Test Quicksort
if not testSort(sort.quick_sort, 101):
    print("Error: Quick Sort 101:  -2")
    score -= 2
#if not testSort(sort.quick_sort, 785):
#    print("Error: Quick Sort 785:  -2")
#    score -= 2
#if not testSort(sort.quick_sort, 5629):
#    print("Error: Quick Sort 5629:  -1")
#    score -= 1

#Test ShellSort
if not testSort(sort.shell_sort, 101):
    print("Error: Shell Sort 101:  -2")
    score -= 2
if not testSort(sort.shell_sort, 785):
    print("Error: Shell Sort 785:  -2")
    score -= 2
if not testSort(sort.shell_sort, 5629):
    print("Error: Shell Sort 5629:  -1")
    score -= 1
if not testSort(sort.merge_sort, 101):
    print("Error: Merge Sort 101:  -2")
    score -= 2
if not testSort(sort.merge_sort, 785):
    print("Error: Merge Sort 785:  -2")
    score -= 2
if not testSort(sort.merge_sort, 5629):
    print("Error: Merge Sort 5629:  -1")
    score -= 1

#Iterative Merge Sort
if not testSort(sort.iterative_merge_sort, 9):
    print("Error: Iterative Merge Sort 9:  -2")
    score -= 2
if not testSort(sort.iterative_merge_sort, 10):
    print("Error: Iterative Merge Sort 10:  -2")
    score -= 2
if not testSort(sort.iterative_merge_sort, 11):
    print("Error: Iterative Merge Sort 11:  -2")
    score -= 1
if not testSort(sort.iterative_merge_sort, 101):
    print("Error: Iterative Merge Sort 101:  -2")
    score -= 2
if not testSort(sort.iterative_merge_sort, 785):
    print("Error: Iterative Merge Sort 785:  -2")
    score -= 2
if not testSort(sort.iterative_merge_sort, 5629):
    print("Error: Iterative Merge Sort 5629:  -1")
    score -= 1
print("Final Score: ", score)
