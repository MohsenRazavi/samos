class Memory:
    memory = {str(i).zfill(4): 11 * '0' for i in range(0, 10000)}

    def __str__(self):
        res = ''
        for k, v in self.memory.items():
            res += f'<< {k} :: {v} >>\t'
        return res

    def load(self, address):
        return int(self.memory[str(address)])

    def store(self, address, value):
        self.memory[str(address)] = str(value)

    def clear(self):
        self.memory = {str(i): 11 * '0' for i in range(0, 10000)}

    def print_n_lines(self, n):
        for i in range(n):
            print(f'<< {str(i).zfill(4)} :: {self.memory[str(i).zfill(4)]} >>')
