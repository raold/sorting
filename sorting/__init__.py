import heapq


def selection_sort(items):
    for fillslot in range(len(items)-1, 0, -1):
        position_max = 0
        for location in range(1, fillslot + 1):
            if items[location] > items[position_max]:
                position_max = location

        temp = items[fillslot]
        items[fillslot] = items[position_max]
        items[position_max] = temp


def bubble_sort(items):
    for i in range(len(items)):
        for j in range(len(items) - 1 - i):
            if items[j] > items[j+1]:
                items[j], items[j + 1] = items[j + 1], items[j]


def insertion_sort(items):
        for i in range(1, len(items)):
                j = i
                while j > 0 and items[j] < items[j-1]:
                        items[j], items[j-1] = items[j-1], items[j]
                        j -= 1


def merge_sort(items):
    if len(items) > 1:
        mid = len(items) // 2
        lefthalf = items[:mid]
        righthalf = items[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i = 0
        j = 0
        k = 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                items[k] = lefthalf[i]
                i = i + 1
            else:
                items[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            items[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            items[k] = righthalf[j]
            j = j + 1
            k = k + 1


def quick_sort(items):
    if len(items) > 1:
        pivot_index = len(items) / 2
        smaller_items = []
        larger_items = []

        for i, val in enumerate(items):
            if i != pivot_index:
                if val < items[pivot_index]:
                    smaller_items.append(val)
                else:
                    larger_items.append(val)

        quick_sort(smaller_items)
        quick_sort(larger_items)
        items[:] = smaller_items + [items[pivot_index]] + larger_items


def heap_sort(items):
    heapq.heapify(items)
    items[:] = [heapq.heappop(items) for i in range(len(items))]


def radix_sort(items):
    radix = 10
    max_length = False
    temp, placement = -1, 1

    while not max_length:
        max_length = True
        # declare and initialize buckets
        buckets = [list() for _ in range(radix)]

        # split items betwen lists
        for i in items:
            temp = i / placement
            buckets[temp % radix].append(i)
            if max_length and temp > 0:
                max_length = False

        # empty lists into items array
        a = 0
        for b in range(radix):
            buck = buckets[b]
            for i in buck:
                items[a] = i
                a += 1

        # move to next digit
        placement *= radix
