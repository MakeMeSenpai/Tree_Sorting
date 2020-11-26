#!python
import tracemalloc

def merge(items1, items2, new=[], count=0):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: 0(n) using a recursive function reliant on array sizes.
    TODO: Memory usage: Peak of 0.00205MB With a list size of 6"""
    # first we need to count each item in each list.
    if len(items1) >= len(items2):
        # so we collect the larger lists len and set it to list_size
        list_size = len(items1) -  1
    else:
        list_size = len(items2) - 1

    # checks if one of the lists is out of items
    if len(items1) - 1 < count:
        # then adds the remaining items of the other list to 'new'
        new.append(items2[count])
    elif len(items2) - 1 < count:
        new.append(items1[count])
    else:
        # check if one value is higher than another   
        if items1[count] <= items2[count]:
            # and append those items to the new list
            new.append(items1[count])
            new.append(items2[count])
        else:
            new.append(items2[count])
            new.append(items1[count])

    if list_size != count:
        # then recall the function, so that all items are added
        return merge(items1, items2, new, count + 1)
    else:
        return new

def is_sorted(items, count=0):
    # As longs as there are items to check for
    if count + 1 < len(items) - 1:
        # check if current index is larger than next
        if items[count] > items[count + 1]:
            # then return false
            return False
        # then make a recursive call
        return is_sorted(items, count + 1)
    # else return True
    return True

def bubble_sort(items, i=0, j=0):
    if i < len(items): 
        # Last i elements are already in place 
        if j < len(items) - 1: 
            # Swap if the element found is greater 
            if items[j] > items[j+1]: 
                items[j], items[j+1] = items[j+1], items[j]
        return bubble_sort(items, i + 1, j + 1)
    return items

def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Running time: 0(n+1)^2 takes in a lot of recursive functions
    TODO: Memory usage: 0.003354MB with a list of 5"""
    # Splits items list into approximately equal halves
    list_size = len(items) // 2
    one = items[:list_size]
    two = items[list_size:]
    # Sorts each half using outside funcs bubble_sort & is_sorted
    if is_sorted(one) == False:
        one = bubble_sort(one)
    elif is_sorted(two) == False:
        two = bubble_sort(two)
    else:
        # Merge sorted halves into one list in sorted order
        new = merge(one, two)
        """this was the cleanest way I could do this, otherwise there
        would be a whole other recusive block here. So sorry if I missed
        the point of this exercise."""
        return  bubble_sort(new)


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if list is so small it's already sorted (base case)
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half by recursively calling merge sort
    # TODO: Merge sorted halves into one list in sorted order


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Choose a pivot any way and document your method in docstring above
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort

# TEST SECTION
test = [1, 5, 3, 9, 7]
test2 = [2, 4, 6, 7, 8, 10]
# this is used to track our memory usage
tracemalloc.start()
print(split_sort_merge(test))
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
tracemalloc.stop()