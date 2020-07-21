# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # elements = len(arrA) + len(arrB)
    merged_arr = []

    # Your code here
    # start the pointer for both arrs
    a, b = 0, 0

    # check if a and b is still in range of its array
    # if so, compare their first value, if arrA[a] > arrB[b]
    # append the smaller value to the merged_arr
    # increase that index and keep going
    while a < len(arrA) and b < len(arrB):
        if arrA[a] < arrB[b]:
            merged_arr.append(arrA[a])
            a += 1
        else:
            merged_arr.append(arrB[b])
            b += 1

    # if either one indexes reach their length of the array
    # that means it ran out of item to compare.
    # Now we can just extends the list with the remaining
    # of the other array
    if a == len(arrA):
        merged_arr.extend(arrB[b:])
    else:
        merged_arr.extend(arrA[a:])

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):

    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]

    # break down the array until they only have 1 item in it
    if len(arr) == 1:
        return arr

    # if len(arr) != 1, keep sorting on both left and right
    elif len(arr) > 1:
        left = merge_sort(left_arr)
        right = merge_sort(right_arr)

        # return the merge value of each left and right
        return merge(left, right)
    
    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass

def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

# print(merge([1, 4, 9, 14], [1, 3, 5, 7, 11, 13, 15]))