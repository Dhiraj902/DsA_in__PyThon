# Quick Sort using Recursion


def Quick_sort(list):
    l = len(list)
    if l <=1:
        return list
    else:
        pivote = list[0]
        lesser = [x for x in list[1 :] if x <= pivote]
        greter =[ x for x in list[1:] if x >pivote]
        return Quick_sort(lesser)+ [pivote] + Quick_sort(greter)
    
input = print("Enter the element here: ")
list = list(map(int,input.split()))
list = Quick_sort(list)
print(list)
