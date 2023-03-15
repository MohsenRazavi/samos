"""
Objects witch just have a value
"""


class Flag:
    value = 0

    def __str__(self):
        return str(self.value)


class Ic(Flag):
    pass


class Output(Flag):
    pass
