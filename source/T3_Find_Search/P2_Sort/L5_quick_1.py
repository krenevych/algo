def qsort(v, left, right):
    if left >= right:
        return
    pivot = v[left + (right - left) // 2]
    i = left
    j = right
    while True:
        while v[i] < pivot:
            i += 1
        while pivot < v[j]:
            j -= 1
        if i >= j:
            break
        v[i], v[j] = v[j], v[i]  # swap
        i += 1
        j -= 1

    qsort(v, left, j)
    qsort(v, j + 1, right)
