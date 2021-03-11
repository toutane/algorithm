def convert(n, b):
    r = n

    arr = []
    while r != 0:
        arr.append(r % base)
        r = r // b

    ints = list(arr[::-1])
    string_ints = [str(int) for int in ints]
    result = ''.join(string_ints)

    print(result)


num = int(input('Nombre: '))
base = int(input('Convertir en base: '))

convert(num, base)
