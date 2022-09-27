#remove items from set
thisset={"apple","banana","cherry"}
thisset.remove("banana")
print(thisset)

#remove item using discard()
thisset={"apple","banana","cherry"}
thisset.discard("banana")
print(thisset)

#remove last item using the pop()
thisset={"apple","banana","cherry"}
x=thisset.pop()
print(x)
print(thisset)

#empties the set
thisset={"apple","banana","cherry"}
thisset.clear()
print(thisset)

#del the set completely
thisset={"apple","banana","cherry"}
del thisset
print(thisset)