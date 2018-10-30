def add(*x):
    s = 0
    if len(x) > 1:
        for num in x:
            s += num
        print(s)

add(3,4,5)
add(3,7,4,9)
add(1,7)
