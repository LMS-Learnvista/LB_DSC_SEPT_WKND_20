#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Declare a string and store it in a variable. 
str1 = 'Data Science'


#Check the type and print the id of the same.
print(str1, type(str1), id(str1))


# In[ ]:


#Which are valid/invalid strings
1. 'This is Python class'
valid/invalid - valid

2. "This is Python class"
valid/invalid - valid

3. '''This is Python class'''
valid/invalid - valid

4. """This is Python class"""
valid/invalid - valid

5. 'This is Python's class'
valid/invalid - invalid

6. "Learnbay provides "Java", "Python" classes"
valid/invalid - invalid

7. "Learnbay provides 'Java', 'Python' classes"
valid/invalid - valid

8. "This is Python's class"
valid/invalid - valid

9. """Learnbay provides "Java", "Python" classes"""
valid/invalid - valid

10. '''Learnbay provides "Java", "Python" classes'''
valid/invalid - valid

11. '''Learnbay provides
"Java", "Python" 
classes'''
valid/invalid - valid

12. 'This is
Python 
class'
valid/invalid - invalid


# In[3]:


#Write the code to get the output mentioned below print statement
my_str = "Although that way may not be obvious at first unless you're Dutch."
my_str1 = "Although that way may not be obvious at first unless you're Dutch."

print('The length of my_str is', len(my_str))
#output:- The length of my_str is 66

print('id of my_str and my_str1 is same? - ',id(my_str)!=id(my_str1))
#output:- id of my_str and my_str1 is same? - True

print('Type of my_str is: ', type(my_str))
#output:- Type of my_str is: str


# In[14]:


#Indexing
my_str = "Although 8 that way may not be obvious at first unless you're Dutch"
#Write the code to get the output,instructions are mentioned below print statement. use indexing

print('The first character in my_str is:', my_str[0])
#output:- The first character in my_str is: A
#Note:- Use positive indexing

print('The first character in my_str is:', my_str[-len(my_str)])
#output:- The first character in my_str is: h
#Note:- Use len() function.

print('The character at index 10 in my_str is:', my_str[10])
#output:- The character at index 10 in my_str is: c
#Note:- Use positive indexing

print('The last character in my_str is:', my_str[-1])
#output:- The last character in my_str is: h
#Note:- Use negative indexing.

print('he last character in my_str is:', my_str[len(my_str)-1])
#output:- The last character in my_str is: h
#Note:- Use len() function.

# print(my_str.find('8'))
print('The character in my_str is:', my_str[9] )
#output:- The character in my_str is: 8
#Note:- Use positive index


# In[63]:



#Slicing
my_str = "Although that way may not be obvious at first unless you're Dutch."
#Write the code to get the output,instructions are mentioned below print statement. use slicing
print('You have sliced:', my_str)
#output:- You have sliced: Although that way may not be obvious at first unless you're Dutch.Without begin, end and step


print('You have sliced:', my_str[0:(len(my_str))])
#output:- You have sliced: Although that way may not be obvious at first unless you're Dutch.with begin as 0 end using len and without step


print('You have sliced:', my_str[::1])
#output:- You have sliced: Although that way may not be obvious at first unless you're Dutch.without begin and end but using step

# print(len(my_str))
print('You have sliced:', my_str[0:66:1])
#output:- You have sliced: Although that way may not be obvious at first unless you're Dutch.With begin, end and step


print('You have sliced:', my_str[0:66:-1])
#output:- You have sliced:   .with using begin and end using postive values and step as negative values.
#Slicing command should print empty string.


print('You have sliced:', my_str[0:66:2])
#output:- You have sliced: Atog htwymyntb biu tfrtuls o'eDth


print('You have sliced:', my_str[0:66:3])
#output:- You have sliced: Ahgttam tebo  r lsorDc


print('You have sliced:', my_str[::-1])
#output:- You have sliced: .hctuD er'uoy sselnu tsrif ta suoivbo eb ton yam yaw taht hguohtlA. Use only step


print('You have sliced:', my_str[-1:-67:-1])
#output:- You have sliced: .hctuD er'uoy sselnu tsrif ta suoivbo eb ton yam yaw taht hguohtlA. Use begin end and step.


print('You have sliced:', my_str[::-2])
#output:- You have sliced: .cu ruysen si asovoe o a a athuhl. use only step


print('You have sliced:', my_str[-1:-67:-2])
#output:- You have sliced: .cu ruysen si asovoe o a a athuhl. use begin, end and step.


print(my_str[10:18:-1])
#What will be the output?
#Ans. - output will be an empty string

# print(my_str.find('y'))
print('You have sliced:', my_str[16:10:-1])
#output:- You have sliced: yaw ta, Using begin, end and step.

# print(my_str.find('ess'))
print('You have sliced:', my_str[49:56:1])
#output:- You have sliced: ess you. Using begin, end and step.


# In[66]:


#Basic operation on string
str1 = 'Learnbay'
str2 = 'Python'

#Write the code to get the output,instructions are mentioned below.
print(str1 + ' ' + str2)
#Output is: Learnbay Python


#Error: TypeError: can only concatenate str (not "int") to str


#Error: TypeError: can only concatenate str (not "float") to str



#Find below Output
print(str1 * 3)
#Output is: LearnbayLearnbayLearnbay


#Error: TypeError: can't multiply sequence by non-int of type 'float'


#Error: TypeError: can't multiply sequence by non-int of type 'str'


# In[72]:


#Find below Output
str1 = 'Python'
str2 = 'Python'
str3 = 'Python$'
str4 = 'Python$'

#print True by using identity operator between str1 and str2
print(id(str1)==id(str2))


#print False by using identity operator between str1 and str3
print(id(str1)!=id(str2))


#print False by using identity operator between str4 and str3
print(id(str3)==id(str4))


#Check if P is available in str1 and print True by using membership operator
print('P' in str1)


#Check if $ is available in str3 and print True by using membership operator
print('$' in str3)


#Check if N is available in str3 and print False by using membership operator
print('N' in str3)



# In[81]:


#Complete the below code
str1 = 'This is Python class'
#write the code to replace 'Python' with 'Java' and you should get below error.
#TypeError: 'str' object does not support item assignment.
str1[8:14]= 'Java'


# In[85]:


str1 = 'A'
str2 = 'A'
#Compare str1 and str2 and print True using comparison operator
print(str1<=str2)

#Compare str1 and str2 and print True using equality operator
print(str1==str2)

#Compare str1 and str2 and print False using equality operator
print(str1!=str2)

#Compare str1 and str2 and print False using comparison operator
print(str1<str2)


# In[89]:


str1 = 'A'
str2 = 'a'
#Compare str1 and str2 and print True using comparison operator
print(str1<str2)

#Compare str1 and str2 and print True using equality operator
print(str1!=str2)

#Compare str1 and str2 and print False using equality operator
print(str1==str2)

#Compare str1 and str2 and print False using comparison operator
print(str1>str2)


# In[96]:


str1 = 'A'
str2 = '65'
#Compare str1 and str2 using comparison operator and it should give below error.
# Ans. - print(str1>=int(str2)) - I have commented it so that next line can run.
#Error: TypeError: '>=' not supported between instances of 'str' and 'int'

#Compare str1 and str2 and print True using equality operator
print(str1!=str2)

#Compare str1 and str2 and print False using equality operator
print(str1==str2)


# In[4]:


str1 = 'Python'
str2 = 'Python'
#Compare str1 and str2 and print True using comparison operator
print(str1<=str2)

#Compare str1 and str2 and print True using equality operator
print(str1==str2)

#Compare str1 and str2 and print False using equality operator
print(str1<str2)

#Compare str1 and str2 and print False using comparison operator
print(str1!=str2)


# In[17]:


str1 = 'Python'
str2 = 'python'

#Compare str1 and str2 and print True using comparison operator
print(str1<=str2)

#Compare str1 and str2 and print True using equality operator
print(str1!=str2)

#Compare str1 and str2 and print False using equality operator
print(str1==str2)

#Compare str1 and str2 and print False using comparison operator
print(str1>str2)


# In[18]:


a = 'Python'
b = ''

#Apply logical opereators (and, or & not) on above string values and observe the output.
print(a=='Python' and b=='')
print(not a=='Python' and b=='')
print(not a=='Python' or b=='')
print(a=='Pthon' or b=='')
print(a=='Python' and not b=='')


# In[21]:


a = ''
b = ''

#Apply logical opereators (and, or & not) on above string values and observe the output.
print(a=='' and b=='')
print(not a=='' and b=='')
print(a=='' or not b=='')


# In[24]:


a = 'Python'
b = 'learnbay'

#Apply logical opereators (and, or & not) on above string values and observe the output.
print(a=='Python' or not b=='learnbay')
print(a=='Python' and not b=='learnbay')
print(a=='Python' or b=='learnbay')


# In[58]:


my_str = "Although 8 that way may not be obvious at first unless you're Dutch"

#Write the code to get the total count of 't' in above string. Use find() and index() method.
print(my_str.find('t')), print(my_str.find('t', 3)), print(my_str.find('t', 12)), print(my_str.find('t', 15))
print(my_str.find('t', 27)), print(my_str.find('t', 41)), print(my_str.find('t', 47)), print(my_str.find('t', 65))
#total count : 7
print('\n', my_str.index('t')),print(my_str.index('t', 3)),print(my_str.index('t', 12)), print(my_str.index('t', 15))
print(my_str.index('t', 27)), print(my_str.index('t', 41)), print(my_str.index('t', 47)), print(my_str.index('t', 64))
#total count : 7

print('\n')

#Write the code to get the index of '8' in my_str. Use find() and index() method.
print(my_str.find('8'))
print(my_str.index('8'))

#What will be the output of below code?
# print(my_str.find('the'))
# output : -1


# print(my_str.index('the'))
# output :
# ---------------------------------------------------------------------------
# ValueError                                Traceback (most recent call last)
# <ipython-input-49-446a384f6fcc> in <module>
#      20 
#      21 
# ---> 22 print(my_str.index('the'))
#      23 
#      24 

# ValueError: substring not found


# print(my_str.find('t', 9, 15))
# output: 11


# print(my_str.rfind('u'))
# output: 63


# print(my_str.rindex('u'))
# output: 63


# In[61]:


#W A P which applies strip() method if any string, which will be taken from user, starts and ends with space, or applies 
#rrstrip() method if that string only ends with space or applies lstrip() method if that string only starts with a space.

#For example:-
#input:- '    Python   '
a = '    Python   '
print(a.strip())
#output:- 'Python'

#input:- '    Python'
b='    Python'
print(b.lstrip())
#output:- 'Python'

#input:- 'Python   '
c='Python   '
print(c.rstrip())
#output:- 'Python'


# In[64]:


my_str = "Although 8 that way may not be obvious at first unless you're Dutch"

#Write the code to convert all alphabets in my_str into upper case.
print(my_str.upper())

#Write the code to convert all alphabets in my_str into lower case.
print(my_str.lower())

#Write the code to swap the cases of all alphabets in my_str.(lower to upper and upper to lower)
print(my_str.swapcase())


# In[66]:


#Write the code which takes one string from user and if it starts with small case letter then convert it to corresponding 
#capital letter otherwise if starts with capital letters then convert first character of every word in that string into capital.
my_str = 'peter Piper picked a peck of pickled peppers'
print(my_str.capitalize())
my_str1 = 'Peter Piper picked a peck of pickled peppers'
print(my_str.title())


# In[80]:


#Take a string from user and check if it is:-
name_str = "jasmeet123"
#     1. alphanumeric
print(name_str.isalnum())
#     2. alphabets
print(name_str.isalpha())
#     3. digit
print(name_str.isdigit())
#     4. all letters are in lower case
print(name_str.islower())
#     5. all letters are in upper case
print(name_str.isupper())
#     6. in title case
print(name_str.istitle())
#     7. a space character
print(name_str.isspace())
#     8. numeric
print(name_str.isnumeric())
#     9. all number elements in string are decimal
print(name_str.isdecimal())


# In[88]:


#W A P which takes a string as an input and prints True if the string is valid identifier else returns False.
#Sample Input:- 'abc', 'abc1', 'ab1c', '1abc', 'abc$', '_abc', 'if'
print('abc'.isidentifier())
print('abc1'.isidentifier())
print('ab1c'.isidentifier())
print('1abc'.isidentifier())
print('abc$'.isidentifier())
print('__abc'.isidentifier())
print('if'.isidentifier())


# In[93]:


#What will be output of below code?
s = chr(65) + chr(97)
print(s.isprintable())

s = chr(27) + chr(97)
print(s.isprintable())

s = '\n'
print(s.isprintable())

s = ''
print(s.isprintable())


# In[ ]:


#What will be output of below code?
my_string = '  '
print(my_string.isascii())

my_string = 'Studytonight'
print(my_string.isascii())

my_string = 'Study tonight'
print(my_string.isascii())

my_string = 'Studytonight@123'
print(my_string.isascii())

my_string = '°'
print(my_string.isascii())

my_string = 'ö'
print(my_string.isascii())


# In[81]:


#What will be the output of below code?
firstString = "der Fluß"
secondString = "der Fluss"

if firstString.casefold() == secondString.casefold():
    print('The strings are equal.')
else:
    print('The strings are not equal.')


# In[6]:


#Write the code to get below output
p = 'python'
p1 =p.ljust(8, '*')
print (p1)
#O/P 1:- python** (using ljust method)


#Write the code to get below output
p2 =p.rjust(8, '*')
print (p2)
#O/P 1:- **python (using rjust method)


#Write the code to get below output
print(p1.rjust(10, '*'))
#O/P 1:- **python** (using rjust method)


# In[19]:


#Write a Python program to find the length of the my_str:-

#Input:- 'Write a Python program to find the length of the my_str'
my_str = 'Write a Python program to find the length of the my_str'
print(len(my_str))
#Output:- 55


# In[20]:


#Write a Python program to find the total number of times letter 'p' is appeared in the below string:-
    
#Input:- 'peter piper picked a peck of pickled peppers.'
my_str1='peter piper picked a peck of pickled peppers.'
print(my_str1.count('p'))
#Output:- 9


# In[61]:


#Write a Python Program, to print all the indexes of all occurences of letter 'p' appeared in the string:-
#Input:- 'peter piper picked a peck of pickled peppers.'
my_str2='peter piper picked a peck of pickled peppers.'
print(my_str2.find('p')), print(my_str2.find('p', 1)), print(my_str2.find('p', 7)), print(my_str2.find('p', 9)),
print(my_str2.find('p', 13)), print(my_str2.find('p', 22)), print(my_str2.find('p', 30)), print(my_str2.find('p', 38)),
print(my_str2.find('p', 40))
#Output:- 
# 0
# 6
# 8
# 12
# 21
# 29
# 37
# 39
# 40


# In[31]:


#Write a python program to find below output:-

#Input:- 'peter piper picked a peck of pickled peppers.'
my_line = 'peter piper picked a peck of pickled peppers.'
#Output:- ['peter', 'piper', 'picked', 'a', 'peck', 'of', 'pickled', 'peppers.']
print(my_line.split())


# In[57]:


#Write a python program to find below output:-

#Input:- 'peter piper picked a peck of pickled peppers.'
reverse = 'peter piper picked a peck of pickled peppers.'
reverse1 = reverse.split()
reverse1 = reverse1[::-1]
print(reverse1)
print(' '.join(reverse1))
#Output:- 'peppers. pickled of peck a picked piper peter'


# In[44]:


#Write a python program to find below output:-

#Input:- 'peter piper picked a peck of pickled peppers.'
reverse = 'peter piper picked a peck of pickled peppers.'
print(reverse[::-1])
#Output:- '.sreppep delkcip fo kcep a dekcip repip retep'


# In[62]:


#Write a python program to find below output:-

#Input:- 'peter piper picked a peck of pickled peppers.'
reverse = 'peter piper picked a peck of pickled peppers.'
rev = reverse.split()
rev1 = [i[::-1] for i in rev]
# print(rev1)
print(' '.join(rev1))
#Output:- 'retep repip dekcip a kcep fo delkcip .sreppep'


# In[63]:


#Write a python program to find below output:-

#Input:- 'peter piper picked a peck of pickled peppers.'
string = 'peter piper picked a peck of pickled peppers.'
print(string.title())

#Output:- 'Peter Piper Picked A Peck Of Pickled Peppers.'


# In[66]:


#Write a python program to find below output:-

#Input:- 'Peter Piper Picked A Peck Of Pickled Peppers.'
string = 'peter piper picked a peck of pickled peppers.'
print(string.capitalize())
#Output:- 'Peter piper picked a peck of pickled peppers.'


# In[68]:


#Write a python program to implement index method. If sub_str is found in my_str then it will print the index
# of first occurrence of first character of matching string in my_str:-

#Input:- my_str = 'Peter Piper Picked A Peck Of Pickled Peppers.', sub_str = 'Pickl'
my_str = 'Peter Piper Picked A Peck Of Pickled Peppers.'
sub_str = 'Pickl'
print(my_str.index(sub_str))
#Output:- 29


# In[69]:


#Write a python program to implement replace method. If sub_str is found in my_str then it will replace the first 
#occurrence of sub_str with new_str else it will will print sub_str not found:-

#Input:- my_str = 'Peter Piper Picked A Peck Of Pickled Peppers.', sub_str = 'Peck', new_str = 'Pack'
my_str = 'Peter Piper Picked A Peck Of Pickled Peppers.'
print(my_str.replace('Peck', 'Pack'))
#Output:- 'Peter Piper Picked A Pack Of Pickled Peppers.'


# In[5]:


#Write a python program to find below output (implements rjust and ljust):-

#Input:- 'Peter Piper Picked A Peck Of Pickled Peppers.', sub_str = 'Peck', 
a = 'Peter Piper Picked A Peck Of Pickled Peppers.'
print(a.find('Peck'))
print(len(a))
a1 = a[21:25].rjust(25, '*')
print(a1)
#Output:- '*********************Peck********************'
a2 = a1.ljust(45, '*')
print(a2)


# In[ ]:





# In[ ]:




