def is_valid_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a


def part_b_reformat(triangle_list: list) -> list:
    new_list = []
    index = 0
    while index + 2 < len(triangle_list):
        new_list.extend([
            (triangle_list[index][0], triangle_list[index + 1][0], triangle_list[index + 2][0]),
            (triangle_list[index][1], triangle_list[index + 1][1], triangle_list[index + 2][1]),
            (triangle_list[index][2], triangle_list[index + 1][2], triangle_list[index + 2][2]),
        ])
        index += 3

    return new_list


triangles = []
with open('input/3') as f:
    for line in f:
        temp = map(lambda x: x.strip(), line.split(" "))
        temp = filter(lambda x: x != "", temp)
        temp = tuple(map(lambda x: int(x), temp))
        triangles.append(temp)

# part b
triangles = part_b_reformat(triangles)

triangles = list(filter(lambda tri: is_valid_triangle(*tri), triangles))
print(len(triangles))
