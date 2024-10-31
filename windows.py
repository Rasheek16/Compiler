#!/usr/bin/env python3
from tokenizer import tokenize
from parser import Parser
from assembly_generation import AssemblyGenerator, Mov,Ret


if __name__ == "__main__":
    code = """
    int main(void) {
        return 5;
    }
    """

    try:
        # Tokenize the code
        tokens = tokenize(code)
        print(tokens)

        # Parse the tokens
        parser = Parser(tokens)
        program = parser.parse()
        
        print(program)
        # Generate assembly
        generator = AssemblyGenerator()
        generator.generate(program)
        assembly_output = generator.get_assembly()
        
        # Print generated assembly code to console
        print("\nGenerated Assembly Code:")
        print(assembly_output)

        # Write the assembly output to a file
        with open('output.s', 'w') as f:
            f.write(assembly_output)
        print("\nAssembly code has been written to output.s")

    except RuntimeError as e:
        print(f"Error: {e}")