#Basic slices
from array import array
arr= array('i',[10,20,30,40,50])
print(arr[1:4])#index 1 to 3
print(arr[:3])#start to index
print(arr[2:1])#index 2 to end
print(arr[:])#entire array"""


#slicing with step
"""from array import array
arr=array('i',[10,20,30,40,50])
print(arr[::2])#every second element
print(arr[1::2])#every second element starting from index 1
print(arr[::3])#every thired element"""


#Negative slicing
"""from array import array
arr=array('i',[10,20,30,40,50])
print(arr[-4:-1])#every second element
print(arr[-3:1])#every second element starting from index 1
print(arr[:-2])#every thired element"""


#Reverse array using slicing
"""from array import array
arr=array('i',[10,20,30,40,50])
print(arr[::-1])#reverse entire array"""


#Modifying slices
"""from  array import array
arr=array('i',[10,20,30,40,50])
arr[1:4]=array('i',[25,35,45])
print(arr)"""



