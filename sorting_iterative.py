#!python
import tracemalloc

def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: O(n) becuase the time complexity depends on the length of the list
    TODO: Memory usage: Peak of 9.6e-05MB using short array length of 4"""
    # TODO: Check that all adjacent items are in order, return early if sorted
    # grabs an index variable
    for i in range(len(items) - 1):
        # print(f"{items[i]} <= {items[i + 1]}")
        # checks if list is sorted least to greatest
        if items[i] > items[i + 1]:
            # if current index is larger then next return false
            return False
    # else return true
    return True


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: O(n)^2 due to nested for loop and dependency of length of list
    TODO: Memory usage: Peak of 9.6e-05MB using short array length of 4"""
    # TODO: Repeat until all items are in sorted order
    while is_sorted(items) == False:
        # TODO: sort the list
        for i in range(len(items) - 1): 
            # Last i elements are already in place 
            for j in range(0, len(items) - i - 1): 
                # Swap if the element found is greater 
                if items[j] > items[j+1]: 
                    items[j], items[j+1] = items[j+1], items[j]
    return items



def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # while is_sorted(items) == False:
    # checks the first index
    min = items[0]
    count = 0
    for i in range(count, len(items)):
        # TODO: Find minimum item in unsorted items
        for j in range(len(items)):
        # if item's value is lower than min
            if items[j] < min:
                # TODO: Swap it with first unsorted item
                # new minimume is set to item[j]s's vale
                # item[i + 1] is set to old min
                min, items[i + 1] = items[j], min
                # first index is change to minimum value
                items[0] = min
                print(items)
    return items


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items

test = [3, 0, 1, -5]
print(selection_sort(test))
# this is used to track our memory usage
tracemalloc.start()
selection_sort(test)
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
tracemalloc.stop()