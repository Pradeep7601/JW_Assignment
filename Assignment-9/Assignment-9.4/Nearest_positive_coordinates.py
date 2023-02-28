# Assignment 9.4 - Nearest positive coordinates

coordinates = [(1,-2), (-2, 4), (-1,-1),(-8, -3), (0, 4), (10,-3)]
max_x = max_y = 0

for x, y in coordinates:
    if x < 0:
        max_x = max(max_x, abs(x))
    if y < 0:
        max_y = max(max_y, abs(y))

new_coordinates = [(x+max_x, y+max_y) for x, y in coordinates]

print(new_coordinates)
