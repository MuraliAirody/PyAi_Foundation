D, R, C = 3,4,6

matrix = []

for i in range(D):
    depth_layer = []
    for j in range(R):
        row = []
        for k in range(C):
            row.append(i * j + k)
        depth_layer.append(row)
    matrix.append(depth_layer)

print("[")
for idx, layer in enumerate(matrix):
    print("    " + str(layer) + ("," if idx < D - 1 else ""))
print("]")
