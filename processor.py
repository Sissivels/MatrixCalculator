A = []
B = []
result = []
constant = 0
user_choice = 0
error = "The operation cannot be performed"


def create_matrix(matrix_name, text, tex2):
    rows, columns = input(text).split()
    print(tex2)
    for i in range(int(rows)):
        # initiate rows
        row = []
        # create rows in matrix (empty boxes)
        matrix_name.append(row)
        # populate rows
        elements = input().split()
        for element in elements:
            if element.isdigit():
                element = int(element)
            else:
                element = float(element)
            row.append(element)


def matrix_sum():
    create_matrix(A, "Enter size of first matrix: ", "Enter first matrix:")
    create_matrix(B, "Enter size of second matrix: ", "Enter second matrix:")
    rows_A = int(len(A))
    columns_A = int(len(A[0]))
    rows_B = int(len(B))

    if rows_A != rows_B:
        print(error)
    else:
        for i in range(rows_A):
            # collect all sums here to make the rows:
            list_sum = []
            for j in range(columns_A):
                element_sum = A[i][j] + B[i][j]
                list_sum.append(element_sum)
            result.append(list_sum)
        print("The result is:")
        for row in result:
            print(*row)
    A.clear()
    B.clear()
    result.clear()


def matrix_constant_multiplication():
    create_matrix(A, "Enter size of matrix: ", "Enter matrix:")
    constant = input("Enter constant: ")
    if constant.isdigit():
        constant = int(constant)
    else:
        constant = float(constant)
    rows_A = int(len(A))
    columns_A = int(len(A[0]))
    result = []
    for i in range(rows_A):
        list_multiplication = []
        for j in range(columns_A):
            element_multiplic = A[i][j] * constant
            list_multiplication.append(element_multiplic)
        result.append(list_multiplication)
    print("The result is:")
    for row in result:
        print(*row)
    A.clear()
    B.clear()
    result.clear()


def matrix_x_matrix():
    # CREATE MATRICES:
    create_matrix(A, "Enter size of first matrix: ", "Enter first matrix:")
    create_matrix(B, "Enter size of second matrix: ", "Enter second matrix:")
    rows_A = int(len(A))
    columns_A = int(len(A[0]))
    rows_B = int(len(B))
    columns_B = int(len(B[0]))
    result = []
    # STEP1: CHECK IF OPERATION CAN BE DONE
    if columns_A == rows_B:
    # STEP2: CREATE RESULT MATRIX
        for i in range(rows_A):
            row = []            # initiate rows
            result.append(row)  # create rows in result matrix (empty boxes)
            for j in range(columns_B):  # initiate columns
                element = 0
                row.append(int(element))
    # STEP3: MULTIPLICATION
        for i in range(rows_A):
            for j in range(columns_B):
                for k in range(rows_B):
                    result[i][j] += A[i][k] * B[k][j]

    # STEP4: PRINT RESULT
        print("The result is:")
        for row in result:
            print(*row)
    A.clear()
    B.clear()
    result.clear()


def transpose_main_():
    create_matrix(A, "Enter size of matrix: ", "Enter matrix:")
    rows_A = int(len(A))
    columns_A = int(len(A[0]))
    result = []
    for i in range(columns_A):
            columns = []  # initiate columns
            result.append(columns)  # create columns  (empty boxes)
            for j in range(rows_A):
                element = A[j][i]
                columns.append(element)
    print("The result is:")
    for row in result:
        print(*row)
    A.clear()


def transpose_side():
    create_matrix(A, "Enter size of matrix: ", "Enter matrix:")
    rows_A = int(len(A))
    columns_A = int(len(A[0]))
    result = []
    for row in range(columns_A - 1, -1, -1):
        rows = []  # initiate columns
        result.append(rows)  # create columns in rows (empty boxes)

        for column in range(rows_A - 1, -1, -1):
            element = A[column][row]
            rows.append(element)
    print("The result is:")
    result = result[::-1]
    for row in result[::-1]:
        print(*row)
    A.clear()
    result.clear()


def transpose_horizontal():
    create_matrix(A, "Enter size of matrix: ", "Enter matrix:")
    rows_A = int(len(A))
    columns_A = int(len(A[0]))
    result = []
    A.reverse()
    for column in range(rows_A):
        columns = []  # initiate columns
        result.append(columns)  # create columns  (empty boxes)
        for row in range(columns_A):
            element = A[column][row]
            columns.append(element)
    print("The result is:")
    for row in result:
        print(*row)
    A.clear()
    result.clear()


def transpose_vertical():
    create_matrix(A, "Enter size of matrix: ", "Enter matrix:")
    rows_A = int(len(A))
    columns_A = int(len(A[0]))
    result = []
    for row in range(rows_A):
        rows = []
        result.append(rows)
        for column in range(columns_A):
            element = A[row][column]
            rows.append(element)
    print("The result is:")
    for row in result:
        row.reverse()
        print(*row)
        A.clear()
        result.clear()


def create_C_():
    global C
    C = []
    rows_A = int(len(A))
    columns_A = int(len(A[0]))
    for i in range(rows_A):          # Repeat the following x 2
        row = []               # initiate rows
        C.append(row)      # create rows in matrix C (empty boxes)
                                     # populate rows
        for j in range(columns_A):      # initiate columns
            element = A[i][j]
            row.append(element)


def determinant(A):
    create_matrix(A, "Enter size of matrix:", "Enter matrix:")
    global C
    total = 0
    indices = list(range(len(A)))
    create_C_()


    # Section 2: when at 2x2 submatrices recursive calls end
    if len(A) == 2 and len(A[0]) == 2:
        val = A[0][0] * A[1][1] - A[1][0] * A[0][1]
        return val

    # Section 3: define submatrix for focus column and call this function
    for fc in indices:  # for each focus column, find the submatrix ...
          # make a copy, and ...
        C = C[1:]  # ... remove the first row
        height = len(C)

        for i in range(height):  # for each remaining row of submatrix ...
            C[i] = C[i][0:fc] + C[i][fc+1:]  # zero focus column elements

        sign = (-1) ** (fc % 2)  # alternate signs for submatrix multiplier
        sub_det = determinant(C)  # pass submatrix recursively
        total += sign * A[0][fc] * sub_det  # total all returns from recursion
    print(total)
    return total





def menu_text():
    print("1. Add matrices\n"
          "2. Multiply matrix by a constant\n"
          "3. Multiply matrices\n"
          "4. Transpose matrix\n"
          "5. Calculate a determinant\n"
          "0. Exit\n")


def menu():
    menu_text()
    user_choice = int(input("Your choice: "))
    while user_choice != 0:
        if user_choice == 1:
            matrix_sum()
            print("\n")
            menu_text()
            user_choice = int(input("Your choice: "))
        elif user_choice == 2:
            matrix_constant_multiplication()
            print("\n")
            menu_text()
            user_choice = int(input("Your choice: "))
        elif user_choice == 3:
            matrix_x_matrix()
            print("\n")
            menu_text()
            user_choice = int(input("Your choice: "))
        elif user_choice == 4:
            second_choice = int(input("1. Main diagonal\n"
                                            "2. Side diagonal\n"
                                            "3. Vertical line\n"
                                            "4. Horizontal line\n"
                                            "Your choice: "))
            if second_choice == 1:
                transpose_main_()
                menu_text()
                user_choice = int(input("Your choice: "))
            elif second_choice == 2:
                transpose_side()
                menu_text()
                user_choice = int(input("Your choice: "))
            elif second_choice == 3:
                transpose_vertical()
                menu_text()
                user_choice = int(input("Your choice: "))
            elif second_choice == 4:
                transpose_horizontal()
                menu_text()
                user_choice = int(input("Your choice: "))
        elif user_choice == 3:
            matrix_x_matrix()
            print("\n")
            menu_text()
            user_choice = int(input("Your choice: "))

    else:
        quit()


menu()
