dct =  {123:{"name":"vishnu","semgpa":[6,8,6,8],"cgpa":8},
        524:{"name":"thazeel","semgpa":[8,9,8,9],"cgpa":9},
        789:{"name":"pranoy","semgpa":[9,9,9,9],"cgpa":9.5},
        240:{"name":"albin","semgpa":[9,9,10,9],"cgpa":10},
        }

lst=[]
# converting into a list to sort
for item in dct.keys():
    new_dct = {"rollno":item}
    new_dct.update(dct[item])
    lst.append(new_dct)

# sorting it based on cgpa
def sort(lst):
    sorted_list = sorted(lst, key=lambda report: report["cgpa"],reverse=True) 
    return sorted_list
print(sort(lst))


# add new student
def addStudent(dct,lst):
    lst.append(dct)
    lst = sort(lst)
    return lst
new_student = {"rollno":230,"name":'ab',"semgpa":[7,4,6,2],"cgpa":8.2}

print(addStudent(new_student,lst))
