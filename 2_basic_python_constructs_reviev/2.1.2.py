w, h = (float(input()) for i in '__')

if h > 0:
    res = w / h ** 2
    print('Оптимальная масса' if 18.5 <= res <= 25 else "Недостаточная масса" if res < 18.5 else "Избыточная масса")
