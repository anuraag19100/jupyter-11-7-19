#!/usr/bin/env python
# coding: utf-8

# ### Standard Libraries
# - File I/O
# - Regular expression
# - Datetime
# - Math(numerical and mathmatical)

#  ### File Handling in Python
#  - File:- Document containing information  resides on the permannent storage
#  - Different types of files-text,doc,pdf,csv and etc..
#  - Input--Keyboard
#  - Output-File
#  ### Modes of the File I/O
#  - 'w' -- This mode is used to file writing
#        -- if the file is not present first it creates the file and write so me data top it
#        --if the file is already present then it will rewrite the previous content

# In[5]:


# Function to create a file and write to the file
def createFile(filename):
    f = open(filename,'w')
    for i in range(10):
        f.write('This is %d Line' %i)
        print('File is created and data has written')
        return
createFile('file1.txt')


# In[6]:


ls


# In[7]:


cat file1.txt


# In[8]:


def createFile(filename):
    f= open(filename,'w')
    f.write('Testing--\n')
    print("File is created and data has written")
    return
createFile('file1.txt')


# In[12]:


def appendData(filename):
    f=open(filename,'a')
    for i in range(10):
        f.write("This is % Line\n" % i)
    print("File Created and Successfully data written")
    return
appendData('file2.txt')


# In[13]:


def appendData(filename):
    f = open(filename,"a")
    f.write("New Line 1\n")
    f.write("New Line 2\n")
    print("File Created and Successfully data written")
    return
appendData('file2.txt')


# In[14]:


def readfiledata(filename):
    f = open(filename,'r')
    if f.mode == 'r':
        x = f.read()
        print(x)
    f.close()
    return
readfiledata('file2.txt')


# In[1]:


# Function to read the file
def fileOperations(filename,mode):
    with open(filename,mode) as f:
        if f.mode =='r' :
            data = f.read()
            print(data)
        elif f.mode == 'a':
            f.write('Data to the file')
            print('The data successfully written')
    f.close()
    return
filename = input('Enter the file name')
mode = input('Enter the mode of the file')
fileOperations(filename,mode)
            


# In[5]:


# Data Analysis
# Word Count Program
def wordCount(filename,word):
    with open(filename,'r') as f:
        if f.mode == 'r':
            x = f.read()
            li = x.split()
    cnt = li.count(word)
    return cnt
filename = input('Enter the file name : ')
word = input('Enter the word : ')
wordCount(filename,word)


# In[1]:


# Character count from the given file
def charCount(filename):
    with open(filename,'r') as f:
        if f.mode == 'r':
            x=f.read()
            li = list(x)
    return len(li)
filename = input('Enter the filename : ')
charCount(filename)


# In[5]:


# Function to the number of lines in the input file
# Input--filename(file2.txt)
# Output--number of lines (12)
def countOflines(filename):
    with open(filename,'r') as f:
        if f.mode == 'r':
            x = f.read()
            li = x.split("\n")
    return len(li)
filename = input('Enter the filename : ')
countOflines(filename)


# In[12]:


# Function to print the upper and lower characters
def caseCount(filename):
    cntUpper = 0
    cntLower = 0
    with open(filename,'r') as f:
        if f.mode == 'r':
            x = f.read()
            li = list(x)
    for i in li:
        if i.isupper():
            cntUpper += 1
        elif i.islower():
            cntLower += 1
    output = 'Upper case = {0} , Lower case = {1}'.format(cntUpper,cntLower)
    return output
filename = input('Enter the filename : ')
caseCount(filename)


# # math,random,os
# - os package it containsthe certain methods which works with OS

# In[13]:


ls


# In[14]:


cd Deskyop/PythonProg/Git


# In[17]:


cd Desktop/ProbsolvingProgramming/Git


# In[18]:


ls


# In[19]:


cd ..


# In[20]:


import os
os.listdir('git/')


# In[21]:


k


# - Older version Python--os.listdir()
# - New version Python--os.scandir() and pathlib.path()

# In[28]:


li = os.scandir('git/')
for i in li:
    print(i)


# In[33]:


from pathlib import Path
li = Path('git/')
for i in li.iterdir():
    print(i.name)


# ### Listing all files in  a Directory

# In[2]:


import os
dirPath = "git/"
for i in os.listdir(dirPath):
    if os.path.isfile


# In[3]:


pwd


# In[4]:


cd Desktop/ProbsolvingProgramming/Git


# ### Listing Subdirectories

# In[7]:


dirPath = 'Git/'
for i in os.listdir(dirPath):
    if os.path.isdir(os.path.join(dirPath,i)):
        print(i)


# In[ ]:


from pathlib import Path


# ### Creating a single Directory

# In[8]:


import os
os.mkdir('SingleDirectory')


# In[9]:


import pathlib
p = pathlib.Path('TestFolder')
p.mkdir()


# In[10]:


ls


# ### Creating Multiple Directories

# In[11]:


import os
os.makedirs('2019/july/11')


# In[12]:


ls


# ### Filename Pattern Matching

# In[13]:


cd ..


# In[13]:


cd ProbsolvingProgramming


# In[24]:


ls


# In[14]:


cd git


# In[18]:


cd ..


# In[19]:


cd Git


# In[25]:


cd ..


# In[26]:


cd ..


# In[30]:


cd ..


# In[35]:


ls


# In[23]:


ls


# In[22]:


import os
dirPath = 'Git/'
for f_name in os.listdir(dirPath):
    if f_name.endswith(' .ipynb'):
        print(f_name)


# ### Deleting Files and Directories

# In[7]:


import os
data_file ='file1.txt'  #Give the path c:\\Users
os.remove(data_file)


# In[10]:


data_dir = 'TestFolder'
os.rmdir(data_dir)


# In[ ]:




