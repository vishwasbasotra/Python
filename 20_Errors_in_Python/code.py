def divide(dividend,divisor):
    if divisor == 0:
        raise ZeroDivisionError('Divisor cannot be 0.')
    
    return dividend/divisor

print("Welcome to teh average grade program.")

students = [
    {'name':'rob','grades':[75,98,65]},
    {'name':'mike','grades':[34]},
    {'name':'pal','grades':[68,67,72]}
    ]

try:
    for student in students:
        name = student['name']
        grades = student['grades']
        avg = divide(sum(grades),len(grades))
        print("{n}'s average score: {s}".format(n=name,s=avg))
except ZeroDivisionError as e:
    print('ERROR: {n} has no grades !!!'.format(n=name))
else:
    print("All students average calculated !!!")
finally:
    print('END of Student average calculation !!!')
