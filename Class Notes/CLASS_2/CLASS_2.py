name, phone_no, cgpa = input("Enter name, phone_no, cgpa ").split()

phone_no = int(phone_no)
cgpa =  float(cgpa)

print(f"Name:{name}",f"Phone number:{phone_no}",f"cgpa:{cgpa}",sep=", ")

a,b,c = 1,2,3

if a < b< c :
    print("a is the smallest")

# a,b,c = 1,2,3
# print(a,b,c, sep='<', end='\t')

# #format fn
# msg = "hey {x},{y},{z}".format(x='name1',y='name2',z='name3')
# print(msg)
