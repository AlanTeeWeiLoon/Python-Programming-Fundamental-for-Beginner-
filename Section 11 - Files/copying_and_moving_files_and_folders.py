import shutil

print('\n1------------------------------------\n')
# copy file - shutil.copy()

# just copy without rename file
shutil.copy('D:\\Python\\Section 11 - Files\\12345.txt','D:\\Python\\Section 11 - Files\\alan')
# '12345.txt' will copy to 'alan' folder

# copy and rename file
shutil.copy('D:\\Python\\Section 11 - Files\\12345.txt','D:\\Python\\Section 11 - Files\\alan\\123456.txt')
# '12345.txt' will copy to 'alan' folder with name '123456.txt'

print('\n2------------------------------------\n')
# copy entire folder - shutil.copytree()

#shutil.copy('D:\\Python\\Section 11 - Files\\alan','D:\\Python\\Section 11 - Files\\alan1')
# 'alan' folder will copied to a new folder called 'alan1'
# - Permission denied

print('\n3------------------------------------\n')
# move folder - shutil.move()

#shutil.move('D:\\Python\\Section 11 - Files\\alan\\123456.txt','D:\\Python\\Section 11 - Files')
# '123456.txt' will be move from 'alan' folder to 'Section 11 - Files' folder

print('\n4------------------------------------\n')
# shutil doesn't have rename function
# use shutil.move() function to rename

shutil.move('D:\\Python\\Section 11 - Files\\alan\\12345.txt','D:\\Python\\Section 11 - Files\\alan\\1234567.txt')
# move the file to the save location and give a new name to rename
# '12345.txt' in 'alan' folder will be rename to '1234567.txt'


