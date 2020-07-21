# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    while end >= start:
        # get the middle index
        middle_i = (start + end) // 2

        # compare the middle point's value with the target
        # if middle == target => return True
        if arr[middle_i] == target:
            return middle_i
        
        # move start or end index closer to another
        # to shrink our search space
        else:
            # checking the left
            if arr[middle_i] > target:
                # end = middle_i - 1
                return binary_search(arr, target, start, middle_i - 1)

            # checking the right
            else:
                start = middle_i + 1
                return binary_search(arr, target, middle_i + 1, end)

    return -1

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass