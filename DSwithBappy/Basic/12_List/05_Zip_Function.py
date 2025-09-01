"""
Zip

The zip() function returns a zip object, which is an iterator of tuples where the first item in each passes iterator is paired together, and then the second item in each passed iterator are paired together.

If the passed iterators have different lengths, the iterator with the least items decides the length of the new iterator.
"""

L1 = [1, 2, 3, 4]
L2 = [5, 6, 7, 8]

print(zip(L1, L2)) # <zip object at 0x0000018B8ED29BC0>
print(list(zip(L1, L2))) # [(1, 5), (2, 6), (3, 7), (4, 8)]
print(list(zip(L2, L1))) # [(5, 1), (6, 2), (7, 3), (8, 4)]

print()

roll_number = [1, 2, 3, 4, 5]
student_name = ['Ram', 'Shyam', 'Shiv', 'Hari', 'Vishnu']

print(list(zip(roll_number, student_name))) # [(1, 'Ram'), (2, 'Shyam'), (3, 'Shiv'), (4, 'Hari'), (5, 'Vishnu')]

print()

L1 = [1, 2, 3, 4]
L2 = [5, 6, 7, 8]

LC1 = [i - j for i, j in zip(L1, L2)]
LC2 = [i - j for i, j in zip(L2, L1)]

print(LC1) # [-4, -4, -4, -4]
print(LC2) # [4, 4, 4, 4]

print()

L1 = [1, 2, 3, 4]
L2 = [5, 6, 7, 8]
L3 = [9, 10, 11, 12]

print(list(zip(L1, L2, L3))) # [(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]

print()

L1 = [1, 2, 3, 4]
L2 = [5, 6, 7, 8]
L3 = [9, 10, 11]

print(list(zip(L1, L2, L3))) # [(1, 5, 9), (2, 6, 10), (3, 7, 11)]

print()

L1 = [1, 2, 3, 4]
L2 = [5, 6, 7, 8]
L3 = [9, 10]

print(list(zip(L1, L2, L3))) # [(1, 5, 9), (2, 6, 10)]

print()

L1 = [1, 2, 3, 4]
L2 = [5, 6, 7, 8]

print(zip(L1, L2)) # <zip object at 0x000001644F487980>

for i in zip(L1, L2):
    print(i)
"""
(1, 5)
(2, 6)
(3, 7)
(4, 8)
"""