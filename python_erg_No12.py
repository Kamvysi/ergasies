# Creation of ascidict
print('# Creation of ascidict')
print(' ')
ascidict = {i: chr(i) for i in range(128)}
print(ascidict)

mytext = 'I just found out that IBM email platform goes under changes for the next two weeks, so if there is no response and problem persists please call Grigori'

# Reversing the ascidict, because the key value pair does not suit, I need value as key and key as value
print(' ')
print('# Reversing the ascidict, because the key value pair does not suit, I need value as key and key as value')
print(' ')
mydict = {v: k for k, v in ascidict.items()}
print(mydict)


import requests
import  numpy as np
firstdict = {"round":1650086,"randomness":"cb1c21bae97718963d14d3d7af7d2c91dda9a4fe34e3f57ba9a4172190d4daf2",
 "signature":"b97722444ff667fcc7a8dc27ffaefd80ce59e8e67586ea25683c451be25e9c057c5f9701c10e026cc16a0be94217bcad0f5d89d4ba5f6d037e55b8199d5b3f8249726343ce8476f011a3fb7d2a91860ac144f0b7cfeb926d5fc59be926107acc","previous_signature":"84ef481ff9aee779e1b27929acac314e2afabc23e48cebdfc868b20ffe19293a556d301f110f764b2705d0471c4e9a6c0ae6de3d5c8924e3255d32545fbb424decebefd417fbffdda6d82ba95698afdf215adbd964998a7a2cc3c3ac0b3395c5"}

start = firstdict['round']
finish = firstdict['round'] + 100

# Creation of list of urldicts
urldicts = []
for number in np.arange(start,finish, 1):
    r=requests.get('https://drand.cloudflare.com/public/1650045')
    d=r.json()
    urldicts.append(d)


urldicts

# List of the values of key randomness
randomnesslist = []
for somedict in urldicts:
    randomnesslist.append(somedict['randomness'])
print(randomnesslist)    

# Converting each character of my text in a number through the ascidict (mydict) from above
print(' ')
print('# Converting each character of my text in a number through the ascidict (mydict) from above')
print(' ')
mynumbers = []
for el in randomnesslist:
    for character in el:
        print(character, ':', mydict[character])
        mynumbers.append(mydict[character])
print(mynumbers)

# Turning into binary and checking that if the len is not 7, add a zero in the beginning
print(' ')
print('# Turning into binary and checking that if the len is not 7, add a zero in the beginning')
print(' ')
binned = []
lengths = []
for number in mynumbers:
    a = format(number, "b")
    lengths.append(len(a))
    if len(a) <7:
        a = '0' + str(a)
    binned.append(a)
print(binned)
from collections import Counter
print(Counter(lengths))


# Concatenating everything into a large string
print(' ')
print('# Concatenating everything into a large string')
print(' ')
concatlist = ''.join(binned)
print(concatlist)



# Counting consecutive appearances of 1 and 0 in tuples
print('# Counting consecutive appearances of 1 and 0 in tuples')
from itertools import groupby

groups = groupby(concatlist)
result = [(label, sum(1 for _ in group)) for label, group in groups]
print(result)


# Creation of list of tuples where the first element is 1
print('# Creation of list of tuples where the first element is 1')
assoi = []

for el in result:
    if el[0] == '1':
        assoi.append(el)
print(assoi)



# Creation of list of tuples where the first element is 0
print('# Creation of list of tuples where the first element is 0')
zeros = []
for el in result:
    if el[0] == '0':
        zeros.append(el)
print(zeros)


# Python program to sort a list of
# tuples by the second Item using sorted() 
  
# Function to sort the list by second item of tuple
def Sort_Tuple(listoftups): 
  
    # reverse = None (Sorts in Ascending order) 
    # key is set to sort using second element of 
    # sublist lambda has been used 
    return (sorted(listoftups, key = lambda x: x[1]))  

print('Sorted tuple of assoi')

print(Sort_Tuple(assoi)) 

print('Sorted tuple of zeros')

print(Sort_Tuple(zeros)) 

print('The biggest consecutive appearance of 1 is:',Sort_Tuple(assoi)[-1][1]) 

print('The biggest consecutive appearance of 0 is:',Sort_Tuple(zeros)[-1][1]) 
