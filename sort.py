#sorting algorithms

#bubble sort
def bubble_sort(list):
    for i in range(len(list)):
        for j in range(len(list) - i - 1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]

#insertion sort
def insertion_sort(list):
    for place in range(1, len(list)):
        temp = list[place]
        i = place
        while i > 0 and list[i - 1] > temp:
            list[i] = list[i - 1]
            i -= 1
        list[i] = temp

#merge sort        
def merge_sort(list):
    if len(list) > 1:
        mid = len(list) // 2
        left_side = list[:mid]
        right_side = list[mid:]

        merge_sort(left_side)
        merge_sort(right_side)

        i = 0
        j = 0
        k = 0

        while i < len(left_side) and j < len(right_side):
            if left_side[i] < right_side[j]:
                list[k] = left_side[i]
                i += 1
            else:
                list[k] = right_side[j]
                j += 1
            k +=1

        while i < len(left_side):
            list[k] = left_side[i]
            i += 1
            k += 1

        while j < len(right_side):
            list[k] = right_side[j]
            j += 1
            k += 1

#helper function for iterative merge sort
def iterative_merge_sort_helper(list, templist, low, mid, high):
    k = low
    i = low
    j = mid + 1

    while i <= mid and j <= high:
        if list[i] < list[j]:
            templist[k] = list[i]
            i += 1
        else:
            templist[k] = list[j]
            j += 1
        k += 1

    while i < len(list) and i <= mid:
        templist[k] = list[i]
        k += 1
        i += 1

    for i in range(low, high + 1):
        list[i] = templist[i]

#iterative merge sort which is a non-recursive, one extra list merge sort
def iterative_merge_sort(list):
    templist = list.copy()
    start = 0
    last = len(list) - 1

    n = 1
    while n <= last - start:
        for i in range(start, last, 2*n):
            low = i
            mid = i + n - 1
            high = min(i + 2*n - 1, last)
            iterative_merge_sort_helper(list, templist, low, mid, high)
        n = 2*n
#partition function for quick sort helper
def partition(list, first, last):
    pivot = list[first]
    low = first + 1
    high = last

    while True:
        while low <= high and list[high] >= pivot:
            high -= 1
        while low <= high and list[low] <= pivot:
            low += 1
        if low <= high:
            list[low], list[high] = list[high], list[low]
        else:
            break

    list[first], list[high] = list[high], list[first]
    return high

#helper function for quick sort
def quick_sort_helper(list, first, last):
   if first >= last:
       return
   p = partition(list, first, last)
   quick_sort_helper(list, first, p-1)
   quick_sort_helper(list, p+1, last)


#quick sort
def quick_sort(list):
    first = 0
    last = len(list) - 1
    quick_sort_helper(list, first, last)


#shell sort
def shell_sort(list):
  size = len(list)
  gap = size // 2
  while gap > 0:
      for i in range(gap, size):
          temp = list[i]
          j = i
          while j >= gap and temp < list[j - gap]:
              list[j] = list[j - gap]
              j -= gap
          list[j] = temp
      if gap == 2:
          gap = 1
      else:
          gap = int(gap / 2.2)
