# Nested Functions
print('Nested Functions')

print("Case 1")
def f():
    def g():
        print('Inside function g')
    print('Inside function f')

f() # Inside function f

print()

print("Case 2")
def f():
    def g():
        print('Inside function g')
    g() 
    print('Inside function f')

f() 
# Inside function g
# Inside function f

print()

print("Case 3")
def f():
    def g():
        print('Inside function g')
        f()
    g()
    print('Inside function f')

# f() # RecursionError: maximum recursion depth exceeded
print("RecursionError: maximum recursion depth exceeded")