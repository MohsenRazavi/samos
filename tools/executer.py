from instructions import *


def execute(memory, ic, acc, output):
    command = ''
    while command != 'HLT':
        code = memory.memory[str(ic.value).zfill(4)]
        command = code[1:4]
        param = code[7:]

        if command == 'LDA':
            lda(param, memory, acc)
        elif command == 'STO':
            sto(param, memory, acc)
        elif command == 'ADD':
            add(param, acc)
        elif command == 'SUB':
            sub(param, acc)
        elif command == 'MPY':
            mpy(param, acc)
        elif command == 'DIV':
            div(param, acc)
        elif command == 'BRU':
            bru(param, ic)
            continue
        elif command == 'BMI':
            bmi(param, ic, acc)
            continue
        elif command == 'RWD':
            rwd(param, memory, ic.value)
        elif command == 'WWD':
            wwd(param, memory, output)

        ic_val = int(ic.value) + 1
        ic.value = str(ic_val)

