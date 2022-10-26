# applicable for list but not for tuple
# --> append, clear, copy, extend, insert, pop, remove, reverse, sort

lst = [2,32,1,23]

new_lst = lst.copy()
print(new_lst)

new_lst.pop()
print(new_lst)

new_lst.extend(lst)
print(new_lst)

new_lst.insert(1,20)
print(new_lst)

new_lst.append(10)
print(new_lst)

new_lst.remove(10)
print(new_lst)

new_lst.sort()
print(new_lst)

new_lst.reverse()
print(new_lst)

new_lst.clear()
print(new_lst)