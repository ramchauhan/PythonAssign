def insertionSort(list_to_sort):
    """ list_to_sort is the list which needs to be sort, \
        complexity of the sorting is O(n**2)
    """
    for index in range(1, len(list_to_sort)):
        currentval = list_to_sort[index]
        position = index
        while position > 0 and list_to_sort[position - 1] > currentval:
            list_to_sort[position] = list_to_sort[position-1]
            position = position -1

        list_to_sort[position] = currentval
              
list_to_sort = [54,26,93,17,77,31,44,55,20]
insertionSort(list_to_sort)
print list_to_sort
