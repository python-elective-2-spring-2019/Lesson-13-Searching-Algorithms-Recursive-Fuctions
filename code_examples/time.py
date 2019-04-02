# How to measure the execution time of a Python script?
import time
import sys

start = time.time()

for i in range(1, int(sys.argv[1])):
    print(i, end='')

end = time.time()
print()
print('========')
print('The scripts execusion time was', end - start, 'seconds')
