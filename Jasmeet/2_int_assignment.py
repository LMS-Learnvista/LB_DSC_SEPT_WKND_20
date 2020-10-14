#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Declare an int value and store it in a variable. 
my_int = 5

#Check the type and print the id of the same.
print(type(my_int), id(my_int))

# output - 
# <class 'int'> 140723976746912


# In[4]:


#Take one int value between 0 - 256.
#Assign it to two different variables.
#Check the id of both the variables. It should come same. Check why?
a = 15
b = 15
print(id(a), id(b))

#Take one int value either less than -5 or greater than 256.
#Assign it to two different variables.
#Check the id of both the variables. It should come different.Check why?
c = 257
d = 257
print(id(c), id(d))


# output - 
140723976747232 140723976747232
2200695760144 2200695760208


# In[14]:


#Arithmatic Operations on integers
#Take two different intger values.
#Store them in two different variables.
x = 39
y = 20
#Do below operations on them:-
    #Find sum of both numbers
print(x + y)
    #Find differce between them
print(x-y)
    #Find the product of both numbers.
print(x*y)
    #Find value after dividing first num with second number
print(x/y)
    #Find the remainder after dividing first number with second number
print(x%y)
    #Find the quotient after dividing first number with second number
print(x//y)
    #Find the result of first num to the power of second number.
print(x**y)



# output - 
59
19
780
1.95
19
1
66266211231824447117620880943201


# In[18]:


#Comparison Operators on integers
#Take two different intger values.
#Store them in two different variables.
a = 20
b = 10
#Do below operations on them:-
    #Compare se two numbers with below operator:-
        #Greater than, '>'
print(a>b)
        #Smaller than, '<'
print(a<b)
        #Greater than or equal to, '>='
print(a>=b)
        #Less than or equal to, '<='
print(a<=b)
#Observe their output(return type should be boolean)

# output - 
True
False
True
False


# In[21]:


#Equality Operator
#Take two different intger values.
#Store them in two different variables.
x = 20
y=15
#Equuate them using equality operator (==, !=)
print(x==y)
print(x!=y)
#Observe the output(return type should be boolean)


# output - 
False
True


# In[22]:


#Logical operators
#Observe the output of below code
#Cross check the output manually

print(10 and 20)       #----------------------------------------->Output is 20
print(0 and 20)        #----------------------------------------->Output is 0
print(20 and 0)        #----------------------------------------->Output is 0
print(0 and 0)         #----------------------------------------->Output is 0

print(10 or 20)        #----------------------------------------->Output is 10
print(0 or 20)         #----------------------------------------->Output is 20
print(20 or 0)         #----------------------------------------->Output is 20
print(0 or 0)          #----------------------------------------->Output is 0

print(not 10)          #----------------------------------------->Output is False
print(not 0)           #----------------------------------------->Output is True


# In[32]:


#Bitwise Operators 
#Do below operations on the values provided below:-
    #Bitwise and(&) -----------------------------------------> 10, 20   -------> Output is 0
print(10 & 20)
    #Bitwise or(|)  -----------------------------------------> 10, 20   -------> Output is 30
print(10 | 20)
    #Bitwise(^)     -----------------------------------------> 10, 20   -------> Output is 30
print(10 ^ 20)
    #Bitwise negation(~) ------------------------------------> 10       -------> Output is -11
print(~10)
    #Bitwise left shift  ------------------------------------> 10,2     -------> Output is 40
print(10<<2)
    #Bitwise right shift ------------------------------------> 10,2     -------> Output is 2
print(10>>2)
#Cross check the output manually


# In[23]:


#What is the output of expression inside print statement. Cross check before running the program.
a = 10 
b = 10
print(a is b)          #True or False? - True
print(a is not b)      #True or False? - False

a = 1000
b = 1000
print(a is b)          #True or False? - False
print(a is not b)      #True or False? - True


# In[53]:


#What is the output of expression inside print statement. Cross check before running the program.
print(10+(10*32)//2**5&20+(~(-10))<<2)

# Output
20


# In[63]:


#Membership operation
#in, not in are two membership operators and it returns boolean value

print('2' in 'Python2.7.8')
print(10 in [10,10.20,10+20j,'Python'])
print(10 in (10,10.20,10+20j,'Python'))
print(2 in {1,2,3})
print(3 in {1:100, 2:200, 3:300})
print(10 in range(20))

# Output-
True
True
True
True
True
True


# In[67]:


#An integer can be represented in binary, octal or hexadecimal form.
#Declare one binary, one octal and one hexadecimal value and store them in three different variables.
binary = 0b10110
octal = 0o2523
hexadecimal = 0x123fa
print(binary), print(octal), print(hexadecimal)
#Convert 9876 to its binary, octal and hexadecimal equivalent and print their corresponding value.
print(bin(9876))
print(oct(9876))
print(hex(9876))


# In[64]:


#What will be the outut of following:-
a = 0b1010000
print(a)

b = 0o7436
print(b)

c = 0xfade
print(c)

print(bin(80))

print(oct(3870))

print(hex(64222))

print(bin(0b1010000))

print(bin(0xfade))

print(oct(0xfade))

print(oct(0o7436))

print(hex(0b1010000))

print(hex(0xfade))


# Output-
80
3870
64222
0b1010000
0o7436
0xfade
0b1010000
0b1111101011011110
0o175336
0o7436
0x50
0xfade

