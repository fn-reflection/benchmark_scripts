from time import time
import logging
from functools import partial
import numpy as np
from fn_reflection.time import timeit
def matmul(A, B):
    return np.dot(A, B)


def vecmul(C, D):
    return np.dot(C, D)


def singular_decomp(E):
    return np.linalg.svd(E, full_matrices=False)


def cholesky_decomp(F):
    return np.linalg.cholesky(F)


def eigen_decomp(G):
    return np.linalg.eig(G)

def main():
    logging.basicConfig(level=logging.DEBUG)
    logger =logging.getLogger(__name__)
    logger.debug('numpy blas configuration:')
    np.__config__.show()
    np.random.seed(0)
    size = 4096
    A, B = np.random.random((size, size)), np.random.random((size, size))
    C, D = np.random.random((size * 128,)), np.random.random((size * 128,))
    E = np.random.random((int(size / 2), int(size / 4)))
    F = np.random.random((int(size / 2), int(size / 2)))
    F = np.dot(F, F.T)
    G = np.random.random((int(size / 2), int(size / 2)))
    d = {}
    timeit(partial(matmul,A,B),out=logger,with_args_digest=True)
    timeit(partial(vecmul,C,D),out=logger,with_args_digest=True)
    timeit(partial(singular_decomp,E),out=logger,with_args_digest=True)
    timeit(partial(cholesky_decomp,F),out=logger,with_args_digest=True)
    timeit(partial(eigen_decomp,G),out=logger,with_args_digest=True)
    print(d)



if __name__ == "__main__":
    main()
