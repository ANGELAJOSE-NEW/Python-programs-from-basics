student_data={
  "Payal":{"roll_no":45,"age":20,"course":"python"},
  "Mohan":{"roll_no":50,"age":20,"course":"python"}
}
print(student_data)
print(student_data["Payal"])
print(student_data["Mohan"]["roll_no"])
student_data["Mohan"]["Phone_no"]=467829
print(student_data["Mohan"])
del student_data["Mohan"]["Phone_no"]
print(student_data["Mohan"])
print(student_data["Mohan"].pop("course"))

#list within a dictionary
travel_data={
  "Kannur":["Bekal fort","Palakkayamthatt"],
  "Kozhikkkode":["Beach"]
}
print(travel_data)
#Dictionary within a list
student=[{"name":"Payal","roll_no":45,"age":20,"course":"python"},
         {"name":"Rohan","roll_no":48,"age":20,"course":"python"}]

print(student[0])
print([student[1]["age"]])
