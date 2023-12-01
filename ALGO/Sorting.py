########################################################################################################################
#########################################################HEAP SORT######################################################
########################################################################################################################

def heapsort(lst):
    for j in range((len(lst) - 2) // 2, -1, -1):
        shiftDown(lst, j, len(lst))

    for end in range(len(lst) - 1, 0, -1):
        swap(lst, 0, end)
        shiftDown(lst, 0, end)


def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]


def shiftDown(lst, i, j):
    while True:
        l, r = i * 2 + 1, i * 2 + 2
        if max(l, r) < j:
            if lst[i] >= max(lst[l], lst[r]):
                break
            elif lst[l] > lst[r]:
                swap(lst, i, l)
                i = l
            else:
                swap(lst, i, r)
                i = r
        elif l < j:
            if lst[l] > lst[i]:
                swap(lst, i, l)
                i = l
            else:
                break
        elif r < j:
            if lst[r] > lst[i]:
                swap(lst, i, r)
                i = r
            else:
                break
        else:
            break
