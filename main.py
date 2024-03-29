import time

from tools.memory import Memory
from tools.accumolator import Acc
from tools.flags import Ic, Output
from tools.reader import read_code
from tools.executer import execute

while 1:
    mem_size = input('Enter memory size (leave free to set 10000) :\n')
    try:
        mem_size = int(mem_size)
    except ValueError:
        if mem_size == '':
            mem_size = 10000
            break
        else:
            print("Invalid input! Try again.")

file_name = input('Enter file name :\n')
check_file = True
while check_file:
    try:
        file_path = f'./testcase/{file_name}'
        open(file_path, 'r')
        check_file = False
    except:
        print("File not found !")
        file_name = input('Enter file name :\n')

mem = Memory(mem_size)
acc = Acc()
ic = Ic()
output = Output()

read_code(mem, file_path)
start_time = time.time()
errors = execute(mem, ic, acc, output)
end_time = time.time()

run_time = str(end_time - start_time)[:5]

print(mem)
print(">> Ic :: ", ic)
print(">> Output :: ", output)
print(">> Acc :: ", acc)
if errors:
    for e in errors:
        print(e)
    print(f"The program finished after {run_time} seconds !")
else:
    print(f'The program run successfully in {run_time} seconds !')

"""
// Seyed Mohsen Razavi Zadegan 40030489
// github link : https://github.com/MohsenRazavi/samos ( private while upload time :) )
"""
