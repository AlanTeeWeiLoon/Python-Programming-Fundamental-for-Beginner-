
# the os.walk() function
import os

for folderName, subfolders, filenames in os.walk('D:\\Python\\Section 11 - Files'):
    print('The folder is ' + folderName)
    print('The subfolders in ' + folderName + ' are: ' + str(subfolders))
    print('The filenames in ' + folderName + ' are: ' + str(filenames))
    print()

    for subfolder in subfolders:
        #os.unlink(subfolder) # can detele all subfolder
        if 'Caemas' in subfolder: 
            #os.rmdir(subfolder) # delete all the folder that name with 'Caemas'
            print('rmfir on ' + subfolder) # rmfir on Caemas - check

    for file in filenames:
        if file.endswith('.txt'):
            #shutil.copy(os.join(folderName, file), os.join(folderName, file + '.backup'))
            # - copy the folder and all files inside the folder with a name end with '.backup'
            print('file.endswith on ' + file) # file.endswith on 1234567.txt - check


