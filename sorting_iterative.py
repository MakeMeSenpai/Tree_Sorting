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
    TODO: Running time: O(n)^2 due to nested for loop and dependency of length of list
    TODO: Memory usage: Peak of 9.6e-05MB using short array length of 4"""
    # TODO: Repeat until all items are in sorted order
    while is_sorted(items) == False:
        # TODO: Find minimum item in unsorted items
        for i in range(len(items)):
            # creates min index
            min_index = 1
            for j in range(i + 1, len(items)):
                # if item's value is lower than min
                if items[j] < items[min_index]:
                    # add 1 to min
                    min_index = j
                    # TODO: Swap it with first unsorted item
                    items[i], items[min_index] = items[min_index], items[i] 
    return items


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # while is_sorted(items) == False:
    # TODO: Take first unsorted item
    for i in range(len(items)):
        for j in range(len(items) - 1):
            if items[j + 1] < items[j]:
                # TODO: Insert it in sorted order in front of items
                items.insert(0, items[j + 1])
                items.pop(j + 1)
    return items

test = [3, -1, 1, -5]
print(insertion_sort(test))
# this is used to track our memory usage
tracemalloc.start()
insertion_sort(test)
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
tracemalloc.stop()