c=[]
p=' '
with open('./input','r')as f:
    c=[[l.split(p)[0],int(l.split(p)[1])]for l in f.readlines()]
a=h=v=0
for m in c:
    l,d=m[1],m[0]
    if d=='forward':
        h+=l
        v+=a*l
    else:
        a+=(l,-l)[d=='up']
print(v*h)
