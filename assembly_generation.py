from classes import *  # Ensure all necessary classes are imported

class AssemblyGenerator:
    def __init__(self):
        self.assembly_output = []

    def generate(self, ast):
        """Main entry point for generating assembly from the AST."""
        if isinstance(ast, Program):
            self.visit_program(ast)
        else:
            raise ValueError("Unknown AST node type")
    
    def visit_program(self, program):
        """Visit a program node."""
        self.visit_function(program.function)
        self.assembly_output.append(".section .note.CNU-stack,\"\",@progbits")

    def visit_function(self, function):
        """Visit a function definition node."""
        self.assembly_output.append(f"globl {function.name.value}")
        self.assembly_output.append(f"{function.name.value}:")
        instructions = self.visit_instructions(function.body)
        self.assembly_output.extend(instructions)

    def visit_instructions(self, instructions):
        """Visit a list of instructions."""
        assembly_instructions = []
        if isinstance(instructions, Return):
            assembly_instructions.extend(self.visit_return(instructions))
        return assembly_instructions

    def visit_return(self, return_node):
        """Visit a return statement."""
        # Generate the MOV instruction to move the return value into EAX
        mov_instruction = Mov(self.visit_expression(return_node.expression), Register("EAX"))

        # Return both instructions as a list of strings
        return [str(mov_instruction), str(Ret())]

    def visit_expression(self, expr):
        """Visit an expression node."""
        if isinstance(expr, Constant):
            return Imm(expr.value)  # Create an immediate operand
        
        raise ValueError("Unknown expression type")

    def get_assembly(self):
        """Return the generated assembly program."""
        return "\n".join(self.assembly_output)