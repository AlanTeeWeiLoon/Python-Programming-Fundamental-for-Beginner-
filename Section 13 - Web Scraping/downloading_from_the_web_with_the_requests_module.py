# the requests module

import requests

# requests.get() returns a Respond object
res = requests.get('http://automatetheboringstuff.com/files/rj.txt')

print('\n1-----------------------------------------------\n')
# .status_code

print(res.status_code) # 200 - 200 ststus code means everythings when OK, 'error 404'

print('\n2-----------------------------------------------\n')
# .text

print(len(res.text)) # 178978

print('\n3-----------------------------------------------\n')
# .text[]

print(res.text[:500]) # Python will print the first 500 character of 'http://automatetheboringstuff.com/files/rj.txt'

print('\n4-----------------------------------------------\n')
# raise_for_status() = raise an exception if there was an error downloading the file

print(res.raise_for_status()) # None - all is fine

badRes = requests.get('http://automatetheboringstuff.com/fdssvgsvs.txt') 
#print(badRes.raise_for_status()) # 404 Client Error: Not Found for url: http://automatetheboringstuff.com/fdssvgsvs.txt

print('\n5-----------------------------------------------\n')
# write-binary mode: open(filename,'wb')

playFile = open('RomeoAndJuliet.txt','wb')
for chunk in res.iter_content(100000): # 
    playFile.write(chunk) # 'RomeoAndJuliet.txt' text file opened with contents

    print(playFile.write(chunk)) # 100000 78978 - write method will return an integer of how many bytes it wrote to this file
playFile.close()




