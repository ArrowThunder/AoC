import hashlib
import time
start_time = time.time()
start = 'yzbqklnj'
num = 0
while True:
    num += 1
    hasher = hashlib.md5()
    to_hash = start + str(num)
    hasher.update(to_hash.encode())
    output = hasher.hexdigest()
    check = True
    for i in range(6):
        if output[i] != '0':
            check = False
            break
    if check:
        break
    print(num)
print(num)

end_time = time.time()
print(end_time-start_time)