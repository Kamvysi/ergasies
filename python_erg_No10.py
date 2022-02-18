# Creation of ascidict
print('# Creation of ascidict')
print(' ')
ascidict = {i: chr(i) for i in range(128)}
print(ascidict)

mytext = 'I just found out that IBM email platform goes under changes for the next two weeks, so if there is no response and problem persists please call Athin Kamvisi'

# Reversing the ascidict, because the key value pair does not suit, I need value as key and key as value
print(' ')
print('# Reversing the ascidict, because the key value pair does not suit, I need value as key and key as value')
print(' ')
mydict = {v: k for k, v in ascidict.items()}
print(mydict)

# Converting each character of my text in a number through the ascidict (mydict) from above
print(' ')
print('# Converting each character of my text in a number through the ascidict (mydict) from above')
print(' ')
mynumbers = []
for character in mytext:
    print(character, ':', mydict[character])
    mynumbers.append(mydict[character])
print(mynumbers)

# Turning into binary and checking that if the len is not 7, add a zero in the beginning
print(' ')
print('# Turning into binary and checking that if the len is not 7, add a zero in the beginning')
print(' ')
binned = []
for number in mynumbers:
    a = format(number, "b")
    if len(a) <7:
        a = '0' + str(a)
    binned.append(a)
print(binned)

# Keeping only two first and last digits
print(' ')
print('# Keeping only two first and last digits')
print(' ')
endiam = []
for el in binned:
    a = el[:2] + el[-2:]
    endiam.append(a)
print(endiam)    

# Concatenating everything into a large string
print(' ')
print('# Concatenating everything into a large string')
print(' ')
concatlist = ''.join(endiam)
print(concatlist)

# Turning into 16 bits
print(' ')
print('# Turning into 16 bits')
print(' ')
n = 16
sixteendigits = [concatlist[i:i+n] for i in range(0, len(concatlist), n)]
print(sixteendigits)

# Converting again to int
print(' ')
print('# Converting again to int')
print(' ')
sixteendigits_to_int = []
for number in sixteendigits:
    a = int(number,2)
    print(a)
    sixteendigits_to_int.append(a)
print(sixteendigits_to_int)



evens = []
for num in sixteendigits_to_int:
    if num % 2 == 0:
        evens.append(num)
print(' ')
print('The percentage of evens is:', len(evens)/len(sixteendigits_to_int))
print(' ')

dividable_with_3 = []
for num in sixteendigits_to_int:
    if num % 3 == 0:
        dividable_with_3.append(num)
        
print('The percentage of dividable_with_3 is:', len(dividable_with_3)/len(sixteendigits_to_int))
print(' ')
dividable_with_5 = []
for num in sixteendigits_to_int:
    if num % 5 == 0:
        dividable_with_5.append(num)
        
print('The percentage of dividable_with_5 is:', len(dividable_with_5)/len(sixteendigits_to_int))
print(' ')
dividable_with_7 = []
for num in sixteendigits_to_int:
    if num % 7 == 0:
        dividable_with_7.append(num)
print('The percentage of dividable_with_7 is:', len(dividable_with_7)/len(sixteendigits_to_int))

