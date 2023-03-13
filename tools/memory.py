class Memory:
    memory = {str(i): 11 * '0' for i in range(0, 10000)}

    def load(self, index):
        return self.memory[str(index)]

    def store(self, index, value):
        self.memory[str(index)] = str(value)

    def clear(self):
        self.memory = {str(i): 11 * '0' for i in range(0, 10000)}