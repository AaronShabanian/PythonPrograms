a=0
b=0
c=0
d=0
e=0
f=0
g=0
h=0
i=0
j=0
k=0
l=0
m=0
n=0
o=0
p=0
q=0
r=0
s=0
t=0
u=0
v=0
w=0
x=0
y=0
z=0
new=[]
maxcount=0
filename=input("what is the name of the file?: ")
text=open(filename,"r")
for line in text:
    line=line.lower()
    for char in line:
        print(char)
        if char=='a':
            a=a+1
        elif char=='b':
            b=b+1
        elif char=='c':
            c=c+1
        elif char=='d':
            d=d+1
        elif char=='e':
            e=e+1
        elif char=='f':
            f=f+1
        elif char=='g':
            g=g+1
        elif char=='h':
            h=h+1
        elif char=='i':
            i=i+1
        elif char=='j':
            j=j+1
        elif char=='k':
            k=k+1
        elif char=='l':
            l=l+1
        elif char=='m':
            m=m+1
        elif char=='n':
            n=n+1
        elif char=='o':
            o=o+1
        elif char=='p':
            p=p+1
        elif char=='q':
            q=q+1
        elif char=='r':
            r=r+1
        elif char=='s':
            s=s+1
        elif char=='t':
            t=t+1
        elif char=='u':
            u=u+1
        elif char=='v':
            v=v+1
        elif char=='w':
            w=w+1
        elif char=='x':
            x=x+1
        elif char=='y':
            y=y+1
        elif char=='z':
            z=z+1
maxchar=int(a)
letter='a'
if b>maxchar:
    maxchar=b
    letter='b'
elif c>maxchar:
    maxchar=c
    letter='c'
elif d>maxchar:
    maxchar=d
    letter='d'
elif e>maxchar:
    maxchar=e
    letter='e'
elif f>maxchar:
    maxchar=f
    letter='f'
elif g>maxchar:
    maxchar=g
    letter='g'
elif h>maxchar:
    maxchar=h
    letter='h'
elif i>maxchar:
    maxchar=j
    letter='j'
elif k>maxchar:
    maxchar=k
    letter='k'
elif l>maxchar:
    maxchar=l
    letter='l'
elif m>maxchar:
    maxchar=m
    letter='m'
elif n>maxchar:
    maxchar=n
    letter='n'
elif o>maxchar:
    maxchar=o
    letter='o'
elif p>maxchar:
    maxchar=p
    letter='p'
elif q>maxchar:
    maxchar=q
    letter='q'
elif r>maxchar:
    maxchar=r
    letter='r'
elif s>maxchar:
    maxchar=s
    letter='s'
elif t>maxchar:
    maxchar=t
    letter='t'
elif u>maxchar:
    maxchar=u
    letter='u'
elif v>maxchar:
    maxchar=v
    letter='v'
elif w>maxchar:
    maxchar=w
    letter='w'
elif x>maxchar:
    maxchar=x
    letter='x'
elif y>maxchar:
    maxchar=y
    letter='y'
elif z>maxchar:
    maxchar=z
    letter='z'
distance=(ord('e')-ord(letter))
def decrypt(filename, distance):
    text=open(filename,"r")
    for line in text:
        for char in line:
            if char.isalpha():
                if char.islower():
                    newchar=chr(ord(char)+distance)
                    if newchar.isalpha():
                        newchar=newchar
                    else:
                        neword=ord(char)+(26-distance)
                        newchar=chr(neword)
                    new.append(newchar)
                if char.isupper():
                    newchar=chr(ord(char)+distance)
                    if newchar.isalpha():
                        newchar=newchar
                    else:
                        neword=ord(char)+(26-distance)
                        newchar=chr(neword)
                    new.append(newchar)
            else:
                new.append(char)
decrypt(filename,distance)
print("".join(new))
