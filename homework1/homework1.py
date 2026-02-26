# File: homework1. py
# --- Variables and Data Types --- 
a = 10
print(a)
print(type(a)) # a is an integer, a whole number with no decimals.

b = 1.5
print(b)
print(type(b)) # b is a float, a number that contains a decimal point.

c = 3j
print(c)
print(type(c)) # c is a complex number.

d = "hello" 
print(d)
print(type(d)) # d is a string, a collection of characters/words.

e = [1,2,3]
print(e)
print(type(e)) # e is a list, combining multiple items between brackets.

f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f)) # f is a dictionary, used to store data in key-value pairs.

g = (1, 2)
print(g)
print(type(g)) # g is a tuple, used to store a fixed, ordered collection of items.

h = ["apple", "banana", "strawberry"]
print(h)
print(type(h)) # h is a list, just like e. 

i = True
print(i)
print(type(i)) # i is a boolean, a data type that has only two possible values: true or false.

j = None
print(j)
print(type(j)) # j is a nonetype, used to represent the absence of a value or a null object reference.

k = [True, "blue", 12]
print(k)
print(type(k)) # k is a list, just like h and e.

l = str(14)
print(l)
print(type(l)) # l is a string, just like d, but we use a number here instead.

m = 1e4
print(m)
print(type(m)) # m is a float, just like b.

# Question 1: I found 9 data types
'''
Question 2: Integers, floats, complex numbers, strings, lists, dictionaries,
tuples, booleans, and nonetypes.
'''
# Question 3: b and m are floats. d and l are strings. e, h, and k are lists.
'''
Question 4: l is a string because the command str() was used to convert it. 
Str() converts data types like integers, floats, or lists into text 
so they can be printed or joined with other text.
'''
# Question 4 below
n = {"apple", "orange"}
print(n)
print(type(n)) #n is a set, used to store unique items in an unordered manner.

# --- Booleans ---
print(10>9) # True, 10 is greater than 9
print(10 == 9) #False, 10 is NOT equal to 9
print(10 <= 9) #False, 10 is not smaller than or equal to 9
print(bool("abc")) #True, "abc" is a non-empty string
print(bool(123)) #True, 123 is not zero or nothing
print(bool(["apple", "cherry", "banana"])) #True, not an empty list
print(bool(True)) #True, it returns itself lol 
print(bool(False)) #False, it returns itself
print(bool(0)) #False, Python defines 0 as false
print(bool("")) #False, empty string
print(bool(" ")) #True, contains a space
print(bool(())) #False, empty tuple
print(bool([])) #False, empty list
print(bool({})) #False, empty dictionary
#Note: You cannot use {} for an empty set because Python defaults that to an empty dictionary. You need to use the function Set().
print( bool(True and False)) #False, both can't happen simulataneously
print( bool(True and True)) #True, both are the same
print( bool(False and False)) #False but because both are false so it's logical
print(bool(True or False)) #True, they happen exclusively
print(bool(True or True)) #True, it's like saying either 1 or 1
print(bool(False or False)) #False, we get false or false (self-explanatory)
print(bool(not(False))) #True, which is the opposite of False
print(bool(not(True))) #False, the opposite of True

# Question 1: I noticed that Python returns empty values as False, while non-empty ones are True.
# Question 2: I was surprised about the difference between a dictionary and a set in the bool function, as noted in line 86.
# Question 3 below
n = [1, 2]
print(bool(set(n))) #This returns True because it's a non-empty set.
#Question 4 below
print(bool(set())) #False because it's an empty set.

# --- Operators --- 
# Arithmetic
print(10 + 5) #15, + performs addition
print(10 - 5) #5, - performs subtraction
print(2 * 4) #8, * performs multiplication
print(6 / 3) #2, / performs division
print(5 % 2) #1, % performs modulus (used to find the remainder)
print(3 ** 2) #9, ** performs exponentiation
print (15 // 2) #7, // performs floor division (divides two numbers and rounds the result down to the nearest whole integer)

#Comparison
print(5 == 2) #False, == means equal
print(10 !=10) #False, != means not equal
print(2 < 5) #True, 5 is greater than 2
print(12 > 5) #True, 12 is greater than 5
print(5 <= 6) #True, <= means 5 is less than or equal to 6
print(1 >= 10) #False, 1 is NOT greater than or equal to 10

#Assignments
x = 5
x += 5
print(x)
x -= 4
print(x)
x *= 3
print(x)

#Logical
# Q1: "and" returns true only if both are true. It returns false if one side (or both) is false.
print(1 <= 2 and 1 == 1) #True
print(1 >= 2 and 1 <= 2) #False
#Q2: "or" returns true if at least one side is true. It returns false if both sides are false.
print(1 > 2 or 1 == 1) #True
print(1 == 2 or 1 > 2) #False
#Q3: "not" returns the opposite of what's printed. Returns false if something is true and returns true if something is false.
print(not 1 > 2) #True
print (not 1 < 2) #False

#Extra Questions
#Q1: / performs regular division. // performs floor division (divides two numbers and rounds the result down to the nearest whole integer)
#Q2: % performs modulus operation (returns the remainder left over after the division is performed). // performs floor division.
#Q3: I'd use %
print(20 % 9) #Results is 2, which is the remainder.
#Q4: Assignment operators update the variable by performing the operation and assigning the result back to itself


# --- Strings ---
my_string = "hello"
print(my_string) # Prints: hello
print(my_string[0]) # Prints: h
print(my_string[1]) # Prints: e
print(my_string[2]) # Prints: l
print(my_string[3]) # Prints: l
print(my_string[4]) # Prints: o
print(my_string[-1]) # Prints: o
print(my_string[1:3]) # Prints: el
print(my_string[0:5:2]) # Prints hlo
print(len(my_string)) # Prints: 5
print(my_string + "goodbye") # Prints: hellogoodbye
print(my_string * 7) # Prints: hellohellohellohellohellohellohello
#Q1: slicing is a way to extract a portion of a sequenece like a string in our case. print(my_string[0:5:2]) is where I sliced.
#Q2 below
name = "Oski"
print("Hello, my name is", name) # Prints: Hello, my name is Oski
#Q3 below
name = "Oski"
print(f"Hello, my name is {name}") # Prints: exactly as Q2
'''
Q4: The 1st statement joins a string and a variable with a space between them. 
The 2nd statement uses an f-string, where the variable is evaluated inside the string itself before the print() function sees it.
'''

# --- Terminal Commands ---
# cd 
# changes directories. Used to move from one folder to another.
# Example: cd Desktop.

# ls
# lists the contents of a directory
# Example: ls ~ 

# ls -a
# lists all files/directories within current folder, including hidden files
# Example: ls -a ~

# mkdir
# create new directory in the file system
# Example: mkdir astron-98

# cat
# prints out all file contents
# Example: cat homework1.py

# pwd
# displays path of the directory you're currently in
# Example: pwd then press enter

# cd .. 
# moves up one level to the parent directory
# Example: cd .. then press enter

# cd .
# changes current directory to current directory
# Example: cd . then press enter

# cd ~
# takes you back to home directory
# Example: cd ~ 

# cp
# duplicates files and directories from one location to another
# Example: cp python_decal_sp26/homework1.py ~/Desktop/

# mv
# moves files/directories from a location to another and can be used to rename them.
# Example: mv homework1.py ~/Desktop/

# rm
# removes a specific file permanently
# Example: rm homework1.py (skull emoji)

# clear
# empties current view of the terminal (makes screen less cluttered)
# Example: clear then press enter

# grep
# Filters large text files. Used to search for specific text patterns within files or command output.
# Example: grep "hello" homework1.py

#EXTRA Commands and questions below
# man
# Opens the manual (help page for any command)
# Example: man grep

# touch
# Creates a brand new file.
# Example: touch new_script.py

# head
# shows the first few lines of a file
# Example: head -n 5 homework1.py

#Q2: ls lists normal files/directories (hides ones that start with a dot). ls -a shows all.
#Q3: Hidden files are files on the computer that are not visible by default in file managers or through normal browsing.

#Q4 Below
# -r (recursive)
# Tells the command to look into subfolders
# Used with rm, cp, grep

# -i (interactive)
# Forces computer to ask for permission before deleting/overwriting anything
# Used with rm, cp, mv

# -l (long format)
# changes the view of ls from a simple names list to a detailed table
# Example: ls -l 

