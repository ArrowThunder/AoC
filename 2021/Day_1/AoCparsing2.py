increase = 0
with open('input.txt') as file:
    a = file.readline()
    b = file.readline()
    c = file.readline()
    for d in file:
        if int(d) > int(a):
            increase += 1
        a = b
        b = c
        c = d
print(increase)