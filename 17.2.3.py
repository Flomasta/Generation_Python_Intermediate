with open('lines (1).txt', 'r', encoding='utf-8') as file:
    data = file.readlines()
    ld = max([len(i) for i in data])
    print(*[i.strip() for i in data if len(i) == ld][::-1], sep='\n')
