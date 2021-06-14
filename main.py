from random import randint
from datetime import datetime


def time_work(func):
    def wrap(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        res_time = datetime.now() - start
        print(f"time work function {func.__name__}: {res_time.microseconds}\n")
        return result
    return wrap


@time_work
def generate_print_matrix(size):
    _matrix = [[randint(1, 9) for j in range(size)] for i in range(size)]
    [print(i) for i in _matrix]
    return _matrix


@time_work
def print_forward_matrix(_matrix):
    res = []
    for i in range(len(_matrix)):
        for j in range(len(_matrix[i])):
            res.append(_matrix[i][j])
        res.append('|')
    print(res)


@time_work
def print_reverse_matrix(_matrix):
    res = []
    for i in range(len(_matrix)-1, -1, -1):
        for j in range(len(_matrix)-1, -1, -1):
            res.append(_matrix[i][j])
        res.append('|')
    print(res)


@time_work
def print_diagonal(_matrix):
    res = []
    for i in range(len(_matrix)):
        for j in range(len(_matrix[i])):
            if i == j:
                res.append(_matrix[i][j])
    print(res)


@time_work
def print_side_diagonal(_matrix):
    res = []
    for i in range(len(_matrix)):
        j = len(_matrix) - 1 - i
        res.append(_matrix[i][j])
    print(res)


@time_work
def print_both_diagonals_without_center(_matrix):
    def even(_size):
        """ Return True if even """
        return True if size % 2 == 0 else False

    res_side = []
    res_forward = []

    size = len(_matrix)
    mid_str = (size // 2)

    for i in range(size):
        if i == mid_str and not even(size):
            continue
        j_side = size - 1 - i
        res_side.append(_matrix[i][j_side])
        for j_forward in range(size):
            if i == j_forward:
                res_forward.append(_matrix[i][j_forward])
    print(f"res_forward: {res_forward}")
    print(f"   res_side: {res_side}")


@time_work
def print_spiral(_matrix):
    res = []

    size = len(_matrix)
    mid = (size // 2)

    # first central element
    res.append(_matrix[mid][mid])

    print(res)


matrix = generate_print_matrix(6)

# print_forward_matrix(matrix)
# print_reverse_matrix(matrix)
#
# print_diagonal(matrix)
# print_side_diagonal(matrix)
#
# print_both_diagonals_without_center(matrix)

print_spiral(matrix)
