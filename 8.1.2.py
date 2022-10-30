n, m, k, x, y, z, t, a = (int(input()) for _ in range(8))

one_and_two = n + m - (x + t)
two_and_three = m + k - (y + t)
three_and_one = k + n - (z + t)

read_two_books = one_and_two + two_and_three + three_and_one

book_n = n - one_and_two - three_and_one - t
book_m = m - one_and_two - two_and_three - t
book_k = k - three_and_one - two_and_three - t

read_one_book = book_n + book_m + book_k

read_no_book = a - (read_one_book + read_two_books + t)

print(read_two_books, read_one_book, read_no_book, sep='\n')
# 19 n
# 18 m
# 22 k
# 32 x
# 33 y
# 35 z
# 2 t
# 50 a
