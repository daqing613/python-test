##age = 20
##if age >= 18:
##    print 'your age is', age
##    print 'adult'
##else:
##    print 'your age is', age
##    print 'teenage'


##def my_abs(x):
##    if not isinstance(x, (int, float)):
##        raise TypeError('bad operand type')
##    if x>= 0:
##        return x
##    else:
##        return -x

##def power(x, n):
##    s = 1
##    while n > 0:
##        n = n - 1
##        s = s * x
##    return s


class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name: %s)' % self.name
    
