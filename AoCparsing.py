import sys
increase = 0
with open('input.txt') as file:
    a = file.readline()
    for b in file:
        if int(b) > int(a):
            increase += 1
        a = b
print(increase)