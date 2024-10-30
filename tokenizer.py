def tokenize(code):
    tokens = []
    position = 0  # Position in the input code

    while position < len(code):
        # Trim whitespace from the start
        if code[position].isspace():
            position += 1  # Skip whitespace
            continue
        
        matched = False
        
        # Test each token specification against the input
        for token_name, token_regex in TOKEN_SPECIFICATIONS:
            regex = re.compile(token_regex)
            
            # Match at the current position
            match = regex.match(code, position)
            if match:
                value = match.group()
                tokens.append((token_name, value))
                position = match.end()  # Move the position after the match
                matched = True
                break
        
        if not matched:
            # If no tokens matched, raise an error
            raise RuntimeError(f'Unexpected character "{code[position]}" at position {position}')

    return tokens
