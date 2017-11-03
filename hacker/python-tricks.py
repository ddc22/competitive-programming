#http://sahandsaba.com/thirty-python-language-features-and-tricks-you-may-not-know.html

#unpacking
a, b, c = (2 * i + 1 for i in range(3))
a, (b, c), d = [1, (2, 3), 4]
#a, b, c = [1, 2, 3]


#unpackung for swapping
a, b = b, a

#Negative index
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a[-3]
#3rd element from the right


#list slice, a[start:end]
a[2:8]
#element at index 2 included
#element at index 8 not included
#[2, 3, 4, 5, 6, 7]

a[:-1]
#list except last element
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

a[-3:]
#list only last 3 elements
#[8, 9, 10]


#List slices with step (a[start:end:step])
a[::2]
#[0, 2, 4, 6, 8, 10]
a[2:8:2]
#[2, 4, 6]

#insert into list
a = [1, 2, 3, 4, 5]

a[2:3] = [0, 0]
#delete 3rd element and insert [0, 0]
#[1, 2, 0, 0, 4, 5]

a[1:1] = [8, 9]
#insert 8,9 after 1st element location
#[1, 8, 9, 2, 0, 0, 4, 5]

a[1:-1] = []
#remove elements between 0 index and last index


#Iterating over list index and value pairs (enumerate)
for i, x in enumerate(a):
    print '{}: {}'.format(i, x)

#Iterating over dictionary key and value pairs (dict.iteritems)
m = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
for k, v in m.iteritems():
    print '{}: {}'.format(k, v)

#Zipping and unzipping lists and iterables
a = [1, 2, 3]
b = ['a', 'b', 'c']

z = zip(a, b)
#[(1, 'a'), (2, 'b'), (3, 'c')]

zip(*z)
#[(1, 2, 3), ('a', 'b', 'c')]

2**3