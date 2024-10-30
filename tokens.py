TOKEN_SPECIFICATIONS = [
    ("Int Keyword", r"int\b"),           # Keyword: int
    ("Void Keyword", r"void\b"),         # Keyword: void
    ("Return Keyword", r"return\b"),     # Keyword: return
    ("Identifier", r"[a-zA-Z_]\w*"),     # Valid identifiers
    ("Constant", r"[0-9]+"),             # Integer constant
    ("Open parenthesis", r"\("),         # Open parenthesis
    ("Close parenthesis", r"\)"),        # Close parenthesis
    ("Open brace", r"\{"),               # Open brace
    ("Close brace", r"\}"),              # Close brace
    ("Semicolon", r";"),                 # Semicolon
]
