from tools.instructions import *


def execute(memory, ic, acc, output):
    errors = []
    ic_in_instruction_range = False
    while 1:
        code = memory.memory[str(ic.value).zfill(4)]
        if ic_in_instruction_range:
            pattern = re.compile("^[+][A-Z]{3}0{3}[0-9]{4}$")
        else:
            pattern = re.compile("^[+][A-Z0]{3}0{3}[0-9]{4}$")

        if pattern.match(code):
            command = code[1:4]
            param = code[7:]

            if command == 'LDA':
                lda(param, memory, acc)
                ic_in_instruction_range = True
            elif command == 'STO':
                sto(param, memory, acc)
                ic_in_instruction_range = True
            elif command == 'ADD':
                add(param, memory, acc)
                ic_in_instruction_range = True
            elif command == 'SUB':
                sub(param, memory, acc)
                ic_in_instruction_range = True
            elif command == 'MPY':
                mpy(param, memory, acc)
                ic_in_instruction_range = True
            elif command == 'DIV':
                div(param, memory, acc)
                ic_in_instruction_range = True
            elif command == 'BRU':
                bru(param, ic)
                ic_in_instruction_range = True
                continue
            elif command == 'BMI':
                last_ic_val = ic.value
                bmi(param, ic, acc)
                if ic.value == last_ic_val:
                    ic_val = int(ic.value) + 1
                    ic.value = str(ic_val)
                continue
            elif command == 'RWD':
                rwd(param, memory, ic.value)
            elif command == 'WWD':
                wwd(param, memory, output)
            elif command == 'HLT':
                hlt(param, ic)
                ic_in_instruction_range = False
                break

            else:
                error_index = str(ic.value).zfill(4)
                errors.append(f"Invalid instruction in line {error_index} ! :: {memory.memory[error_index]}")
                break

            ic_val = int(ic.value) + 1
            ic.value = str(ic_val).zfill(4)

        else:
            error_index = str(ic.value).zfill(4)
            errors.append(f"Instruction doesn't match with pattern +XXX0009999 {error_index} ! :: {memory.memory[error_index]}")
            break
    return errors
