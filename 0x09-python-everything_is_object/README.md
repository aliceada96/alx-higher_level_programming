
# 0x09. Python - Everything is object

## Background Context

Now that we understand that everything is an object and have a little bit of knowledge, let’s pause and look a little bit closer at how Python works with different types of objects.

BTW, have you ever modified a variable without knowing it or wanting to? I mean:

```python
>>> a = 1
>>> b = a
>>> a = 2
>>> b
1
>>>
``` 

OK. But what about this?

```python
>>> l = [1, 2, 3]
>>> m = l
>>> l[0] = 'x'
>>> m
['x', 2, 3]
>>> 

```

This project is a little bit different than the usual projects. The first part is only questions about Python’s specificity like “What would be the result of…”. You should read all documentation first (as usual :)), then take the time to think and brainstorm with your peers about what you think and why. Try to do this without coding anything for a few hours.

### Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

#### General

Why Python programming is awesome
What is an object
What is the difference between a class and an object or instance
What is the difference between immutable object and mutable object
What is a reference
What is an assignment
What is an alias
How to know if two variables are identical
How to know if two variables are linked to the same object
How to display the variable identifier (which is the memory address in the CPython implementation)
What is mutable and immutable
What are the built-in mutable types
What are the built-in immutable types
How does Python pass variables to functions

### Requirements

#### Python Scripts

Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
All your files should end with a newline character
The first line of all your script files should be exactly #!/usr/bin/python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the pycodestyle (version 2.8.*)
All your files must be executable
The length of your files will be tested using wc

#### .txt Answer Files

Only one line
No Shebang
All your files should end with a new line

## Tasks

0. Who am I?

What function would you use to get the type of an object?

Write the name of the function in the file, without ().
File: 0-answer.txt
   
1. Where are you?

How do you get the variable identifier (which is the memory address in the CPython implementation)?

Write the name of the function in the file, without ().

File: 1-answer.txt
   
2. Right count

In the following code, do a and b point to the same object? Answer with Yes or No.

```python
>>> a = 89
>>> b = 100
```

File: 2-answer.txt
   
3. Right count =

In the following code, do a and b point to the same object? Answer with Yes or No.

```python
>>> a = 89
>>> b = 89
```

File: 3-answer.txt
   
4. Right count =

In the following code, do a and b point to the same object? Answer with Yes or No.

```python
>>> a = 89
>>> b = a
```

File: 4-answer.txt
   
5. Right count =+

In the following code, do a and b point to the same object? Answer with Yes or No.

```python
>>> a = 89
>>> b = a + 1
```

File: 5-answer.txt
   
6. Is equal

What do these 3 lines print?

```
>>> s1 = "Best School"
>>> s2 = s1
>>> print(s1 == s2)
```

File: 6-answer.txt
   
7. Is the same

What do these 3 lines print?

```python
>>> s1 = "Best"
>>> s2 = s1
>>> print(s1 is s2)
```

GitHub repository: alx-higher_level_programming
Directory: 0x09-python-everything_is_object
File: 7-answer.txt
   
8. Is really equal

What do these 3 lines print?

```python
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 == s2)
```

File: 8-answer.txt
   
9. Is really the same

What do these 3 lines print?

```python
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 is s2)
```

File: 9-answer.txt
   
10. And with a list, is it equal

What do these 3 lines print?

```python
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 == l2)
```

File: 10-answer.txt
   
