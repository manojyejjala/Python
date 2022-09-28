#get a list of the key:value pairs

thisdict= {
    "brand": "Ford",
	"model": "Mustang",
	"year": 1964
}
x=thisdict.items()
print(x)

#make a change in original dictionary and check updated list

thisdict={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}

x=thisdict.items()

print(x) #before the change
thisdict["year"]=2020
print(x) #after the change

#add new item to the original directory and check the updated items

thisdict={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}

x=thisdict.items()

print(x) #before the change
thisdict["colour"]="red"
print(x) #after the change