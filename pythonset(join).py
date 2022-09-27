#joining sets using union()
set1={"apple","banana","cherry"}
set2={1,2,3}

set3=set1.union(set2)
print(set3)

#joining sets using update()
set1={"apple","banana","cherry"}
set2={1,2,3}

set1.update(set2)
print(set1)