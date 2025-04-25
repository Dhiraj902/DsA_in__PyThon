# Modifi Bubble Sort

def m_bubble_sort(list):
    for i in range(1,len(list)):
        flag = False
        for j in range(len(list)-i):
            flag = False
            if list[j]>list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]
                flag = True
        if flag is False:
            break
choice = input("Do you want to sort integers or strings? (int/str): ").strip().lower()

if choice == "int":
    nums = input("Enter integers separated by spaces: ")
    data = list(map(int, nums.split()))
    m_bubble_sort(data)
    print("Sorted integers:", data)
  
elif choice == "str":
    words = input("Enter strings separated by spaces: ")
    data = words.split()
    m_bubble_sort(data)
    print("Sorted strings:", data)

else:
    print("Invalid choice! Please enter 'int' or 'str'.")
