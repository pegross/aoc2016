def is_valid_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a


triangles = []
with open('input/3') as f:
    for line in f:
        temp = map(lambda x: x.strip(), line.split(" "))
        temp = filter(lambda x: x != "", temp)
        temp = tuple(map(lambda x: int(x), temp))
        triangles.append(temp)

triangles = list(filter(lambda tri: is_valid_triangle(*tri), triangles))
print(len(triangles))
