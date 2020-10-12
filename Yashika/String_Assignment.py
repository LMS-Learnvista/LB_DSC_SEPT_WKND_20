#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Declare a string and store it in a variable. 

my_str = 'Yashika'


#Check the type and print the id of the same.

print('Type:',type(my_str),'Id:',id(my_str))


# In[ ]:


#Which are valid/invalid strings
1. 'This is Python class'
valid/invalid

Ans: valid string

2. "This is Python class"
valid/invalid

Ans: valid string

3. '''This is Python class'''
valid/invalid

Ans: valid string

4. """This is Python class"""
valid/invalid

Ans: valid string

5. 'This is Python's class'
valid/invalid

Ans: invalid string

6. "Learnbay provides "Java", "Python" classes"
valid/invalid

Ans: invalid string

7. "Learnbay provides 'Java', 'Python' classes"
valid/invalid

Ans: valid string

8. "This is Python's class"
valid/invalid

Ans: valid string

9. """Learnbay provides "Java", "Python" classes"""
valid/invalid

Ans: valid string

10. '''Learnbay provides "Java", "Python" classes'''
valid/invalid

Ans: valid string

11. '''Learnbay provides
"Java", "Python" 
classes'''
valid/invalid

Ans: valid string

12. 'This is
Python 
class'
valid/invalid

Ans: invalid string


# In[ ]:


#Write the code to get the output mentioned below print statement
my_str = "Although that way may not be obvious at first unless you're Dutch."
my_str1 = "Although that way may not be obvious at first unless you're Dutch."

print('The Length of the my_str is',len(my_str))
#output:- The length of my_str is 66

print('id of my_str and my_str1 is same? -',(my_str == my_str1))
#output:- id of my_str and my_str1 is same? - True

print('Type of my_str:',type(my_str))
#output:- Type of my_str is: str


# In[ ]:


#Indexing
my_str = "Although 8 that way may not be obvious at first unless you're Dutch"
#Write the code to get the output,instructions are mentioned below print statement. use indexing

print('The first character in my_str is:',my_str[0])
#output:- The first character in my_str is: A
#Note:- Use positive indexing

print('The first character in my_str is:',my_str[-len(my_str)+3])
#output:- The first character in my_str is: h
#Note:- Use len() function.

print('The character at index 10 in my_str is:',my_str[10])
#output:- The character at index 10 in my_str is: ' '
#Note:- Use positive indexing

print('The last character in my_str is:',my_str[-1])
#output:- The last character in my_str is: h
#Note:- Use negative indexing.

print('The last character in my_str is:',my_str[len(my_str)-1])
#output:- The last character in my_str is: h
#Note:- Use len() function.

print('The character in my_str is:',my_str[9])
#output:- The character in my_str is: 8
#Note:- Use positive index


# In[ ]:



#Slicing
my_str = "Although that way may not be obvious at first unless you're Dutch."
#Write the code to get the output,instructions are mentioned below print statement. use slicing
print(my_str[::])
#output:- You have sliced: Although that way may not be obvious at first unless you're Dutch.Without begin, end and step


print(my_str[0:len(my_str)])
#output:- You have sliced: Although that way may not be obvious at first unless you're Dutch.with begin as 0 end using len and without step


print(my_str[::1])
#output:- You have sliced: Although that way may not be obvious at first unless you're Dutch.without begin and end but using step


print(my_str[0:len(my_str):1])
#output:- You have sliced: Although that way may not be obvious at first unless you're Dutch.With begin, end and step


print(my_str[:66:-1])
#output:- You have sliced:   .with using begin and end using postive values and step as negative values.
#Slicing command should print empty string.


print(my_str[::2])
#output:- You have sliced: Atog htwymyntb biu tfrtuls o'eDth


print(my_str[::3])
#output:- You have sliced: Ahgttam tebo  r lsorDc


print(my_str[::-1])
#output:- You have sliced: .hctuD er'uoy sselnu tsrif ta suoivbo eb ton yam yaw taht hguohtlA. Use only step


print(my_str[len(my_str):-67:-1])
#output:- You have sliced: .hctuD er'uoy sselnu tsrif ta suoivbo eb ton yam yaw taht hguohtlA. Use begin end and step.


print(my_str[::-2])
#output:- You have sliced: .cu ruysen si asovoe o a a athuhl. use only step


print(my_str[len(my_str):-67:-2])
#output:- You have sliced: .cu ruysen si asovoe o a a athuhl. use begin, end and step.


print(my_str[10:17:-1])
#What will be the output?
output:prints empty string


print(my_str[-49:-56:-1])
#output:- You have sliced: yaw ta, Using begin, end and step.

print(my_str[49:56:1])
#output:- You have sliced: ess you. Using begin, end and step.


# In[ ]:


#Basic operation on string
str1 = 'Learnbay'
str2 = 'Python'

#Write the code to get the output,instructions are mentioned below.
#Output is: Learnbay Python
print('Output is:',str1+' '+str2)


#Error: TypeError: can only concatenate str (not "int") to str
num = 9 
print(str1+ num)


#Error: TypeError: can only concatenate str (not "float") to str
num1 = 1.2
print(str1+num1)



#Find below Output
#Output is: LearnbayLearnbayLearnbay
print('Output is:',str1*3)

#Error: TypeError: can't multiply sequence by non-int of type 'float'
print(str1*2.0)

#Error: TypeError: can't multiply sequence by non-int of type 'str'
print(str1*str1)


# In[ ]:


#Find below Output
str1 = 'Python'
str2 = 'Python'
str3 = 'Python$'
str4 = 'Python$'

#print True by using identity operator between str1 and str2
print(str1 is str2)

#print False by using identity operator between str1 and str3
print(str1 is str3)

#print False by using identity operator between str4 and str3
print(str3 is str4)

#Check if P is available in str1 and print True by using membership operator
print('P' in str1)

#Check if $ is available in str3 and print True by using membership operator
print('$' in str3)

#Check if N is available in str3 and print False by using membership operator
print('N' in str3)


# In[ ]:


#Complete the below code
str1 = 'This is Python class'
#write the code to replace 'Python' with 'Java' and you should get below error.
str1[8:14] = 'Java'
print(str1)
#TypeError: 'str' object does not support item assignment.



# In[ ]:


str1 = 'A'
str2 = 'A'
#Compare str1 and str2 and print True using comparison operator
print(str1 <= str2)

#Compare str1 and str2 and print True using equality operator
print(str1 == str2)

#Compare str1 and str2 and print False using equality operator
print(str1 != str2)

#Compare str1 and str2 and print False using comparison operator
print(str1 > str2)


# In[ ]:


str1 = 'A'
str2 = 'a'
#Compare str1 and str2 and print True using comparison operator
print(str1 < str2)

#Compare str1 and str2 and print True using equality operator
print(str1 != str2)

#Compare str1 and str2 and print False using equality operator
print(str1 == str2)

#Compare str1 and str2 and print False using comparison operator
print(str1 > str2)


# In[ ]:


str1 = 'A'
str2 = '65'
#Compare str1 and str2 using comparison operator and it should give below error.
#Error: TypeError: '>=' not supported between instances of 'str' and 'int'
str1 = 'A'
str2 = 65
print(str1 >= str2)

#Compare str1 and str2 and print True using equality operator
print(str1 != str2)

#Compare str1 and str2 and print False using equality operator
print(str1 == str2)


# In[ ]:


str1 = 'Python'
str2 = 'Python'
#Compare str1 and str2 and print True using comparison operator
print(str1 <= str2)

#Compare str1 and str2 and print True using equality operator
print(str1 == str2)

#Compare str1 and str2 and print False using equality operator
print(str1 != str2)

#Compare str1 and str2 and print False using comparison operator
print(str1 < str2)


# In[ ]:


str1 = 'Python'
str2 = 'python'
#Compare str1 and str2 and print True using comparison operator
print(str1 < str2)

#Compare str1 and str2 and print True using equality operator
print(str1 != str2)

#Compare str1 and str2 and print False using equality operator
print(str1 == str2)

#Compare str1 and str2 and print False using comparison operator
print(str1 > str2)


# In[ ]:


a = 'Python'
b = ''

#Apply logical opereators (and, or & not) on above string values and observe the output.

print(a and b) - prints empty string
print(b and a) - prints empty string
print(a or b) - prints Python
print(b or a) - prints Python
print(not a,not b)- prints False,True


# In[ ]:


a = ''
b = ''

#Apply logical opereators (and, or & not) on above string values and observe the output.
print(a and b)- prints empty string
print(a or b) - prints empty string
print(not a,not b) - prints True,True


# In[ ]:


a = 'Python'
b = 'learnbay'

#Apply logical opereators (and, or & not) on above string values and observe the output.
print(a and b) - prints Learnbay
print(a or b) - prints Python
print(not a,not b) - prints False,False


# In[ ]:


my_str = "Although 8 that way may not be obvious at first unless you're Dutch"

#Write the code to get the total count of 't' in above string. Use find() and index() method.
ind = -1
ind2 = -1
count = 0
while True: 
     ind2 = my_str.find('t', ind+1)
     if ind2 == -1:
         break
     else:
         ind = my_str.index('t', ind+1)
         count +=1
         print(ind)
print('Total count of p is ', count)

#Write the code to get the index of '8' in my_str. Use find() and index() method.
print(my_str.find('8'))
print(my_str.index('8'))

#What will be the output of below code?
print(my_str.find('the'))
output = -1

print(my_str.index('the'))
ValueError: substring not found

print(my_str.find('t', 9, 15))
output = 11

print(my_str.rfind('u'))
output = 63

print(my_str.rindex('u'))
output = 63


# In[ ]:


#W A P which applies strip() method if any string, which will be taken from user, starts and ends with space, or applies 
#rrstrip() method if that string only ends with space or applies lstrip() method if that string only starts with a space.

#For example:-
#input:- '    Python   '
#output:- 'Python'
str1 = input('input:')
print(str1.strip())
#input:- '    Python'
#output:- 'Python'
print(my_str1.lstrip())
#input:- 'Python   '
#output:- 'Python'
print(my_str1.rstrip())


# In[ ]:


my_str = "Although 8 that way may not be obvious at first unless you're Dutch"

#Write the code to convert all alphabets in my_str into upper case.
print(my_str.upper())

#Write the code to convert all alphabets in my_str into lower case.
print(my_str.lower())

#Write the code to swap the cases of all alphabets in my_str.(lower to upper and upper to lower)
print(my_str.swapcase())


# In[ ]:


#Write the code which takes one string from user and if it starts with small case letter then convert it to corresponding 
#capital letter otherwise if starts with capital letters then convert first character of every word in that string into capital.

str1 = input('Enter a string:')
print(str1.capitalize())
print(str1.title())



# In[ ]:


#Take a string from user and check if it is:-
#     1. alphanumeric
#     2. alphabets
#     3. digit
#     4. all letters are in lower case
#     5. all letters are in upper case
#     6. in title case
#     7. a space character
#     8. numeric
#     9. all number elements in string are decimal

str1 = input('Enter a string:')
print(str1.isalnum())  
print(str1.isalpha())
print(str1.isdigit())
print(str1.islower())
print(str1.isupper())
print(str1.title())
print(str1.isspace())
print(str1.isnumeric())
print(str1.isdecimal())



# In[ ]:


#W A P which takes a string as an input and prints True if the string is valid identifier else returns False.
#Sample Input:- 'abc', 'abc1', 'ab1c', '1abc', 'abc$', '_abc', 'if'
str1 = input('Enter a string:')
print(str1.isidentifier())

Enter a string:abc
True


Enter a string:abc1
True


Enter a string:ab1c
True


Enter a string:1abc
False

Enter a string:abc$
False


Enter a string:__abc
True


Enter a string: if
False


# In[ ]:


#What will be output of below code?
s = chr(65) + chr(97)
print(s.isprintable())
True
s = chr(27) + chr(97)
print(s.isprintable())
False
s = '\n'
print(s.isprintable())
False
s = ''
print(s.isprintable())
True


# In[ ]:


#What will be output of below code?
my_string = '  '
print(my_string.isascii())
output : True

my_string = 'Studytonight'
print(my_string.isascii())
output :True

my_string = 'Study tonight'
print(my_string.isascii())
output :True
    
my_string = 'Studytonight@123'
print(my_string.isascii())
output :True

my_string = '°'
print(my_string.isascii())
output :False

my_string = 'ö'
print(my_string.isascii())
output :False


# In[ ]:


#What will be the output of below code?
firstString = "der Fluß"
secondString = "der Fluss"

if firstString.casefold() == secondString.casefold():
    print('The strings are equal.')
else:
    print('The strings are not equal.')
    
output: The strings are equal.


# In[ ]:


#Write the code to get below output
#O/P 1:- python** (using ljust method)
   
str1 = 'python'
print(str1.ljust(8,'*'))

#Write the code to get below output
#O/P 1:- **python (using rjust method)
str1 = 'python'
print(str1.rjust(8,'*'))

#Write the code to get below output
#O/P 1:- **python** (using rjust method)

str1 = 'python'
print(str1.rjust(8,'*') + '**')


# In[ ]:


#Write a Python program to find the length of the my_str:-

#Input:- 'Write a Python program to find the length of the my_str'
#Output:- 55

str1 = 'Write a Python program to find the length of the my_str'
print(len(str1))


# In[ ]:


#Write a Python program to find the total number of times letter 'p' is appeared in the below string:-
    
#Input:- 'peter piper picked a peck of pickled peppers.'
#Output:- 9
my_str = 'peter piper picked a peck of pickled peppers.'
print(my_str.count('p'))


# In[ ]:


#Write a Python Program, to print all the indexes of all occurences of letter 'p' appeared in the string:-
my_str = 'peter piper picked a peck of pickled peppers.'
ind = -1
count = 0
while True:
     ind = my_str.find('p', ind+1)
     if ind == -1:
         break
     else:
         count +=1
         print(ind)    
#Input:- 'peter piper picked a peck of pickled peppers.'
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


# In[ ]:


#Write a python program to find below output:-

#Input:- 'peter piper picked a peck of pickled peppers.'
#Output:- ['peter', 'piper', 'picked', 'a', 'peck', 'of', 'pickled', 'peppers.']

str1 = 'peter piper picked a peck of pickled peppers.'
print(str1.split())


# In[ ]:


#Write a python program to find below output:-

#Input:- 'peter piper picked a peck of pickled peppers.'
#Output:- 'peppers. pickled of peck a picked piper peter'
str1 = 'peter piper picked a peck of pickled peppers.'
st = str1.split()
t = st[::-1]
print(' '.join(t))


# In[ ]:


#Write a python program to find below output:-

#Input:- 'peter piper picked a peck of pickled peppers.'
#Output:- '.sreppep delkcip fo kcep a dekcip repip retep'
str1 = 'peter piper picked a peck of pickled peppers.'
print(str1[::-1])


# In[ ]:


#Write a python program to find below output:-

#Input:- 'peter piper picked a peck of pickled peppers.'
#Output:- 'retep repip dekcip a kcep fo delkcip .sreppep'

str1 = 'peter piper picked a peck of pickled peppers.'
print(' '.join(i[::-1] for i in str1.split()))


# In[ ]:


#Write a python program to find below output:-

#Input:- 'peter piper picked a peck of pickled peppers.'
#Output:- 'Peter Piper Picked A Peck Of Pickled Peppers.'

str1 = 'peter piper picked a peck of pickled peppers.'
print(str1.title())


# In[ ]:


#Write a python program to find below output:-

#Input:- 'Peter Piper Picked A Peck Of Pickled Peppers.'
#Output:- 'Peter piper picked a peck of pickled peppers.'

str1 = 'Peter Piper Picked A Peck Of Pickled Peppers.'
print(str1.capitalize())


# In[ ]:


#Write a python program to implement index method. If sub_str is found in my_str then it will print the index
# of first occurrence of first character of matching string in my_str:-

#Input:- my_str = 'Peter Piper Picked A Peck Of Pickled Peppers.', sub_str = 'Pickl'
#Output:- 29

my_str = 'Peter Piper Picked A Peck Of Pickled Peppers.'
sub_str =  'Pickl'
print(my_str.index(sub_str))


# In[ ]:


#Write a python program to implement replace method. If sub_str is found in my_str then it will replace the first 
#occurrence of sub_str with new_str else it will will print sub_str not found:-

#Input:- my_str = 'Peter Piper Picked A Peck Of Pickled Peppers.', sub_str = 'Peck', new_str = 'Pack'
#Output:- 'Peter Piper Picked A Pack Of Pickled Peppers.'


my_str = 'Peter Piper Picked A Peck Of Pickled Peppers.'
sub_str = 'Peck'
new_str = 'Pack'

print(my_str.replace(sub_str,new_str)) if sub_str in my_str else print('substring not found')


# In[7]:


#Write a python program to find below output (implements rjust and ljust):-

#Input:- 'Peter Piper Picked A Peck Of Pickled Peppers.', sub_str = 'Peck', 
#Output:- '*********************Peck********************'

my_str = 'Peter Piper Picked A Peck Of Pickled Peppers.'
sub_str = 'Peck'

print(sub_str.rjust(my_str.index(sub_str), '*').ljust(len(my_str), '*'))


# In[ ]:





# In[ ]:




