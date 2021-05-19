import json

# x = '''[
#   { "id": 7825, "name": "Álgebra lineal", "level": 1, "credits": 8 },
#   { "id": 3085, "name": "Cálculo diferencial", "level": 1, "credits": 8 },
#   { "id": 9212, "name": "Fundamentos de programación", "level": 1, "credits": 5 },
#   { "id": 5995, "name": "Física aplicada", "level": 1, "credits": 7 },
#   { "id": 7693, "name": "Fundamentos de software", "level": 1, "credits": 7 },
#   { "id": 1030, "name": "Matemáticas discretas", "level": 2, "credits": 7 }
#   ]'''

f = open("students.json", "r")
students = json.loads(f.read())

print(students[0]["last_name"])
print(students[4]["id"])

print([s["first_name"] for s in students])
