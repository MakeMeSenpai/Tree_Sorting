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
    TODO: Running time: 0(n) becuase no nested loops
    TODO: Memory usage: 0.000938MB for list size of 5"""
    if len(items) > 1:
 
        # Finding the mid of the array
        split = len(items)//2
 
        # Dividing the array elements
        L = items[:split]
 
        # into 2 halves
        R = items[split:]
 
        # Sorting the first half
        merge_sort(L)
 
        # Sorting the second half
        merge_sort(R)
 
        i = j = k = 0
 
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                items[k] = L[i]
                i += 1
            else:
                items[k] = R[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(L):
            items[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            items[k] = R[j]
            j += 1
            k += 1
    # couldn't figure out how to do recursively
    return items


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (chose Median-of-Three because it was
    most optimal, along with the lomuto partial algorithm) from that range,
    moving pivot into index `p`, items less than pivot into range 
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: Peak was 0.000458MB using array length of 6"""
    # choose a pivot point
    midean = (low + high) // 2
    if items[midean] < items[low]:
        # swap items[low] with items[midean]
        items[low], items[midean] = items[midean], items[low]
    if items[high] < items[low]:
        # swap items[low] with items[high]
        items[low], items[high] = items[high], items[low]
    if items[midean] < items[high]:
        # swap items[mid] with items[hi]
        items[midean], items[high] = items[high], items[midean]
    pivot = items[high]

    # Loop through all items in range [low...high]
    i = low
    for j in range(low, high):
        # Move items less than pivot into front of range [low...p-1]
        if items[j] < pivot:
            # swap items[i] with items[j]
            items[i], items[j] = items[j], items[i]
            i = i + 1
        # Move pivot item into final position [p] and return index p
        # swap items[i] with items[high]
        items[i], items[high] = items[high], items[i]
    # print(items)
    return i

def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # Check if list or range is so small it's already sorted (base case)
    if len(items) <= 1:
        return items
    # Partition items in-place around a pivot and get index of pivot
    p = partition(items, low, high)
    # Sort each sublist range by recursively calling quick sort
    quick_sort(items, low, p-1)
    quick_sort(items, p+1, high)

""" my attempt at returning a list """
# def quick_sort(items, low=None, high=None):
#     # created to return list
#     new_list = []

#     # Check if high and low range bounds have default values (not given)
#     if low == None and high == None:
#         low = 0
#         high = len(items) - 1

#     # calls quick sort
#     for i in range(high):
#         new_list.append(quick_sorter(items, low, high))
    
#     # returns our list
#     return new_list
            

# TEST SECTION
test = [1, 5, 3, 9, 7]
test2 = [2, 4, 6, 7, 8, 10]
# this is used to track our memory usage
tracemalloc.start()
print(quick_sort(test, 0, 4))
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
tracemalloc.stop()