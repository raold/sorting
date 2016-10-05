from random import randint
from bench import tic, toc
from sorting import selection_sort, bubble_sort, insertion_sort, merge_sort, quick_sort, heap_sort, radix_sort


def benchmark(func):
    n = [5, 10, 100, 1000, 10000]

    for i in n:
        unsorted = [randint(-50, 100) for c in range(i)]
        tic()
        func(unsorted)
        print "%s(%d) \t %.4gs" % (func.__name__, i, toc())

benchmark(selection_sort)
benchmark(bubble_sort)
benchmark(insertion_sort)
benchmark(quick_sort)
benchmark(merge_sort)
benchmark(heap_sort)
benchmark(radix_sort)
