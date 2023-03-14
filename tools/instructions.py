import re


def lda(address, memory, acc):
    """
    loads value from memory to acc

    :param address:
    :param memory:
    :param acc:
    :return: None
    """
    acc.value += memory.load(address)


def sto(address, memory, acc):
    """
    stores value from acc to memory
    :param address:
    :param memory:
    :param acc:
    :return: None
    """
    memory.store(address, acc.value)


def add(value, acc):
    """
    adds value to acc
    :param value:
    :param acc:
    :return: None
    """
    acc.value += int(value)


def sub(value, acc):
    """
    subtracts value from acc
    :param value:
    :param acc:
    :return: None
    """
    acc.value -= int(value)


def mpy(value, acc):
    """
    multiplies value to acc value
    :param value:
    :param acc:
    :return: None
    """
    acc.value *= int(value)


def div(value, acc):
    """
    divides acc with value
    :param value:
    :param acc:
    :return: None
    """
    acc.value //= int(value)


def hlt(address, ic):
    """
    sets ic value to address. end of program.
    :param address:
    :param ic:
    :return: None
    """
    ic.value = address


def bru(address, ic):
    """
    branches to address ( sets ic value to address )
    :param address:
    :param ic:
    :return: None
    """
    ic.value = address


def bmi(address, ic, acc):
    if acc.value < 0:
        ic.value = address


def rwd(address, memory, line_number):
    """
    reads 11 chars and saves to the given address of memory
    :param address:
    :param memory:
    :return: None
    """
    while 1:
        user_input = input(f"Enter the instruction (called from line {line_number}, saves at {address}):\n")
        pattern = re.compile("^[+][A-Z0]{3}0{3}[0-9]{4}$")
        if not pattern.match(user_input):
            print("Invalid instruction! Try again")
            user_input = input(f"Enter the instruction (called from line {line_number}, saves at {address}):\n")
        else:
            break
    if memory.memory[address] != 11*'0':
        print("Warning :: destination address is not free. Are you sure (y/n)?")
        user_answer = input()
        while user_answer not in ('y', 'n'):
            user_answer = input('Invalid input! Try again.\n')
        if user_answer == 'y':
            memory.store(address, user_input)


def wwd(address, memory, output):
    """
    sets the values stored in address to output
    :param memory:
    :param address:
    :param output:
    :return: None
    """
    output.value = memory.load(address)
