from random import randint
from datetime import datetime


def time_work(func):
    def wrap(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        res_time = datetime.now() - start
        print(f"time work fucntion !{func.__name__}!: {res_time}")
        return result
    return wrap


@time_work
def generate_print_matrix(n):
    _matrix = [[randint(1, 9) for j in range(n)] for i in range(n)]
    [print(i) for i in _matrix]
    return _matrix


@time_work
def print_forward(_matrix):
    res = [j for i in _matrix for j in i]
    print(res)


@time_work
def print_reverse(_matrix):
    res = [j for i in _matrix[::-1] for j in i[::-1]]
    print(res)


matrix = generate_print_matrix(15)
print_forward(matrix)
print_reverse(matrix)
