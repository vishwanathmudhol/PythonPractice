a=10
b=12.553
c=9+8j
str="vishwanath mudhol"
''' 
#Integer examples
print(a," and type of the variable is ",type(a))
print(b," and type of the variable is ",type(b))
print(c," and type of the variable is ",type(c))
print(str," and type of the variable is ",type(str))

#String examples
print(str)
print(str[1])
print(str[1:10])
print(str[5:])
print(str*2)
print(str+" Mudalgi")
print(str)
'''
print(str.islower())
'''
#List examples
list=['Apple', 'Nokia', "Samsung", 13, 12.556]
print(list)
print(list[0])
print(list[0:3])
print(list[2:])
print(list*2)
print(list[0]*2)
print(type(list))
list.append("Black Berry")
print(list)
list.reverse()
print(list)
'''
#Tuple examples
'''tuple=("Orrange", "Mango", 13.009, 99, 'Banana')
print(tuple)
print(tuple[0])
print(tuple[1:3])
print(tuple[2:])
print(tuple[1:3]*2)
print(tuple*3)'''

#range(x) / range(x,y) / range(x,y,z)
for i in range(2):
    print(i," times Hi")

for i in range(1,5):
    print(i," times Hello")

for i in range(1,10,2):
    print(i," times Bye")