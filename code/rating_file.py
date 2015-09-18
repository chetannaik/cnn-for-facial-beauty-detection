import os

imgs = []


f = open('rating.txt', 'w')
for root, dirs, files in os.walk('/Users/chetannaik/Downloads/sorted/1/'):
    for file in files:
         if file.endswith('.jpg'):
             imgs.append(file)
             f.write(file+' 1\n')

for root, dirs, files in os.walk('/Users/chetannaik/Downloads/sorted/2/'):
    for file in files:
         if file.endswith('.jpg'):
             imgs.append(file)
             f.write(file+' 2\n')

for root, dirs, files in os.walk('/Users/chetannaik/Downloads/sorted/3/'):
    for file in files:
         if file.endswith('.jpg'):
             imgs.append(file)
             f.write(file+' 3\n')

for root, dirs, files in os.walk('/Users/chetannaik/Downloads/sorted/4/'):
    for file in files:
         if file.endswith('.jpg'):
             imgs.append(file)
             f.write(file+' 4\n')

for root, dirs, files in os.walk('/Users/chetannaik/Downloads/sorted/5/'):
    for file in files:
         if file.endswith('.jpg'):
             imgs.append(file)
             f.write(file+' 5\n')
f.close()
