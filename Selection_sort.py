# Selection sort


def selection_sort(list):
    for i in range(len(list)):
        min_index = i
        for j in range(i+1,len(list)):
            if list[j] < list[min_index]:
                min_index = j
        list[i],list[min_index] = list[min_index],list[i]
            
list = [1,2,3,1,2,5,3,99,33,7,3,1,6,34,6,23,6,3,5]
selection_sort(list)
print(list)
