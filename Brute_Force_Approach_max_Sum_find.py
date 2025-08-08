# Brute Force Approach
# Find The Max Sum from the Array 



def find_max_sum(arr):
    max_Sum = float("-inf")
    for i in range(len(arr)):
        current_sum = 0
        for j in range(i,len(arr)):
            current_sum += arr[j]
            max_Sum = max(current_sum,max_Sum)
    return max_Sum
            
arr= [-2,-4]
print(find_max_sum(arr))
