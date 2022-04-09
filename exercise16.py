w, n = [int(i) for i in input().split()]
bricks = [int(i) for i in input().split()]
bricks.sort()
matrix = []

for i in range(n):
    matrix.append([0] * (w + 1))

for i in range(len(matrix)):
    for j in range(1, len(matrix[0])):
        if bricks[i] <= j:
            if i:
                if matrix[i - 1][j - bricks[i]] + bricks[i] > matrix[i - 1][j]:
                    matrix[i][j] = matrix[i - 1][j - bricks[i]] + bricks[i]
                else:
                    matrix[i][j] = matrix[i - 1][j]
            else:
                matrix[i][j] = matrix[i - 1][j - bricks[i]] + bricks[i]
        else:
            matrix[i][j] = matrix[i - 1][j]

print(matrix[n-1][w])