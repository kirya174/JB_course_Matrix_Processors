import numpy as np

def is_int(x):
    try:
        a = float(x)
        b = int(a)
    except (TypeError, ValueError):
        return False
    else:
        return a == b


def conv_to_int_matrix(matrix):
    matrix_int = [[int(x) for x in line] for line in matrix]
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] - matrix_int[row][col] != 0:
                return [[float(x) for x in line] for line in matrix]
    return matrix_int


def print_output_matrix(printing_matrix):
    printing_matrix = conv_to_int_matrix(printing_matrix)
    print("The result is:")
    for line in printing_matrix:
        print('  '.join(map(str, line)))
    print()


def read_matrix(matrix_number=""):
    n, m = map(int, input(f"Enter {matrix_number}matrix size: ").split())
    new_matrix = list()
    print("Enter matrix:")
    for _ in range(n):
        new_matrix.append(list(map(float, input().split())))
    return new_matrix


def add_matrices(matrix_a, matrix_b):
    output_matrix = [[matrix_a[row][col] + matrix_b[row][col] for col in range(len(matrix_a[row]))] for row in
                     range(len(matrix_a))]
    return output_matrix


def mul_by_const(mul_matrix, const):
    const = int(const) if is_int(const) else float(const)
    mul_matrix = [[x * const for x in line] for line in mul_matrix]
    return mul_matrix


def mul_matrices(matrix_a, matrix_b):
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])

    # Dimensions would be rows_A x cols_B
    output = [[0 for row in range(cols_b)] for col in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                output[i][j] += matrix_a[i][k] * matrix_b[k][j]
    return output


def transpose_matrix(transpose_type, tr_matrix):
    if transpose_type == 1:  # main diagonal
        for i in range(0, len(tr_matrix)):
            for j in range(i, len(tr_matrix[i])):
                tr_matrix[i][j], tr_matrix[j][i] = tr_matrix[j][i], tr_matrix[i][j]
        return tr_matrix
    elif transpose_type == 2:  # side diagonal
        for i in range(0, len(tr_matrix)):
            for j in range(0, len(tr_matrix[i]) - (i + 1)):
                tr_matrix[i][j], tr_matrix[-j - 1][-i - 1] = tr_matrix[-j - 1][-i - 1], tr_matrix[i][j]
        return tr_matrix
    elif transpose_type == 3:  # vertical line
        return [x[::-1] for x in tr_matrix]
    elif transpose_type == 4:  # horizontal line
        return tr_matrix[::-1]


def calc_determinant(new_matrix, rows, cols):
    if rows == 1:
        return new_matrix[0][0]
    else:
        const = 1
        if new_matrix[0][0] == 0:
            const *= -1
            new_matrix[0], new_matrix[1] = new_matrix[1], new_matrix[0]
        for i in range(1, rows):
            if new_matrix[i][0] == 0:
                continue
            scalar = new_matrix[i][0] / new_matrix[0][0]
            for j in range(cols):
                new_matrix[i][j] = new_matrix[i][j] - scalar * new_matrix[0][j]
        return const * new_matrix[0][0] * calc_determinant([new_matrix[i][1:] for i in range(1, rows)], rows - 1,
                                                           cols - 1)


def inverse_matrix(matrix):
    a = matrix
    a_inv = np.linalg.inv(a)
    return (np.linalg.inv(np.array(matrix))).tolist()



while True:
    choice = int(input("1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices\n"
                       "4. Transpose matrix\n5. Calculate a determinant\n6. Inverse matrix\n0. Exit\nYour choice: "))
    if choice == 0:
        break

    elif choice == 1:
        matrix_a = read_matrix("first ")
        matrix_b = read_matrix("second ")
        if len(matrix_a) == len(matrix_b) and len(matrix_a[0]) == len(matrix_b[0]):
            print_output_matrix(add_matrices(matrix_a, matrix_b))
        else:
            print("The operation cannot be performed.", end='\n\n')

    elif choice == 2:
        print_output_matrix(mul_by_const(read_matrix(), int(input("Enter constant: "))))

    elif choice == 3:
        matrix_a = read_matrix("first ")
        matrix_b = read_matrix("second ")
        if len(matrix_a[0]) != len(matrix_b):
            print("The operation cannot be performed.", end='\n\n')
        else:
            print_output_matrix(mul_matrices(matrix_a, matrix_b))

    elif choice == 4:
        result_matrix = transpose_matrix(int(input("\n1. Main diagonal\n2. Side diagonal\n3. Vertical "
                                                                  "line\n 4. Horizontal line\nYour choice: ")), read_matrix())
        print_output_matrix(result_matrix)

    elif choice == 5:
        matrix = read_matrix()
        rows = len(matrix)
        cols = len(matrix[0])
        if rows == cols:
            det = calc_determinant(matrix, rows, cols)
            print("The result is:\n" + str(round(det) if round(det, 2) - round(det) < 0.1 else round(det, 2)),
                  end='\n\n')
        else:
            print("The operation cannot be performed.", end='\n\n')

    elif choice == 6:
        matrix = np.array(read_matrix())
        if np.linalg.det(matrix) == 0:
            print("This matrix doesn't have an inverse.", end='\n\n')
        else:
            # print_output_matrix(inverse_matrix(matrix))
            inv_matr = inverse_matrix(matrix)
            print_output_matrix(inv_matr)