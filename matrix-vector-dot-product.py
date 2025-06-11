## Question: Write a Python function that computes the dot product of a matrix and a vector. The function should return a list representing the resulting vector if the operation is valid, or -1 if the matrix and vector dimensions are incompatible. 

def matrix_dot_vector(a:list[list[int|float]], b: list[int|float]) -> list[int|float]:
    if len(a[0]) != len(b):
        return -1
    dot_product = 0
    for row in a:
        sum = 0
        for x in range(len(row)):
            sum += row[x] * b[x]
        dot_product.append(sum)
    return dot_product