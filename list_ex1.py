def even_num(l):
    enum = []
    for n in l:
        if n % 2 == 0:
            enum.append(n)
    return enum
print(even_num([1, 2, 3, 4, 5, 6, 7, 8, 9]))

def odd_num(l):
    onum = []
    for n in l:
        if n % 2 != 0:
            onum.append(n)
    return onum
print(odd_num([1, 2, 3, 4, 5, 6, 7, 8, 9]))

def pos_num(l):
    pnum = []
    for n in l:
        if n > 0:
            pnum.append(n)
    return pnum
print(pos_num([1, -2, 3, 4, -5, -6, 7, 8, 9]))
