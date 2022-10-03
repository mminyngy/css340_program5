import sort
import random
import sys
import time

#Create a list of random integers with a size of input from the user
def create_list(num):
    numbers = []
    for i in range(num):
        number = random.randint(0, 1000)
        numbers.append(number)
    return numbers

#Sort the list

#using bubble sort
def bubble(num):
    list = create_list(num)
    start_time = time.time_ns()
    sort.bubble_sort(list)
    end_time = time.time_ns()
    print(f"Bubble sort time: {(end_time - start_time)} ms")

#using insertion sort
def insertion(num):
    list = create_list(num)
    start_time = time.time_ns()
    sort.insertion_sort(list)
    end_time = time.time_ns()
    print(f"insertion sort time: {(end_time - start_time)} ms")

#using merge sort
def merge(num):
    list = create_list(num)
    start_time = time.time_ns()
    sort.merge_sort(list)
    end_time = time.time_ns()
    print(f"iterative merge sort time: {(end_time - start_time)} ms")

#using iterative merge sort
def imerge(num):
    list = create_list(num)
    start_time = time.time_ns()
    sort.iterative_merge_sort(list)
    end_time = time.time_ns()
    print(f"iterative merge sort time: {(end_time - start_time)} ms")

#using quick sort
def quick(num):
    list = create_list(num)
    start_time = time.time_ns()
    sort.quick_sort(list)
    end_time = time.time_ns()
    print(f"quick sort time: {(end_time - start_time)} ms")

#using shell sort
def shell(num):
    list = create_list(num)
    start_time = time.time_ns()
    sort.shell_sort(list)
    end_time = time.time_ns()
    print(f"shell sort time: {(end_time - start_time)} ms")

#when user calls sorter.py without input
if len(sys.argv) == 1:
    print("Error: Invalid input. Please select the option.")

#when user calls sorter.py and one of the sorts without the size of a list
elif len(sys.argv) == 2:
    print("Error: Invalid input. Please enter the number of elements of the list.")

#when user call sorter.py with appropriate inputs
elif len(sys.argv) == 3:
    length = eval(sys.argv[2])
    if sys.argv[1] == "bubble":
        bubble(length)
    elif sys.argv[1] == "insertion":
        insertion(length)
    elif sys.argv[1] == "merge":
        merge(length)
    elif sys.argv[1] == "imerge":
        imerge(length)
    elif sys.argv[1] == "quick":
        quick(length)
    elif sys.argv[1] == "shell":
        shell(length)
    #typo error
    else:
        print("Error: Invalid input. Please check the spelling.")

