########## 1의 (가) ##########
# immutable 객체
a = 1
b = 1
print(id(a), id(b))   # id(a) :               , id(b) :                    

c = "Hello"
d = "Hello"
print(id(c), id(d))   # id(c) :               , id(d) :                    


########## 1의 (나) ##########
# mutable 객체
a = [10, 20]
b = [10, 20]
print(id(a), id(b))  # id(a) :               , id(b) :                    

c = {30, 40}
d = {30, 40}
print(id(c), id(d))   # id(c) :               , id(d) :                    


########## 2의 (가) ##########
# immutable 객체 변경
a = 10
print(a, id(a))       # a :  10     ,    id(a) :                   

a = a + 1     # 변경

print(a, id(a))       # a :         ,    id(a) :


########## 2의 (나) ##########
# mutable 객체 변경
L = [10, 20]
print(L, id(L))      # L : [10, 20],    id(L) :                   

L[0] = 100    # 변경

print(L, id(L))      # L :         ,    id(L) : 


########## 3의 (가) ##########
L1 = [1, 2, [30, 40]]   
L2 = [1, 2, [30, 40]]

print(L1, id(L1)) # L1 : [1, 2, [30, 40]], id(L1) :              
print(L2, id(L2)) # L2 : [              ], id(L2) :              

L1[0] = 10           # 변경
L2[2][1] = 400       # 변경

print(L1, id(L1)) # L1 : [              ], id(L1) :              
print(L2, id(L2)) # L2 : [              ], id(L2) :              


########## 3의 (나) ##########
L1 = [1, 2, [30, 40]]   
L2 = L1

print(L1, id(L1)) # L1 : [1, 2, [30, 40]], id(L1) :              
print(L2, id(L2)) # L2 : [              ], id(L2) :              

L1[0] = 10           # 변경
L2[2][1] = 400       # 변경

print(L1, id(L1)) # L1 : [              ], id(L1) :              
print(L2, id(L2)) # L2 : [              ], id(L2) :              


########## 3의 (다) ##########
import copy

L1 = [1, 2, [30, 40]]   
L2 = copy.copy(L1)      # (copy()함수로) 얕은 복사

print(L1, id(L1)) # L1 : [1, 2, [30, 40]], id(L1) :              
print(L2, id(L2)) # L2 : [              ], id(L2) :              

L1[0] = 10           # 변경
L2[2][1] = 400       # 변경

print(L1, id(L1)) # L1 : [              ], id(L1) :              
print(L2, id(L2)) # L2 : [              ], id(L2) :              


print(L1[2], id(L1[2])) # L1[2] : [        ], id(L1) :           
print(L2[2], id(L2[2])) # L2[2] : [        ], id(L2) :           


########## 3의 (라) ##########
import copy

L1 = [1, 2, [30, 40]]   
L2 = copy.deepcopy(L1)      # (deepcopy()함수로) 깊은 복사

print(L1, id(L1)) # L1 : [1, 2, [30, 40]], id(L1) :              
print(L2, id(L2)) # L2 : [              ], id(L2) :              

L1[0] = 10           # 변경
L2[2][1] = 400       # 변경

print(L1, id(L1)) # L1 : [              ], id(L1) :              
print(L2, id(L2)) # L2 : [              ], id(L2) :              


print(L1[2], id(L1[2])) # L1[2] : [        ], id(L1) :           
print(L2[2], id(L2[2])) # L2[2] : [        ], id(L2) :           


########## 5의 (가) ##########
def Immutable_Func(i) :
    i = 100             # 값 변경
    print(i, id(i))   # i:     , id(i):          

i = 10                 # 정수(immutable)
Immutable_Func(i)
print(i, id(i))       # i:     , id(i):          


########## 5의 (나) ##########
def Mutable_Func(L) :
    L[0] = 100     # 값 변경
    print(L)    # L:      , id(L):              

L = [10]          # 리스트(mutable)
Mutable_Func(L)
print(L, id(L)  # L:      , id(L):              



########## 6의 (가) ##########
import copy

def Mutable_Func(L) :
    L[0] = 100
    L[2][0] = 300
    print(L, id(L))   # L:       , id(L):        

L = [1, 2, [30, 40]]
Mutable_Func([1, 2, [30, 40]])
print(L, id(L))       # L:       , id(L):        


########## 6의 (나) ##########
import copy

def Mutable_Func(L) :
    L[0] = 100
    L[2][0] = 300
    print(L, id(L))   # L:       , id(L):        

L = [1, 2, [30, 40]]
Mutable_Func(L)
print(L, id(L))       # L:       , id(L):        


########## 6의 (다) ##########
import copy

def Mutable_Func(L) :
    L[0] = 100
    L[2][0] = 300
    print(L, id(L))   # L:       , id(L):        

L = [1, 2, [30, 40]]
Mutable_Func(copy.copy(L))  # 혹은 L[:]
print(L, id(L))       # L:       , id(L):        


########## 6의 (라) ##########
import copy

def Mutable_Func(L) :
    L[0] = 100
    L[2][0] = 300
    print(L, id(L))   # L:       , id(L):        

L = [1, 2, [30, 40]]
Mutable_Func(copy.deepcopy(L))
print(L, id(L))       # L:       , id(L):        
