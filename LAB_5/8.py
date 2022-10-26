lst = [2,6,1,8]
# sort
def quick_sort(l):
    if len(l) <= 1:
        return l
    else:
        return quick_sort([e for e in l[1:] if e <= l[0]]) + [l[0]] + quick_sort([e for e in l[1:] if e > l[0]])


def max_ele(lst):
    sorted_list = quick_sort(lst.copy())
    return sorted_list[-1]


def min_ele(lst):
    sorted_list = quick_sort(lst.copy())
    return sorted_list[0]  

print(max_ele(lst.copy()))
print(min_ele(lst.copy()))