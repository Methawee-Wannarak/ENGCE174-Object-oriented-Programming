# Dictionary initialization
person = {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Accessing values
person['age'] = 31
print("Updated age:" , person['age'])

#Iterating through keys and values
for key , value in person.items():
    print(f"{key}: {value}")