# What are the data structures?
***
They are a way of organizing data and are directly tied of how we access and retrieve them.
1. Different Data Structures have different Ups & Downs.

# Lists
List are arrays, ordered collections of data.
```
List = [a,a,a,a,a,a]
```

### Operations containing Lists
```python
# Creating a List with
# the use of multiple values
List = ["Geeks", "For", "Geeks"]
print("\nList containing multiple values: ")
print(List)

# Creating a Multi-Dimensional List
# (By Nesting a list inside a List)
List2 = [['Geeks', 'For'], ['Geeks']]
print("\nMulti-Dimensional List: ")
print(List2)

# accessing a element from the
# list using index number
print("Accessing element from the list")
print(List[0])
print(List[2])

# accessing a element using
# negative indexing
print("Accessing element using negative indexing")
	
# print the last element of list
print(List[-1])
	
# print the third last element of list
print(List[-3])
```
**Output**
```bash
List containing multiple values: 
['Geeks', 'For', 'Geeks']

Multi-Dimensional List: 
[['Geeks', 'For'], ['Geeks']]
Accessing element from the list
Geeks
Geeks
Accessing element using negative indexing
Geeks
Geeks
```

***
# Dictionary
***
Dictionary in python are hash tables, and have a time complexity of $O(1)$, which means they are  **FAST**, they hold a key-value pair, keys are immutable and unique.

### Operations and Examples
```python
# DICTONARY SYNTAX
Dict= {key:value}

"""EXAMPLES"""
# Creating a Dictionary
Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]}
print("Creating Dictionary: ")
print(Dict)

# accessing a element using key
print("Accessing a element using key:")
print(Dict['Name'])

# accessing a element using get()
# method
print("Accessing a element using get:")
print(Dict.get(1))

# creation using Dictionary comprehension
myDict = {x: x**2 for x in [1,2,3,4,5]}
print(myDict)
```

**Output**:
```bash
Creating Dictionary: 
{'Name': 'Geeks', 1: [1, 2, 3, 4]}
Accessing a element using key:
Geeks
Accessing a element using get:
[1, 2, 3, 4]
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```
***
# Tuples
Tuples are python immutable lists, which means that any value that they will remain untouched. 

### Examples and Operations
```python
# Creating a Tuple with
# the use of Strings
Tuple = ('Geeks', 'For')
print("\nTuple with the use of String: ")
print(Tuple)
	
# Creating a Tuple with
# the use of list
list1 = [1, 2, 4, 5, 6]
print("\nTuple using List: ")
Tuple = tuple(list1)

# Accessing element using indexing
print("First element of tuple")
print(Tuple[0])

# Accessing element from last
# negative indexing
print("\nLast element of tuple")
print(Tuple[-1])

print("\nThird last element of tuple")
print(Tuple[-3])
```
**Output:**
```shell
Tuple with the use of String: 
('Geeks', 'For')

Tuple using List: 
First element of tuple
1

Last element of tuple
6

Third last element of tuple
4
```
***
# Sets

Python sets are a version of of dictionaries without Key-Values pair. They use hashing as well. There are multiple implementations and use cases of sets due its high optimized performance.
**Implementation of a Set**
![[HashTable.png]]
**Set with numerous operations**
![[Hasing-Python.png]]
### Examples and Operations
```python
# Creating a Set with
# a mixed type of values
# (Having numbers and strings)
Set = set([1, 2, 'Geeks', 4, 'For', 6, 'Geeks'])
print("\nSet with the use of Mixed Values")
print(Set)

# Accessing element using
# for loop
print("\nElements of set: ")
for i in Set:
	print(i, end =" ")
print()

# Checking the element
# using in keyword
print("Geeks" in Set)
```
**Output:**
```shell
Set with the use of Mixed Values
{1, 2, 'Geeks', 4, 6, 'For'}

Elements of set: 
1 2 Geeks 4 6 For 
True
```
