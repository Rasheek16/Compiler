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
        
class Return():
    def __init__(self, expression):
        self.expression = expression

class Program(Node):
    def __init__(self, function):
        self.function = function
        
class Unary(Node):
    def __init__(self, operator, expression):
        self.operator = operator  # The unary operator (e.g., "Complement" or "Negate")
        self.expression = expression  # The expression to which the operator is applied

    

class Instruction(Node):
    pass

class Mov(Instruction):
    """Represents a 'mov' instruction in assembly."""
    def __init__(self, src, dst):
        self.src = src  # Source operand
        self.dst = dst  # Destination operand

    def __str__(self):
        return f"\tmov {self.src}, {self.dst}"  # String representation of the MOV instruction

class Ret(Instruction):
    """Represents a 'ret' instruction in assembly."""
    def __str__(self):
        return "\tret"  # String representation of the RET instruction

class Imm:
    """Represents an immediate (constant) operand."""
    def __init__(self, value):
        self.value = value  # Integer constant

    def __str__(self):
        return f"${self.value}"  # String representation of the immediate value

class Register:
    """Represents a register operand."""
    def __init__(self, name):
        self.name = name  # Name of the register (e.g., "EAX")

    def __str__(self):
        return self.name  # String representation of the register name
