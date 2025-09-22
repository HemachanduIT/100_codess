# input:
#     Logicwhile is the Best.
# output:
    # Total characters(with spaces): 23
    # Total characters(without spaces): 20
    # Total words: 4
    # Total sentences: 1
    # Total vowels: 7
    # Total consonants: 12
    # Total digits: 0

import string
s=input()
w=s.split()
w1=s.replace(" ","")
sen=s.count(".")+s.count("!")+s.count("?")
d_c=0
v_c=0
c_c=0
tot_char_with=len(s)
words_count=len(w)
tot_char_without=len(w1)
# print(sen)
v=['a','e','i','o','u','A','E','I','O','U']
z=list(string.ascii_letters)
# print(z)
conso=list(set(z)-set(v))
# print(conso)
d=list(string.digits)
# print(d)
for i in s:
    if i in d:
        d_c+=1
    elif i in v:
        v_c+=1
    elif i in conso:
        c_c+=1
print("Total characters(with spaces):",tot_char_with)
print("Total characters(without spaces):",tot_char_without)
print("Total words:",words_count)
print("Total sentences:",sen)
print("Total vowels:",v_c)
print("Total consonants:",c_c)
print("Total digits:",d_c)
        
