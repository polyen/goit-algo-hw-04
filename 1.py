from random import random
from timeit import timeit
from insert_sort import insertion_sort
from merge_sort import merge_sort


def measure_sort():
    tim_time = timeit(lambda: sorted([random() for _ in range(1000)]), number=1000)
    print('Час на сортування методом Timsort: ', tim_time)

    merge_time = timeit(lambda: merge_sort([random() for _ in range(1000)]), number=1000)
    print('Час на сортування методом злиття: ', merge_time)

    insert_time = timeit(lambda: insertion_sort([random() for _ in range(1000)]), number=1000)
    print('Час на сортування методом вставки: ', insert_time)



if __name__ == "__main__":
    measure_sort()
