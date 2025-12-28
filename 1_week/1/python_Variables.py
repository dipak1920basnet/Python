x = 5
name = "Samantha"
print(x)
print(name)

#  Assigning Values to Variables
x = 5
y = 3.14
z = "Hi"


"""

 Python variables are dynamic typing 
 it means same variables can hold different types of values


"""


# Multiple Assignments 
# assigning same values
a = b = c = 100


# assigning multiple values 

x,y,z = 1,2.5, "Python"

print(x)
print(y)
print(z)

print(x,y,z)


# Type casting a variables 
s = "10"  
n = int(s) 
cnt = 5
f = float(cnt)  
age = 25
s2 = str(age)  

print(n)  
print(f)  
print(s2)


# Getting the types of a variables 

n = 42
f = 3.14
s = "Hello, World!"
li = [1, 2, 3]
d = {'key': 'value'}
bool = True

print(type(n))
print(type(f))
print(type(s))
print(type(li))
print(type(d))
print(type(bool))

# Delete the variable with del key word

x = 10
print(x)
del(x)
