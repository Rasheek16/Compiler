from classes import *
# Instruction classes for assembly generation
class Instruction(Node):
    """Base class for all instructions."""
    pass

class Mov(Instruction):
    """Represents a 'mov' instruction in assembly."""
    def __init__(self, src, dst):
        self.src = src  # Source operand
        self.dst = dst  # Destination operand

class Ret(Instruction):
    """Represents a 'ret' instruction in assembly."""
    pass  # No operands needed for return instruction

class Imm:
    """Represents an immediate (constant) operand."""
    def __init__(self, value):
        self.value = value  # Integer constant

class Register:
    """Represents a register operand."""
    def __init__(self, name):
        self.name = name  # Name of the register (e.g., "EAX")

class AssemblyGenerator:
    def __init__(self):
        self.assembly_program = []

    def generate(self, ast):
        """Main entry point for generating assembly from the AST."""
        if isinstance(ast, Program):
            self.assembly_program = self.visit_program(ast)
        else:
            raise ValueError("Unknown AST node type")

    def visit_program(self, program):
        """Visit a program node."""
        function_definition = self.visit_function(program.function)
        return function_definition

    def visit_function(self, function):
        """Visit a function definition node."""
        name = function.name  # Assuming name is an Identifier instance
        instructions = self.visit_instructions(function.body)
        return {'name': name.value, 'instructions': instructions}

    def visit_instructions(self, instructions):
        """Visit a list of instructions."""
        assembly_instructions = []
        if isinstance(instructions, Return):
            assembly_instructions.extend(self.visit_return(instructions))
        return assembly_instructions

    def visit_return(self, return_node):
        """Visit a return statement."""
        instructions = []
        # Generate MOV instruction to move return value into EAX
        instructions.append(Mov(self.visit_expression(return_node.expression), Register("EAX")))
        instructions.append(Ret())
        return instructions

    def visit_expression(self, expr):
        """Visit an expression node."""
        if isinstance(expr, Constant):
            return Imm(expr.value)  # Create an immediate operand
        else:
            raise ValueError("Unknown expression type")

    def get_assembly(self):
        """Return the generated assembly program."""
        return self.assembly_program