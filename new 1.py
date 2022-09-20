def generate_list(val,list=[]):
  list.append(val)
  return list 


  list1 = generate_list(100)
      print("list1")
  list2 = generate_list(123,[])
      print("list2")
  list3 = generate_list("abc")
      print("list3")