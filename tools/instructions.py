def lda(address, memory, acc):
    """
    loads value from memory to acc

    :param address:
    :param memory:
    :param acc:
    :return: None
    """
    acc.value = memory.load(address)


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
    acc.value += value


def sub(value, acc):
    """
    subtracts value from acc
    :param value:
    :param acc:
    :return: None
    """
    acc.value -= value


def mpy(value, acc):
    """
    multiplies value to acc value
    :param value:
    :param acc:
    :return: None
    """
    acc.value *= value


def div(value, acc):
    """
    divides acc with value
    :param value:
    :param acc:
    :return: None
    """
    acc.value //= value


def hlt(address, ic):
    """
    sets ic value to address
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


def rwd(address, memory):
    """
    reads 11 chars and saves to the given address of memory
    :param address:
    :param memory:
    :return: None
    """
    pass
    memory.store(address)


def wwd(address, memory, output):
    """
    sets the values stored in address to output
    :param memory:
    :param address:
    :param output:
    :return: None
    """
    output.value = memory.load(address)