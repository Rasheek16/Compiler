from classes import *

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token_index = 0
    
    def current_token(self):
        """Returns the current token without consuming it."""
        if self.current_token_index < len(self.tokens):
            return self.tokens[self.current_token_index]
        return None
    
    def take_token(self):
        """Consumes and returns the current token."""
        if self.current_token_index < len(self.tokens):
            token = self.tokens[self.current_token_index]
            self.current_token_index += 1
            return token
        return None
    
    def expect(self, expected):
        """Consumes the next token and checks its type."""
        actual = self.take_token()
        if actual is None or actual[0] != expected:
            raise RuntimeError(f'Expected token {expected} but got {actual}')
        return actual  # Return the actual token for further use
        
    def parse(self):
        """Parses the entire input and returns a Program node."""
        function = self.parse_function()
        return Program(function)
    
    def parse_function(self):
        """Parses a function definition."""
        self.expect('Int Keyword')  # Expect the "int" keyword
        identifier_token = self.expect("Identifier")  # Expect an identifier for the function name
        function_name = Identifier(identifier_token[1])  # Create an Identifier node
        
        self.expect('Open parenthesis')  # Expect the open parenthesis
        self.expect('Void Keyword')       # Expect the "void" keyword
        self.expect('Close parenthesis')  # Expect the close parenthesis
        self.expect("Open brace")         # Expect the open brace
        
        return_statement = self.parse_statement()  # Parse the function body
        self.expect("Close brace")  # Expect the close brace
        
        return Function(function_name, return_statement)
    
    def parse_statement(self):
        """Parses a return statement."""
        self.expect("Return Keyword")  # Expect the "return" keyword
        return_val = self.parse_expression()  # Parse the expression
        self.expect("Semicolon")  # Expect the semicolon after the return value
        return Return(return_val)
        
    def parse_expression(self):
        """Parses an expression and returns the corresponding AST node."""
        token = self.current_token()
        if token is None:
            raise RuntimeError('Unexpected end of input in expression')
        
        if token[0] == "Constant":  # Check for constant token
            self.take_token()  # Consume the constant token
            return Constant(int(token[1]))  # Create a Constant node
        
        if token[0] in ["Bitwise Complement", "Negation Operator"]:
            unary_operator = token[0]  # Store the unary operator
            self.take_token()  # Consume the unary operator token
            expr = self.parse_expression()  # Recursively parse the following expression
            return Unary(unary_operator, expr)  # Create a Unary node
        
        if token[0] == "Open Parenthesis":  # Handle expressions in parentheses
            self.take_token()  # Consume the '(' token
            expr = self.parse_expression()  # Parse the inner expression
            self.expect("Close Parenthesis")  # Expect the ')' token
            return expr  # Return the parsed expression
        
        raise RuntimeError(f'Unexpected token in expression: {token}')