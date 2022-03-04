#cython: language_level=3

cimport cython

@cython.boundscheck(False)  # Deactivate bounds checking
@cython.wraparound(False)   # Deactivate negative indexing.
def rgbtobgr(arr: cython.char[:]) -> cython.char[:]:
    l: cython.int
    i: cython.int
    c: cython.int
    t: cython.char

    l = len(arr)

    for c in range(l >> 4):
        i = c << 4
        
        t = arr[i]
        arr[i] = arr[i + 2]
        arr[i + 2] = t

        t = arr[i + 4]
        arr[i + 4] = arr[i + 6]
        arr[i + 6] = t

        t = arr[i + 8]
        arr[i + 8] = arr[i + 10]
        arr[i + 10] = t

        t = arr[i + 12]
        arr[i + 12] = arr[i + 14]
        arr[i + 14] = t

    return arr
