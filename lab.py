x = "5"
y = str(6)
z = "Abc"
w = "efg"
c = w.len
print(x + y)
print(z + w)
print(x + z)

i = 1
while i < 10:
    print(i)
    i += 1

x = [1, 2, 3, 4, 5]
for i in x:
    print(i)

x = "5"      
y = 6        
z = "Abc"    
w = "efg"   
c="abc efg"
print(x,y)
print(z + w) 
print(x + z)

print(len(c))
print(c[0:2])
print(c[0:5])
print(c[0:])
print(c[:])
print(c[len("5"):len("2")])
f = c.capitalize()
g=c.upper()
print(f)
print(g)
k="ab bc ca ab"
#l=k.count("ab")
l=k.count("bc")
p=k.find("bc")
x=k.find("ca")
q = k.replace("ab", "sa",1)
print(p)
print(x)
#print(l)
print(l)
print(q)
print(k.split())
print(k.split("a"))
f="        abc           "
lo="  ab  abc    "
kk=f.strip()
print(kk)
print(lo.strip(" a"))
print(lo.strip(" ab"))
j=("ab , cd , ef")
h="/"
print(h.join(j))
#print(10<5)

da=["ab"]
f=da
v=["ab"]
print(da == v)
print(da == f)
print(da is not f)

ind = ["ab", "bc"]

if "ab" in ind:
    print("Yes")
else:
    print("No")

a=10
b=5

if a>b: print("a > b")
 
#elif a<b: print("b is greater")  
  
else: print("a < b")  

i=1
while(i<10):
  print(i)



    
for i in range (3):
    print(x[i]);    


x=10
def f():
    x=4
    print(x)
    #print(5 < 10)

from numpy import append


x=["ab", "bc", "cd","ab"]
y=["ab",1,44.5]
print(x)
print(len(x))
print(y)
print(x[1])

x[1]=6
x[0:2]=["xy","ef"]
print(x)
x.append("kely")
x.insert(2, "gh")
print(x)

del x[1]
print(x)