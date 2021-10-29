def my_func(somvalue='no value'):
    """
    This function does stuff, handle with care
    """
    print("i called a function with {}".format(somvalue))

s = 'django'
print('problem 1')
print(s[0])
print(s[-1])
print(s[:4])
print(s[4:])
print(s[::-1])
print("this text has {a}".format(a='format'))

if 1<2:
    print("1 is smaller than 2")
    print("this is another comment")
elif 1==1:
    print('one equals one')
else:
    print("1 is larger than 2")
sequence = [1,2,3,4,5,6,7,8,9]
for i in sequence:
    print("this loop has been running {a} times".format(a=i))

d={'hey':3,'there':2,'buddy':1}
for item in d:
    print("keys are {a}".format(a=item))
    print("values are {b}".format(b=d[item]))

my_func('a value')
