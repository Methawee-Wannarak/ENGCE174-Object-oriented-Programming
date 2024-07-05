# Tuple initalization
coordinates = (3, 5)

# Unpacking tuples
x, y = coordinates
print("x-coordinate:", x)
print("y-coordinate:", y)

# Tuple as keys in dictionary
location = {(3, 5): "Home" , (10, 20): "Office"}
print("Location at (3, 5):" , location[(3, 5)])