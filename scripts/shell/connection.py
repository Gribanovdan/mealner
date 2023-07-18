


class Transmitter:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Transmitter, cls).__new__(cls)
        return cls.instance

    def __init__(self, my_shell):
        self.my_shell = my_shell



class Receiver:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Receiver, cls).__new__(cls)
        return cls.instance

    def __init__(self, my_shell):
        self.my_shell = my_shell
