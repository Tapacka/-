l = {}
with open("1.txt") as one:
    data1 = one.readlines()
    l[len(data1)] = '1.txt'
with open("2.txt") as two:
    data2 = two.readlines()
    l[len(data2)] = '2.txt'
with open("3.txt") as three:
    data3 = three.readlines()
    l[len(data3)] = '3.txt'

min_str = l[min(l.keys())]


def open_file(file_name):
    with open(file_name) as mi:
        data = mi.read()

        with open('4.txt', 'w') as file:
            file.write(f'{file_name} \n{min(l.keys())} \n{data} \n')


open_file(min_str)

del l[min(l.keys())]
min_str = l[min(l.keys())]


def open_file(file_name):
    with open(file_name) as mi:
        data = mi.read()
        with open('4.txt', 'a') as file:
            file.write(f'{file_name} \n{min(l.keys())} \n{data} \n')


open_file(min_str)

del l[min(l.keys())]
min_str = l[min(l.keys())]


def open_file(file_name):
    with open(file_name) as mi:
        data = mi.read()
        with open('4.txt', 'a') as file:
            file.write(f'{file_name} \n{min(l.keys())} \n{data} \n')


open_file(min_str)