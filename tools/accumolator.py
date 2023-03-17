class Acc:
    value = 11 * '0'

    def __str__(self):
        return str(self.value)

    def __int__(self):
        if self.value[0] == '-':
            return -int(self.value[1:])
        return int(self.value[1:])

    def clear(self):
        self.value = 0

    def set(self, new_value):
        self.value = str(new_value).zfill(11)
        if new_value > 0:
            self.value = '+' + self.value[1:]
        elif new_value < 0:
            self.value = '-' + self.value[1:]
        else:
            self.value = '0' + self.value[1:]

