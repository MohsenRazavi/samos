from tools.memory import Memory
from tools.accumolator import Acc
from tools.flags import Ic, Output
from tools.reader import read_code
from tools.executer import execute


mem_size = int(input('Enter memory size :\n'))

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
execute(mem, ic, acc, output)

print(mem)
print(">> Ic :: ", ic)
print(">> Output :: ", output)
print(">> Acc :: ", acc)


