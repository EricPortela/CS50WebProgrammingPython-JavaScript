from unicodedata import name


people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

#Since this is a very short and concise function, we can use lambda ("one-liner") instead
# def f(person):
#     return person["name"]

# people.sort(key=f)

people.sort(key=lambda person: person["name"])

print(people)