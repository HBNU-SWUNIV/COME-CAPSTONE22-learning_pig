import os
import shutil

file_path = '/home/dfx/Desktop/taewon/1/images/'

a = os.listdir(file_path)
print(a)

b = []

for i in a:
    i = i.replace('.txt', '').replace('.jpg', '').replace('.png', '')
    b.append(i)

print(b)

for i in range(len(b)):
    cnt = b.count(b[i])
    if cnt == 2:
        one = file_path + a[i]
        print(one)
        shutil.copy(one, '/home/dfx/Desktop/taewon/2/'+a[i])