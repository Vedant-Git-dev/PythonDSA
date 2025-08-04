# merge two sorted arrays

arr_1 = [1, 3, 5]
arr_2 = [2, 4, 6]

def sort_array(arr_1, arr_2):
    i = j = 0
    merged = []

    while i < len(arr_1) and j < len(arr_2):
        if arr_1[i] < arr_2[j]:
            merged.append(arr_1[i])
            i += 1
        else:
            merged.append(arr_2[j])
            j += 1

    # adding
    merged.extend(arr_1[i:])
    merged.extend(arr_2[j:])

    print(merged)

sort_array(arr_1, arr_2)