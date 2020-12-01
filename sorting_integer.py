#!python
import tracemalloc

def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: 0(n+k) becuase there is usage of multiple for loops 
    traversing threw multiple lists, however they are not nested.
    TODO: Memory usage: Peak was 0.00057MB with list of 12"""
    # Find range of given numbers (minimum and maximum integer values)
    minimum = [0] # min(numbers)
    maximum = len(numbers) + 1 # max(numbers)
    # Create list of counts with a slot for each number in input range
    count_list = minimum * maximum
    # Loop over given numbers and increment each number's count
    for i in numbers:
        count_list[i] += 1
    # Loop over counts and append that many numbers into output list
    nums_before = 0
    for i, count in enumerate(count_list):
        count_list[i] = nums_before
        nums_before += count 
    # FIXME: Improve this to mutate input instead of creating new output list
    new_list = [None] * len(numbers)
    for i in numbers:
        new_list[ count_list[i] ] = i
        count_list[i] += 1
    
    return new_list

def insertion_sort(items):
    for i in range(len(items)):
        for j in range(len(items) - 1):
            if items[j + 1] < items[j]:
                items.insert(0, items[j + 1])
                items.pop(j + 2)
    return items

def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: O(n^2 + k) nested for loops and traversing 
    over multiple lists. Best case would be 0(n)
    TODO: Memory usage: Peak was 0.00101MB with a list of 10"""
    # TODO: Find range of given numbers (minimum and maximum values)
    # Create list of buckets to store numbers in subranges of input range
    buckets = [[]] * num_buckets #[[], [], [], ...]
    # Loop over given numbers and place each item in appropriate bucket
    for num in range(len(numbers)):
        buckets[num].append(numbers[num])
    # Sort each bucket using any sorting algorithm (recursive or another)
    for bucket in range(num_buckets):
        buckets[bucket] = insertion_sort(buckets[bucket])
    # Loop over buckets and append each bucket's numbers into output list
    count = 0
    for i in range(num_buckets):
        for j in range(len(buckets[i])):
            if count < num_buckets:
                numbers[count] = buckets[i][j]
                count += 1
    # Improve this to mutate input instead of creating new output list
    return numbers



# TEST SECTION
test = [3, 1, 1, 2, 5, 2, 3, 4, 4, 12]
# this is used to track our memory usage
tracemalloc.start()
print(bucket_sort(test))
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
tracemalloc.stop()
