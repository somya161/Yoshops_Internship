#!/usr/bin/env python
# coding: utf-8

# ### 1. Write a python program for merge two excel file data to one file

# In[1]:


import pandas as pd


# In[2]:


#loading datasets
df_1 = pd.read_excel("Kalyani_Balance_Sheet_November_2022.xlsx")
df_2 = pd.read_excel("Kalyani_Balance_Sheet_December_2022.xlsx")

#merge datasets
df_combine = pd.concat([df_1, df_2])


# In[3]:


#df_1
#df_2
df_combine


# In[4]:


df_combine = df_combine.iloc[:, 0:6]
df_combine


# In[5]:


df_combine.to_excel('YoshopsBalanceSheet_NovDec_2022.xlsx', index = False)


# In[6]:


new_df = pd.read_excel('YoshopsBalanceSheet_NovDec_2022.xlsx')
new_df


# In[7]:


#import os
#import shutil


# ### 2. Write a python program to shorting file in different folder means main folder containing 40 word file. Now after shorting create 4 child folder and store 10 file each folder.

# In[8]:


import os
import shutil

target_folder = r'/Users/tech/Desktop/Somya/Yo_Shops_Internship/Tasks/Tasks/Task 5'+'\\'
source_folder = r'/Users/tech/Desktop/Somya/Yo_Shops_Internship/Tasks/Tasks'+'\\'

for path,dir,files in os.walk(source_folder):
    print(path)
    print(files)


# In[9]:


for path,dir,files in os.walk(source_folder):
    if files:
        for file in files:
            if not os.path.isfile(target_folder + file):
                os.rename(path + '\\' + file, target_folder + file)


# In[10]:


for path,dir,files in os.walk(target_folder):
    print(path)
    print(files)


# In[11]:


import os
dir_name = '/Users/tech/Desktop/Somya/Yo_Shops_Internship/Tasks/Tasks/Task 5'
# Get list of all files in a given directory sorted by name
list_of_files = sorted( filter( lambda x: os.path.isfile(os.path.join(dir_name, x)),
                        os.listdir(dir_name) ) )
for file_name in list_of_files:
    print(file_name)


# In[13]:


import os
path = '/Users/tech/Desktop/Somya/Yo_Shops_Internship/Tasks/Tasks/Task 5'
for i in range(0,4):
    os.chdir(path)
    Newfolders = 'SubFolder'+str(i)
    os.makedirs(Newfolders)


# In[14]:


i=0
j=0
k=0
for i in range(0,4):
    for j in range(0,10):
        src = '/Users/tech/Desktop/Somya/Yo_Shops_Internship/Tasks/Tasks/Task 5/'+list_of_files[k]
        dst = '/Users/tech/Desktop/Somya/Yo_Shops_Internship/Tasks/Tasks'+str(i)
        shutil.copy2(src,dst)
        k=k+1


# ## 3. Write a python programm separate duplicate file

# In[15]:


# Importing Libraries
import os
from pathlib import Path
from filecmp import cmp
  
  
# list of all documents
DATA_DIR = Path('/Users/tech/Desktop/Somya/Yo_Shops_Internship/Tasks/Tasks/Task 5/')
files = sorted(os.listdir(DATA_DIR))
  
# List having the classes of documents
# with the same content
duplicateFiles = []
  
# comparison of the documents
for file_x in files:
  
    if_dupl = False
  
    for class_ in duplicateFiles:
        # Comparing files having same content using cmp()
        # class_[0] represents a class having same content
        if_dupl = cmp(
            DATA_DIR / file_x,
            DATA_DIR / class_[0],
            shallow=False
        )
        if if_dupl:
            class_.append(file_x)
            break
  
    if not if_dupl:
        duplicateFiles.append([file_x])
  
# Print results
print(duplicateFiles)


# #### Check excel file and create sperate file and store duplicate data

# In[16]:


import pandas as pd
df_master = pd.read_excel('/Users/tech/Desktop/Somya/Yo_Shops_Internship/Tasks/Tasks/Task 5/Kalyani_Balance_Sheet_December_2022.xlsx')
print(df_master)


# In[17]:


# Selecting duplicate rows except first
# occurrence based on all columns
duplicate = df_master[df_master.duplicated()]
 
print("Duplicate Rows :")
 
# Print the resultant Dataframe
duplicate


# #### Sort files in a folder based on their size

# In[18]:


import os
import shutil
# The folder containing files.
directory = '/Users/tech/Desktop/Somya/Yo_Shops_Internship/Tasks/Tasks'

# Get all files.
list = os.listdir(directory)

# Loop and add files to list.
pairs = []
for file in list:

    # Use join to get full file path.
    location = os.path.join(directory, file)

    # Get size and add to list of tuples.
    size = os.path.getsize(location)
    pairs.append((size,file))

# Sort list of tuples by the first element, size.
pairs.sort(key=lambda s: s[0])

i=0
# Display pairs.
for pair in pairs:
    #src = 'F:/Yoshops/task_5/task_5/source/'+pair[1]
    #dst = 'F:/Yoshops/task_5/task_5/destination/size'+str(i)
    #shutil.copy2(src,dst)
    
    print(pair)
    i=i+1

path = r'/Users/tech/Desktop/Somya/Yo_Shops_Internship/Tasks/Tasks/Task 5'
for j in range(0,i):
    os.chdir(path)
    Newfolders = 'size'+str(j)
    os.makedirs(Newfolders)


# In[19]:


i=0
# Display pairs.
for pair in pairs:
    src = r'/Users/tech/Desktop/Somya/Yo_Shops_Internship/Tasks/Tasks'+pair[1]
    dst = r'/Users/tech/Desktop/Somya/Yo_Shops_Internship/Tasks/Tasks/Task 5'+str(i)
    shutil.copy2(src,dst)
    i=i+1


# In[ ]:




