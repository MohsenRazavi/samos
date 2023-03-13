class Memory:
    memory = {str(i): 11 * '0' for i in range(0, 10000)}

    def load(self, address):
        return int(self.memory[str(address)])

    def store(self, address, value):
        self.memory[str(address)] = str(value)

    def clear(self):
        self.memory = {str(i): 11 * '0' for i in range(0, 10000)}
