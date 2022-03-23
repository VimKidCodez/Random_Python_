


# Import random moudule
import random

# this code beloew will genereate random numbers from a range of number from 0 to the predecessor of the number
a = random.randrange(5)
print(a)
#--------------------

# This code will genertae random numbers from a range of numbers from a given number
c = random.randrange(78,87)
print(c)
#---------------------------

# This code genrate float valus from 0 to 1
b = random.random()
print (b)
#--------------------------------------

# This code genetrae random numbers from the first number given to the last number given for only on time
d = random.randint(2,6)
print (d)
#----------------------------------------------------

# This code generate random float numbers fom the first given number to the last 
e = random.uniform(31,32)
print(e)
#------------------------------------------------------------

# This code will generate random str from the given str in a tuple,string or a list
srtring9 = ['Chicken Briyani' , 'frouit salad','idily']
k = random.choice(srtring9)
print(k)
#----------------------------------------------------------------------

# This code will shufle str ina list , touble or string
srtring10 = ['Chicken Briyani' , 'frouit salad','idily']
f = random.shuffle(srtring10)
print (f)
#-------------------------------------------------------------------------------

