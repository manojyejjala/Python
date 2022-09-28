#get the value of the "model"

thisdict= {
    "brand": "Ford",
	"model": "Mustang",
	"year": 1964
}
x=thisdict["model"]
print(x)

#get the value of the model using get

thisdict= {
    "brand": "Ford",
	"model": "Mustang",
	"year": 1964
}
x=thisdict.get("model")
print(x)


#get a list of the keys

thisdict= {
    "brand": "Ford",
	"model": "Mustang",
	"year": 1964
}
x=thisdict.keys()
print(x)

#add item and check the change in keys

thisdict= {
    "brand": "Ford",
	"model": "Mustang",
	"year": 1964
}

x=thisdict.keys()
print(x)  #before the change

thisdict["colour"]="white"

print(x) #after the change

#check if key exists

thisdict={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
if "model" in thisdict:
    print("Yes,'model' is one of the keys in the thisdict dictionary")



