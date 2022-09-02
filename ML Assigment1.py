#!/usr/bin/env python
# coding: utf-8

# In[1]:


ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# sorted() is an inbuilt method used to arrange the data in an order
print(sorted(ages))
print("Max= ", max(ages))
print("Min= ", min(ages))
# max() and min() are the two methods that gives us highest and lowest value in the given data
ages.append(19)
ages.append(26)
# append() method adds the data to the end of the list.
print(ages)


# In[17]:


import statistics
statistics.median(ages)


# In[18]:


statistics.mean(ages)


# In[20]:


range= max(ages)- min(ages)
print("Range:", range)
# mean(), median() and mode() are the inbuilt methods that gives the respective values directly without arithmetic calculations.


# -------------------------------------
# 

# In[22]:


dog = {}
# A dictionary named dog is created.
dog = {'name': 'Tommy', 'colour': 'brown', 'breed':'Golden', 'legs': '4', 'age':'2'}
print(dog)


# In[35]:


stu_dict = {}
stu_dict = { 'first_name', 'last_name', 'gender', 'age', 'marital status', 'Skills', 'Country', 'City', 'Address'}
print(stu_dict)
print(len(stu_dict))
# len() method returns the length of the given data.


# In[40]:


stu_dict = { 'first_name':'Mercy', 'last_name': 'Cooper', 'gender':'F', 'age':'22','marital status':'Single', 'Skills':["C","C++","Python"],'Country':'United States', 'City':'Overland Park','Address':'Hardy Street'}
print(stu_dict)

print(stu_dict.get('Skills'))
# .get() method returns the value of the specified key.

print(type(stu_dict.get('Skills')))

stu_dict['Skills'].append('Java')
print(stu_dict.get('Skills'))


# In[41]:


k= stu_dict.keys()
# keys() method returns all the keys in the dictionary.
print(keys)


# In[43]:


v = stu_dict.values()
# values() methods returns all the values in the dictionary.
print(v)


# ---------------------------------------------

# In[70]:


sisters = (" Sara", "Meera", "Roja", "Mehreen")
brothers = ("Ajay", "Khaleel", "Vijay", "Basheer")
siblings= sisters + brothers
# '+' concatinates both the tuples.
print(siblings)


# In[73]:


print(len(siblings))

family_members = list(siblings)
# list() method converts the tuple datatype ito list
# in the above step the list is assigned to family_members
family_members.append("Jayanth Kumar")
family_members.append("Nameera")
print(family_members)


# -------------------------------

# In[2]:


it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
      
print(len(it_companies))


# In[3]:


it_companies.add('Twitter')  
# add() method is used to add data to the set.
print(it_companies)


# In[7]:


mul_it_companies = {'Cognizant', 'Accenture', 'Capgemini'}    
it_companies.update(mul_it_companies)     
# update() method is used to add data to a set from another set
print(it_companies)


# In[8]:


it_companies.remove('Oracle')
# remove() method is used to remove a dataitem from the set.
print(it_companies)


# In[9]:


A = {19,22,24,20,25,26}
      
B= {19,22,20,25,26,24,28,27}  

C = A.union(B)
# union() method returns the combined set of both the sets removing repetiting elements.
      
print(C)


# In[10]:


D = A. intersection(B)
# intersection() method returns the set of elements that are common in both the sets.
      
print(D)


# In[11]:


E = A. issubset(B)
# issubset() method returns whether A is a subset of B
print(E)


# In[12]:


F = A.isdisjoint(B)  
# isdisjoint() method returns true if there is no intersection in the data and viceversa.
print(F)


# In[48]:


A = {19,22,24,20,25,26}      
B= {19,22,20,25,26,24,28,27} 
G= A.union(B)      
H= B.union(A)
      
print(G)
print(H)


# In[49]:


I = A.symmetric_difference(B)     
# symmetric_difference() method returns a set with the symmetric difference of both the sets.
print(I)
A.clear()
B.clear()
# clear() method clears all the data from the set and makes it empty.
      
print(A, B)


# In[16]:


age = [22,19,24,25,26,24,25,24]
print(len(age))


# In[17]:


age_set = set(age)     
print(age_set)

print(len(age_set))


# --------------------------

# In[18]:


r =  30      
_area_of_circle_ = 3.14*30*30
      
print(_area_of_circle_)


# In[19]:


r=30      
_circum_of_circle_ = 2*3.14*30
      
print(_circum_of_circle_)


# In[20]:


r = int(input("Enter the radius of the circle: "))
# takes the value from user
area = 3.14*r*r
      
print("Area of the circle is: ", area)


# -----------------------------------

# In[21]:


sen = "I am a teacher and I love to inspire and teach people"

x =(sen.split())
# split() method divides the words individually in the sentence.
y=set(x)
# x's datatype is converted in to set and it's valye is assigned to y.
print(y)
print(len(y))


# -------------------------------

# In[26]:


print("Name\t\tAge\tCountry\t City")
# \t in python is used for a tab space.

print("Asabeneh\t250\tFinland\t Helsinki")  


# -------------------------------------

# In[27]:


radius = 10
area = 3.14 * radius ** 2
inp = "The area of a circle with radius {} is {} meters square."
print(inp.format(radius,area))
# The format() method inserts the user specified value into the string's placeholder.
      


# ------------------------------

# In[45]:


N = int(input("Enter the number of students: "))

weights_lbs = []
print("Enter the weights of {} students".format(N))

for i in range(0, N):
    weight_lb = int(input())
    weights_lbs.append(weight_lb)
print("{} students weights in lbs {}".format(N, weights_lbs))

weights_kgs = [i * 0.453592 for i in weights_lbs]
print(N, "students weights in kgs", weights_kgs)


# In[ ]:




