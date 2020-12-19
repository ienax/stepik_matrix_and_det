import numpy as np
from numpy.linalg import matrix_rank

def f_2_2_6():
    A = np.array([[-2, 4, 0], [2, -5, 3], [2, 0, 6]])
    B = np.array([[-2, -4, 6], [1, 0, 3], [1, 2, -5]])
    E = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    print(sum(sum(0.5 * A + 2 * B - E)))


def f_2_8():
    a = np.array([3, 4, 2]).reshape(3, 1)
    b = np.array([5, -2, 3]).reshape(1, 3)
    ab = a @ b
    ba = b @ a
    print(ab)
    print(ba)
    print(sum(sum(ab)))
    print(sum(sum(ba)))
    print(sum(sum(ab)) + sum(sum(ba)))


def f_2_3_11():
    total = []
    for x in range(-10, 10):
        lst = np.array([[5, -3, x], [1, 1, -2], [2, x + 2, -1]])
        if -0.5 < np.linalg.det(lst) < 0.5:
            print(lst)
            print(np.linalg.det(lst))
            total += [x]
    print(f'total: {sum(total)}')


def f_2_4_12():
    d = np.array([[7, 8, 5, 5, 3], [10, 11, 6, 7, 5], [5, 3, 6, 2, 5], [6, 7, 5, 4, 2], [7, 10, 7, 5, 0]])
    print(np.linalg.det(d))


def f_2_5_6():
    A = np.array([[0, 0, 1, 1], [0, 3, 1, -7], [2, 7, 6, 1], [1, 2, 2, 1]])
    A_inv = np.linalg.inv(A)
    print(A_inv)


def f_2_5_7():
    # A*x*C=B
    a = np.array([[3,-1], [5,-2]])
    b = np.array([[14,16], [9,10]])
    c = np.array([[5,6], [7,8]])
    c_inv = np.linalg.inv(c)
    b = np.dot(b, c_inv)

    # A*x=B
    a_inv = np.linalg.inv(a)
    x = np.dot(a_inv, b)
    print(x.sum())

def f_2_6_6():
    m = np.array([[1, 1, 2, 3, -1], [2, -1, 0, -4, -5], [-1, -1, 0, -3, -2], [6, 3, 4, 8, -3]])
    print(matrix_rank(m))

def main():
    f_2_6_6()


if __name__ == "__main__":
    main()
