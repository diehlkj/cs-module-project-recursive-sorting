# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here


    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    # ? is array length greater than 1?
        # * Recursive Part
        # ? find middle of array
        # ? left = call merge_sort on arr[:middle] (left side)
        # ? right = call merge_sort on arr[middle:] (right side)

        # * Sorting Part
        # ? def Left iterate
        # ? def Right iterate
        # ? def arr insertion point
            # * Sort L & R
        # ? while L < len(left) and R < len(right):
            # ? check left < right:
                # ? insert left into arr at insertion point
                # ? left iterate += 1
            # ? else:
                # ? insert right into arr at insertion point
                # ? right iterate += 1
            # ? insertion point += 1
            
            # * Insert any remaining L & R values bc first while loop only runs until L or R equates to respective length
            # * These remaining values should already be in order
        # ? while left iterate less than len of left arr
            # ? insert left in arr at insertion point
            # ? left iterate += 1
            # ? insertion point += 1
            
        # ? while right iterate less than len of right arr
            # ? insert right in arr at insertion point
            # ? right iterate += 1
            # ? insertion point += 1
            
    if len(arr) > 1:
        middle = int(len(arr) / 2)
        left = merge_sort(arr[:middle])
        right = merge_sort(arr[middle:])
        
        L = 0   # ? def Left iterate for returned left arr index
        R = 0   # ? def Right iterate for returned right arr index
        i = 0   # ? def arr insertion point
        
        while L < len(left) and R < len(right):
            if left[L] < right[R]:
                arr[i] = left[L]
                L += 1
            else:
                arr[i] = right[R]
                R += 1
            i += 1
            
        while L < len(left):
            arr[i] = left[L]
            L += 1
            i += 1
        while R < len(right):
            arr[i] = right[R]
            R += 1
            i += 1
    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input

# def merge_in_place(arr, start, mid, end):
    # Your code here



# def merge_sort_in_place(arr, l, r):
    # Your code here

