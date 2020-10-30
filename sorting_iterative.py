#!python
import tracemalloc

def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: O(n) becuase the time complexity depends on the length of the list
    TODO: Memory usage: Peak of 9.6e-05MB using short array length of 4 """
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
    TODO: Memory usage: Peak of 0.000144MB using short array length of 4"""
    # TODO: sort the list
    n = len(items) 

    for i in range(n - 1): 
        # Last i elements are already in place 
        for j in range(0, n - i - 1): 
            # Swap if the element found is greater 
            if items[j] > items[j+1] : 
                items[j], items[j+1] = items[j+1], items[j]
    # TODO: Repeat until all items are in sorted order
        if is_sorted(items) == True:
            return items



def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    

    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items

test = [3, 0, 1, 5]
print(bubble_sort(test))
# this is used to track our memory usage
tracemalloc.start()
bubble_sort(test)
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
tracemalloc.stop()