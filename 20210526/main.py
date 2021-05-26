import json

p = json.loads('''[
{"name":"Pedro", "age":25}, 
{"name":"Juan", "age":19},
{"name":"Andres", "age":22}
]''')

total = 0
for i in p["students"]:
    total += i["age"]
print(total)

# p = json.loads('''{ "students":
# [
# {"name":"Pedro", "age":25},
# {"name":"Juan", "age":19},
# {"name":"Andres", "age":22}
# ]}''')
#
# total = 0
# for i in p["students"]:
#     total += i["age"]
# print(total)

# p = json.loads('{ "students": [ "Pedro", "Juan", "Andres" ] }')
# print(p["students"][1])
#
# for i in p["students"]:
#     print(i)

# p = json.loads('[ "Hola", "Python", "desde", "JavaScript" ]')
# print(p)
# print(type(p))
# print(p[1])
# print(p[3])

# p = json.loads('{ "id":5, "first_name":"Erick" }')
# print(p)
# print(type(p))
# print(p["id"])
# print(p["first_name"])
