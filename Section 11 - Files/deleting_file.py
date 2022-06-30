
### the os's and shutil's  is permenant, the deleted file or folder will not go to recycle bin

print('\nos')
# os 
import os

print('\n1---------------------------------------------------\n')
# os.unlink() - delete a single file

#os.unlink('D:\\Python\\Section 11 - Files\\alan\\1234567.txt')
# '1234567.txt' file will deleted

print('\n2---------------------------------------------------\n')
# os.rmdir() - delete an empty folder

#os.rmdir('D:\\Python\\Section 11 - Files\\new')
# the 'new' folder will be remove when it is empty
# when the folder is not empty Python will give error

print('\nshutil')
# shutil
import shutil

print('\n3---------------------------------------------------\n')
# shutil.rmtree() - deletes a folder and its entire contents

#shutil.rmtree('D:\\Python\\Section 11- Files\\new')
# the 'new' folder will be delete whenever the folder is empty or not


print('\n4---------------------------------------------------\n')
# Dry Run

import os

for filename in os.listdir():
    if filename.endswith('.txt'): 
        #os.unlink(filename) # use comment and check before delete
        print(filename) # print out all the file before delete

        
print('\nsend2trash')
# send2trash
import send2trash

print('\n5---------------------------------------------------\n')
# send2trash module

#send2trash.send2trash('D:\\Python\\Section 11- Files\\new')
# 'new' folder or file will delete and send to recycle bin instead of delete permenantly
                        

