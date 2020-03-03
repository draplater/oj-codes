def sort(a, start, end):
    if start >= end:
        return
    mid = partition(a, start, end)
    sort(a, start, mid - 1)
    sort(a, mid + 1, end)

def partition(a, start, end):
    i = start + 1
    j = end
    t = a[start]
    while i <= j:
        if a[i] > t and a[j] <= t:
            a[i], a[j] = a[j], a[i]
        while i <= end and a[i] <= t:
            i += 1
        while j >= start + 1 and a[j] > t:
            j -= 1
    a[start], a[i - 1] = a[i - 1], a[start]
    return i - 1
