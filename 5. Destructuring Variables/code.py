x = 5,11
a, b = x

print(a,b,'\n')

student_attendence = {'rolf':96,'bob':80,'anne':100}

for student,attendence in student_attendence.items():
    print('{}:{}'.format(student,attendence))

people = [('bob',42,'mechanic'),('james',24,'artist'),('harry',30,'lecturer')]

for name,age,profession in people:
    print('{n} is {a} years old, working as {p}'.format(n=name,a=age,p=profession))

# _ is used when you don't want to use a value
person = ('bob',42,'mechanic')
name, _, profession = person

head, *tail = [1,2,3,4,5]
print(head)
print(tail)

*head, tail = [1,2,3,4,5]
print('\n',head)
print(tail)