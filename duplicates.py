list1 = [2, 5, 3, 5, 7, 1, 7]
unique_list = []
for i in list1:
    if i not in unique_list:
        unique_list.append(i)
print(unique_list)