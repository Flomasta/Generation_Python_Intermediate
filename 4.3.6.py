def chucked(data, n):
    data = data.split()
    lst = []
    for i in range(0, len(data), n):
        lst.append(data[i:i + n])
    print(lst)


chucked(input(), int(input()))

#
# a b c d e f r g b
# 2
