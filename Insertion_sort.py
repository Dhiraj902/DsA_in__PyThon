# insertion  Sort 
def insertion_sort(list):
    for i in range(1,len(list)):
        temp = list[i]
        j= i-1
        while j>=0 and temp< list[j]:
            list[j+1] = list[j]
            j-=1
        list[j+1] = temp


nums = input("Enter integers separated by spaces: ")
data = list(map(int, nums.split()))
insertion_sort(data)
print("Sorted integers:", data)
  
