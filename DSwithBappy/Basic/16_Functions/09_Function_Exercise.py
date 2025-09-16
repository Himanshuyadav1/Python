"""
Problem-1: Write a Python function that takes a list and return a new list with unique elements of the first list.

Example:

input: [1, 2, 3, 3, 3, 3, 4, 4, 4, 5]
output: [1, 2, 3, 4, 5]
"""
print("Problem-1:")

def unique_elements(L):
    result = []
    for element in L:
        if element not in result:
            result.append(element)
    return result

print(unique_elements([1, 2, 3, 3, 3, 3, 4, 4, 4, 5])) 

print()

"""
Problem-2: Write a Python function that accepts a hyphen-separated sequence of words as parameter and returns the words in a hyphen-separated sequence after sorting them alphabetically.

Example:

input: green-red-yellow-black-white
output: black-green-red-white-yellow
"""

print("Problem-2:")

def sorted_hyphen_separated_words(words):
    if words.find("-") == -1:
        return "Please provide hyphen-separated words"
    else:
        L = words.split("-")
        L.sort()
        s = "-"
        return s.join(L)
    

result = sorted_hyphen_separated_words("green-red-yellow-black-white")
print(result)

print()

"""
Problem-3: A dictionary contains following information about 5 employees:

* First name
* Last name
* Age
* Grade(Skilled, Semi-Skilled, Highly-Skilled)

Write a program using map/filter/reduce to a list of employees(first name + last name) who are Highly-Skilled

"""

print("Problem-3:")

employees = [
    {
        'fname': 'Bappy',
        'lname': 'Ahmed',
        'age': 33,
        'grade': 'Skilled'
    },
    {
        'fname': 'Alex',
        'lname': 'Musk',
        'age': 34,
        'grade': 'Semi-Skilled'
    },
    {
        'fname': 'Bunny',
        'lname': 'Singh',
        'age': 35,
        'grade': 'Highly-Skilled'
    },
    {
        'fname': 'Anurag',
        'lname': 'Kumar',
        'age': 30,
        'grade': 'Skilled'
    },
    {
        'fname': 'Abhinav',
        'lname': 'Sharma',
        'age': 37,
        'grade': 'Highly-Skilled'
    }
]


filtered_emp = filter(lambda employee: employee if employee['grade'] == 'Highly-Skilled' else None, employees)
# filtered_emp = filter(lambda employee: True if employee['grade'] == 'Highly-Skilled' else False, employees)

result = map(lambda employee: employee['fname'] + " " + employee['lname'], list(filtered_emp))

print(list(result))

# https://www.hackerrank.com/