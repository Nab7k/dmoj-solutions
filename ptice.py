


n = int(input())

c_letter = str(input())


adrian = 'ABC'
bruno = 'BABC'
goran = 'BBAACC'


a = 0
b = 0 
g = 0

for i in range(0,len(c_letter,),1):
    if c_letter[i] in adrian:
        a += 1
        continue
    elif c_letter[i] in bruno:
        b += 1 
        continue
    elif c_letter[i] in goran:
        g += 1

print(a,b,g)
