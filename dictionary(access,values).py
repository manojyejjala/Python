#get the list of values

thisdict= {
    "brand": "Ford",
	"model": "Mustang",
	"year": 1964
}
x=thisdict.values()
print(x)

#make change in original dictionary check values list get updated
thisdict= {
    "brand": "Ford",
	"model": "Mustang",
	"year": 1964
}

x=thisdict.values()
print(x)  #before the change

thisdict["year"]=2020

print(x) #after the change

#add new item and check the update of values
thisdict= {
    "brand": "Ford",
	"model": "Mustang",
	"year": 1964
}

x=thisdict.values()
print(x)  #before the change

thisdict["colour"]="red"

print(x) #after the change