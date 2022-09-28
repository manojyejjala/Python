#print a dictionary
thisdict= {
    "brand": "Ford",
	"model": "Mustang",
	"year": 1964
}
print(thisdict)

#print the "brand" value of the dictionary
thisdict= {
    "brand": "Ford",
	"model": "Mustang",
	"year": 1964
}
print(thisdict["brand"])

#duplicates values will overwrite existing values

thisdict= {
    "brand": "Ford",
	"model": "Mustang",
	"year": 1964,
    "year": 2020
}
print(thisdict)