# input:
#     Logic123!@While
# output:
# ['123', 'LogicWhile', '!@']
import string
def separation(s):
    res=[]
    no=''
    letters=''
    special=''
    for i in s:
        if i in string.digits:
            no+=i
        elif i in string.punctuation:
            special+=i 
        elif i in string.ascii_letters:
            letters+=i 
    res.append(no)
    res.append(letters)
    res.append(special)
    return res
s=input()
print(separation(s))
