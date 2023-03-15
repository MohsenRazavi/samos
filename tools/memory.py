class Memory:
    memory = {}

    def __init__(self, length):
        self.memory = {str(i).zfill(4): 11 * '0' for i in range(0, length)}

    def __str__(self):
        res = ''
        for k in range(0, len(self.memory), 4):
            for j in range(4):
                try:
                    res += f"<< {str(k + j).zfill(4)} :: {self.memory[str(k + j).zfill(4)]}>>\t"
                except:
                    pass
            res += '\n'
        return res

    def load(self, address):
        return int(self.memory[str(address)])

    def store(self, address, value):
        self.memory[str(address)] = str(value).zfill(11)

    def clear(self):
        self.memory = {str(i): 11 * '0' for i in range(0, 10000)}

    def print_n_lines(self, n):
        for i in range(n):
            print(f'<< {str(i).zfill(4)} :: {self.memory[str(i).zfill(4)]} >>')
