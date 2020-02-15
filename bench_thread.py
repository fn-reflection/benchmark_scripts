from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
import asyncio
import time
import profile
import random
from fn_reflection.time import timeit

def heavy_load(x):
    r = 0
    for i in range(10**5):
        if random.random() < 0.99:
            r += i % x
    return r

def with_tpe(tpe):
    r = [r for r in tpe.map(heavy_load, list(range(1, 16)))]
    print(r)

def with_ppe(ppe):
    r = [r for r in ppe.map(heavy_load, list(range(1, 16)))]
    print(r)

def with_none():
    r = [heavy_load(i) for i in range(1, 16)]
    print(r)

def main():
    TPEXECUTOR = ThreadPoolExecutor()
    PPEXECUTOR = ProcessPoolExecutor()

    start = time.time()
    with_tpe(TPEXECUTOR)
    elapsed = time.time() - start
    print(elapsed)

    start = time.time()
    with_ppe(PPEXECUTOR)
    elapsed = time.time() - start
    print(elapsed)

    start = time.time()
    with_none()
    elapsed = time.time() - start
    print(elapsed)

if __name__ == "__main__":
    main()