class Department:
    def __init__(self, dname):
        self._deptname = dname

    def print_dept(self):
        print("Department Name :", self._deptname)

    def ret_d(self):
        return self._deptname

class Faculty:
    def __init__(self, dept, fname, fid):
        self._fname = fname
        self._fid = fid
        self._dobj = Department(dept)

    def print_faculty(self):
        print("Faculty Name :", self._fname, "\nFaculty ID :", self._fid)
        self._dobj.print_dept()

    def ret_f(self):
        return self._fname

    def ret_obj(self):
        return self._dobj


class Student:
    def __init__(self, sname, sid, dept, fname, fid):
        self._name = sname
        self._stuid = sid
        self._stuobj = Faculty(dept, fname, fid)

    def print_student(self):
        print("Name :", self._name)
        print("ID :", self._stuid)
        print("Faculty Details\n")
        self._stuobj.print_faculty()

    def ret_name(self):
        return self._name

    def ret_fname(self):
        return self._stuobj.ret_f()

    def ret_dname(self):
        return self._stuobj.ret_obj().ret_d()


class Child(Student, Faculty, Department):
    def __init__(self, sname, sid, dept, fname, fid):
        super().__init__(sname, sid, dept, fname, fid)


a = Child('Vishnu', 'ED20B073', 'ED', 'ABC', '123')
b = Child('Sharath', 'NA20B072', 'NA', 'DEF', '345')
c = Child('Thazeel', 'ED20B069', 'ED', 'GHI', '456')

lst = [a, b, c]
res_stuname = []
res_facname = []

d = input("Enter Dept : ")

for i in lst:
    if i.ret_dname() == d:
        res_stuname.append(i.ret_name())
        res_facname.append(i.ret_fname())

print(res_stuname, res_facname)
