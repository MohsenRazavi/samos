def read_code(memory, file_address):
    with open(file_address) as code:
        codes = code.readlines()

    for code in codes:
        splited_code = code.split()
        memory.store(splited_code[0], splited_code[1])

    return codes