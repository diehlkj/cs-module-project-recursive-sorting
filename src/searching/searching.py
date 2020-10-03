# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    
        # ? find the middle index of arr in given range
        middle = int((start + end) / 2)
        
        if start <= end:
            if arr[middle] == target:
                return arr.index(target)
            else:
                if target > arr[middle]:
                    # ? search range middle to len(arr) and repeat
                    return binary_search(arr, target, middle, end)
                    
                elif target < arr[middle]:
                    # ? search range 0 to middle and repeat
                    return binary_search(arr, target, start, middle)
        else:
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