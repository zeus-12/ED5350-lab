lst = [5,1,8,9,2,1]

# sum 
def sum_list(lst):
    if len(lst) == 0:
        return 0
    return lst.pop() + sum_list(lst)

print(sum_list(lst.copy()))

# sort
def quick_sort(l):
    if len(l) <= 1:
        return l
    else:
        return quick_sort([e for e in l[1:] if e <= l[0]]) + [l[0]] + quick_sort([e for e in l[1:] if e > l[0]])

print(quick_sort(lst))