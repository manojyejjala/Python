"""
Examples for enumerate and list operations

"""
list_1=[1, 2, 3, 4]
list_2=[1, 2, 3, 4]
list_3=[1, 2, 3, 4]
list_4=[1, 2, 3, 4]

for idx, item in enumerate (list_1):
    del item
for idx, item in enumerate (list_2):
    list_2.remove(item)
for idx, item in enumerate (list_3):
    list_3.remove(item)
for idx, item in enumerate (list_4):
    list_4.pop(idx)
	
print(list_1)
print(list_2)
print(list_3)
print(list_4)