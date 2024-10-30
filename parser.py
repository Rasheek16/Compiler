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
    
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token_index = 0
    
    def current_token(self):
        if self.current_token_index < len(self.tokens):
            return self.tokens[self.current_token_index]
        return None
    
    def take_token(self):
        if self.current_token_index < len(self.tokens):
            token = self.tokens[self.current_token_index]
            self.current_token_index += 1
            return token
        return None
    
    def expect(self, expected):
        actual = self.take_token()
        if actual is None or actual[0] != expected:
            raise RuntimeError(f'Expected token {expected} but got {actual}')
        return actual  # Return the actual token for further use
        
    def parse(self):
        function = self.parse_function()
        return Program(function)
    
    def parse_function(self):
        self.expect('Int Keyword')  # Expect the "int" keyword
        identifier_token = self.expect("Identifier")  # Expect an identifier for the function name
        function_name = Identifier(identifier_token[1])  # Safe access here
        
        self.expect('Open parenthesis')  # Expect the open parenthesis
        self.expect('Void Keyword')       # Expect the "void" keyword
        self.expect('Close parenthesis')  # Expect the close parenthesis
        self.expect("Open brace")         # Expect the open brace
        
        return_statement = self.parse_statement()  # Parse the function body
        self.expect("Close brace")  # Expect the close brace
        
        return Function(function_name, return_statement)
    
    def parse_statement(self):
        self.expect("Return Keyword")  # Expect the "return" keyword
        return_val = self.parse_expression()  # Parse the expression (should be Constant)
        self.expect("Semicolon")  # Expect the semicolon after the return value
        return Return(return_val)
        
    def parse_expression(self):
        token = self.current_token()
        if token is None:
            raise RuntimeError('Unexpected end of input in expression')
        
        if token[0] == "Constant":  # Check for constant token
            self.take_token()
            return Constant(int(token[1]))  # Convert string to integer
        
        raise RuntimeError(f'Unexpected token in expression: {token}')
