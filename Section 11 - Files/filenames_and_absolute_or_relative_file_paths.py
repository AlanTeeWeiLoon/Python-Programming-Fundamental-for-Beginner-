
print('\n1---------------------------------------\n')
# filename and file paths

a = 'c:\\spam\\eggs.py'
print(a) # c:\spam\eggs.py

print('\\') # \

b = r'c:\\spam\\eggs.py'
print(b) # c:\\spam\\eggs.py

print(r'c:\\spam\\eggs.py') # c:\\spam\\eggs.py

print('\n2---------------------------------------\n')
# use join() to create file paths

d = '\\'.join(['folder1','folder2', 'folder3', 'folder4', 'file.png'])
print(d) # folder1\folder2\folder3\folder4\file.png

print('\n3---------------------------------------\n')

import os # contain file paths related functions

# os.path.join()

e = os.path.join('folder1','folder2', 'folder3', 'folder4', 'file.png')
print(e) # folder1\folder2\folder3\folder4\file.png

print('\n4---------------------------------------\n')
# os.sep()

f = os.sep
print(f) # \

print('\n5---------------------------------------\n')
# os.getcwd() - get the file path of current working directory

g = os.getcwd() 
print(g) # D:\Python\Section 11 - Files

print('\n6---------------------------------------\n')
# os.chdir() -  to change the current working directory


# h = os.chdir('D:\\') - this file will change the directory to 'D:\\'
# print(os.getcwd()) # 'D:\\'

print('\n7---------------------------------------\n')
# absolute and relative paths

# absolute file path
# - always begin with the root folder (D:\\)
# - Exp: 'D:\folder1\folder2\folder3\folder4\file.png'


# relative file path
# - always going to be relative to the current working directory
# - not going to begin with the root folder
# - Exp: 'spam.py'
#   - assume that the 'spam.py' file is particular in the root folder
# - also can begin with other folders
# - Exp: 'folder1\folder2\spam.py'
#   - assume that this relative file path is inside of the root folder
#     and inside that root folder have a folder called folder1 and inside
#     folder1 there is folder2 and then 'spam.py'

print('\n8---------------------------------------\n')
# the . and .. folders

# .  - stands for this directory or this folder
# .. - means the parent folders

print('\n9---------------------------------------\n')
# os.path,abspath() and os.path.isabs()

# os.path.abspath() - return a string of an absolute path of the path you pass it
i = os.path.abspath('spam.png')
print(i) # D:\Python\Section 11 - Files\spam.png

j = os.path.abspath('..\\..\\spam.png')
print(j) # D:\spam.png - parent folder 'Section 11' is 'Python' and parent folder of 'Python' is 'D'.
         #               so the 'Section 11' and 'Python' folder will be disappear under '..' function

# os.path.isabs() - return True when is an absolute path
k = os.path.isabs('..\\..\\spam.png') # relative file path
print(k) # False

l = os.path.isabs('D:\\Python\\Section 11\\spam.png') # absolute file path
print(l) # True

print('\n10---------------------------------------\n')
# os.path.relpath() - give you the relative path between two paths

m = os.path.relpath('D:\\Python\\Section 11\\spam.png','D:\\Python')
print(m) # Section 11\spam.png

print('\n11---------------------------------------\n')
# os.path.dirname() and os.path.basename()

# os.path.dirname() - retrieve the directory part
n = os.path.dirname('D:\\Python\\Section 11\\spam.png')
print(n) # D:\Python\Section 11

# os.path.basename() - return the last part of the path
o = os.path.basename('D:\\Python\\Section 11\\spam.png')
print(o) # spam.png

p = os.path.basename('D:\\Python\\Section 11') # without file
print(p) # Section 11

print('\n12---------------------------------------\n')
# os.path.exists()
# - use when want to check file on the hard drive or not
# - return True if this file exists
# - return false if it does not exist

q = os.path.exists('D:\\Python\\Section 11\\spam.png') 
print(q) # False

r = os.path.exists('D:\\Python\\Section 11 - Files\\alan.py') 
print(r) # True

print('\n13---------------------------------------\n')
# os.path.isfile() and os.path.isdir()

# os.path.isfile() - return True when that is a file
s = os.path.isfile('D:\\Python\\Section 11 - Files\\alan.py') 
print(s) # True

t = os.path.isfile('D:\\Python\\Section 11 - Files') # without file
print(t) # False

# os.path.isdir() - return True the file path is for a directory
u = os.path.isdir('D:\\Python\\Section 11 - Files') # without file
print(u) # True

v = os.path.isdir('D:\\Python\\Section 11 - Files\\alan.py') 
print(v) # False

print('\n14---------------------------------------\n')
# os.path.getsize() and os.listdir()

# os.path.getsize()
w = os.path.getsize('D:\\Python\\Section 11 - Files\\filenames_and_absolute_or_relative_file_paths.py')
print(w) # 4847 - this file is 4847 bytes

# os.path.listdir() - list which file is inside the folder
x = os.listdir('D:\\Python\\Section 11 - Files')
print(x) # ['alan.py', 'alan.txt', 'filenames_and_absolute_or_relative_file_paths.py']

print('\n15---------------------------------------\n')
# Example Code: Finding the total size of all files in a folder


totalSize = 0
for filename in os.listdir('D:\\Python\\Section 11 - Files'):
    if not os.path.isfile(os.path.join('D:\\Python\\Section 11 - Files',filename)):
        continue
    totalSize = totalSize + os.path.isfile(os.path.join('D:\\Python\\Section 11 - Files',filename))

print(totalSize) # 2 - the total size of this folder is 2 bytes

print('\n16---------------------------------------\n')
# os.makedirs() - to create a new folder

y = os.makedirs('D:\\Python\\Section 11 - Files\\alan') # the folder named 'alan' had created


































