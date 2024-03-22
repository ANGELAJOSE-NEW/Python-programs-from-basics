phone_no={
  "Ram":1213,
  "Syam":3456,
  "Mohan":8904,
  "Syam":90552
}

# # phone_no=dict({
# #   "Ram":1213,
# #   "Syam":3456,
# #   "Mohan":8904,
# #   "Syam":90552
# # }
# # )
# print(phone_no)
# print(phone_no["Ram"])
# phone_no["Mohan"]=9999
# print(phone_no)
# phone_no["Madhav"]=[111,666] #Eventhough Madhav didnt exist this is fine
# print(phone_no)
# phone_no["Syam"]={"Syam_home":123,"Syam_office":890}
# print(phone_no)
# print(phone_no["Syam"]["Syam_home"])
# print(phone_no.get("Ram"))
# del phone_no["Ram"]
# print(phone_no.pop("Mohan"))
# print(phone_no)
# print(phone_no.popitem())
# # phone_no.clear()
# # print(phone_no)
# print(phone_no.keys())
# print(phone_no.values())
# print(phone_no.items())

for i in phone_no:
  print(i)

for i in phone_no:
  print(i)
  print(phone_no[i])

for i in phone_no.items():
  print(i)


phone_no2=phone_no.copy()
print(phone_no2)
print(len(phone_no2))