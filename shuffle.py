import os
import sys
from random import shuffle

arg = sys.argv[1]

cnt = os.listdir(arg)

random_number = [i for i in xrange(len(cnt))]
shuffle(random_number)

idx = 0

for filename in os.listdir(arg):
	new_str = os.path.realpath(arg)+'/'+str(random_number[idx])+'-'+filename
	os.rename(os.path.realpath(arg)+'/'+filename, os.path.realpath(arg)+'/'+str(random_number[idx]+1)+'-'+filename)
	idx+=1
