class OverflowWarning(Exception):
    pass


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
        # checking overflow
        overflow = 0
        if new_value >= int(10 * '9') or new_value <= -int(10 * '9'):
            self.value = str(int(self) - int(10 * '9')).zfill(11)
            overflow = 1
        else:
            self.value = str(new_value).zfill(11)

        if new_value > 0:
            self.value = '+' + self.value[1:]
        elif new_value < 0:
            self.value = '-' + self.value[1:]
        else:
            self.value = '0' + self.value[1:]

        if overflow:
            raise OverflowWarning
