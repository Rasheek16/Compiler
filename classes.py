class Node:
    pass

class Constant(Node):
    def __init__(self, value):
        self.value = value
        
class Identifier(Node):
    def __init__(self, name):
        self.value = name
        
class Function(Node):
    def __init__(self, name, body):
        self.name = name 
        self.body = body
        
class Return(Node):
    def __init__(self, expression):
        self.expression = expression

class Program(Node):
    def __init__(self, function):
        self.function = function
    
