def merge(my_list):
    if len(my_list) < 2:
        return my_list
    result = []
    mid = int(len(my_list)/2)
    p1 = merge(my_list[:mid])
    p2 = merge(my_list[mid:])
    i = 0
    j = 0
    while i < len(p1) and j < len(p2):
        if p1[i] > p2[j]:
            result.append(p2[j])
            j += 1
        else:
            result.append(p1[i])
            i += 1
    # once loop finishes running there is one item
    # left in either p1 or p2
    result += p1[i:]
    result += p2[j:]
    return result

print merge([3,4,5,7,3,4,0,7,3,4])