print('\n1-------------------------------------------\n')
# plaintext and binary files

# plaintext
# - only contain basic text characters
# - didn't include any information about font, size or colour
# - usually with .txt file extension
# - can be opened with programs like Windows, Notepad or tense text edit application


# binary files
# - every other type of file
# - Word processing documents, PDF, images, spreadsheets, executable programs

print('\n2-------------------------------------------\n')
# open(), read() and close() method
# read() - return a single string

a = open('D:\\Python\\Section 11 - Files\\1234.txt')
content = a.read()
print(content)
a.close()

print('\n3-------------------------------------------\n')
# readlines() method - return a list of strings

b = open('D:\\Python\\Section 11 - Files\\1234.txt')
content = b.readlines()
print(content)
b.close()

print('\n4-------------------------------------------\n')
# write mode ('w') - overwrite value with a new value
# write() method

c = open('D:\\Python\\Section 11 - Files\\12345.txt','w') # filename = 12345
content = c.write('Hello!!!!!')
print(content) # 10 - write() will return the integer of how many bytes of the charactes wrote
c.close()

print('\n5-------------------------------------------\n')
# open file without a path
# Python will going to use the file path relative to the current working directory

baconFile = open('bacon.txt','w') # just open with a file name
baconFile.write('Bacon is not a vegetable.')
baconFile.close()

# for checking
import os
print(os.getcwd()) # D:\Python\Section 11 - Files


print('\n6-------------------------------------------\n')
# append mode ('a') - append the text that you're writing to the end of an existing file

d = open('D:\\Python\\Section 11 - Files\\12345.txt','a')
# if 'D:\\Python\\Section 11 - Files\\12345.txt' doesn't existing, python will open a new file 
d.write('\n\nHello world!!!!')
d.close()

print('\n7-------------------------------------------\n')
# the shelve module - store variables that have lists, dictionaries and other complex data structures

import shelve

# shelve.open() method

shelveFile = shelve.open('mydata') # will create 3 file - 'mydata.bak', 'mydata.dat', 'mydata.dir'
shelveFile['cats'] = ['Alan', 'Caemas', 'Handsome', 'Pretty']
print(shelveFile['cats']) # ['Alan', 'Caemas', 'Handsome', 'Pretty']
shelveFile.close()
                        

print('\n8-------------------------------------------\n')
# the key() and values() Shelf methods

shelveFile = shelve.open('mydata')
e = list(shelveFile.keys())
print(e) # ['cats']

f = list(shelveFile.values())
print(f) # [['Alan', 'Caemas', 'Handsome', 'Pretty']]
shelveFile.close()































































