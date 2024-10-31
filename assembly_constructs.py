class Node:
    pass


class Program(Node):
    def __init__(self, function_definition):
        self.function = function_definition


class Funtion(Node):
    def __init__(self, name, instruction):
        self.name = name
        self.instruction = instruction


class Mov(Node):
    def __init__(self, exp, register):
        self.exp = exp
        self.Register = register


class Imm:
    def __init__(self, int):
        self.ini = int

class Register:
    def __init__(self,name):
        self.name = name

class Ret():
    pass
