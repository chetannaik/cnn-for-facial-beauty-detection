import shutil

# lines = [line.strip().split(' ')[0] for line in open('rating.txt')]

train = [line.strip().split(' ')[0] for line in open('train.txt')]
test = [line.strip().split(' ')[0] for line in open('test.txt')]


for i in train:
	file_src = '/Users/chetannaik/Downloads/mixture/' + i
	file_dest = '/Users/chetannaik/Downloads/train/' + i
 	shutil.copy2(file_src, file_dest)

for i in test:
	file_src = '/Users/chetannaik/Downloads/mixture/' + i
	file_dest = '/Users/chetannaik/Downloads/test/' + i
 	shutil.copy2(file_src, file_dest)