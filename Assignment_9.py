#!/usr/bin/env python
# coding: utf-8

# 1. To what does a relative path refer?
# 
# Ans:
# 
# A location of file or folder in relative to current working directory. It can be best used to refer to websites that are located on the same domain, ideally on certain sections of websites in which the documents never change relationships to each other.

# 2. What does an absolute path start with your operating system?
# 
# Ans:
# 
# Absolute Path is the hierarchical path that locates a file or folder in a file system starting from the root. The absolute path of a file enables the location of the file to be precisely specified, independent of where the user’s current directory is located.

# 3. What do the functions os.getcwd() and os.chdir() do?
# 
# Ans:
# 
# The getcwd () is a built-in Python os module method that returns the current working directory. To get the current working directory using the Python command, use the os.getcwd () function. To change the current working directory in Python, use the os.chdir () method.

# In[1]:


import os

cwd = os.getcwd()

print("Current working directory:", cwd)


# In[2]:


import os

cwd = os.getcwd()
print("Current working directory:", cwd)

os.chdir('../../')
ncwd = os.getcwd()
print("Current working directory:", ncwd)


# 

# 4. What are the . and .. folders?
# 
# Ans:
# 
# ' . ' represents the current directory, it is a way to reference files and directories using a relative path.
# 
# ' .. ' it is represent the parent directory.

# 5. In C:\bacon\eggs\spam.txt, which part is the dir name, and which part is the base name?
# 
# Ans:
# 
# dir name is "C:\bacon\eggs" and base name is "spam.txt".

# 6. What are the three “mode” arguments that can be passed to the open() function?
# 
# Ans:
# 
# Read mode: open ('test.txt', 'r'), Write mode: open ('test.txt', 'w'), Append mode: open ('test.txt', 'a').

# 7. What happens if an existing file is opened in write mode?
# 
# Ans:
# 
# If the existing file opened in write mode, the existing contents will be deleted before writing.

# 8. How do you tell the difference between read() and readlines()?
# 
# Ans:
# 
# read() reads the entire file and returns a string and readlines() returns a list of strings representing the lines of the file.

# 9. What data structure does a shelf value resemble?
# 
# Ans:
# 
# A shelf value resembles a dictionary value; it has keys and values, along with keys() and values() methods that work similarly to the dictionary methods of the same names.

# In[ ]:




