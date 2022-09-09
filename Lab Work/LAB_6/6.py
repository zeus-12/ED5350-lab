class Department:
    def __init__(self, dname):
        self._deptname = dname

    def print_dept(self):
        print("Department Name :", self._deptname)


class Faculty:
    def __init__(self, dept, fname, fid):
        self._fname = fname
        self._fid = fid
        self._dobj = Department(dept)

    def print_faculty(self):
        print("Faculty Name :", self._fname, "\nFaculty ID :", self._fid)
        self._dobj.print_dept()


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


s = Student("Vishnu", 'ED20B073', 'ED', 'Raman', '1234')
s.print_student()
