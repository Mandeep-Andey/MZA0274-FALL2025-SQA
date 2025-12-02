"""
Test to verify exception logging in py_parser.py
"""
import sys
import os

# Add FAME-ML to path
sys.path.append(os.path.join(os.getcwd(), 'FAME-ML'))

import py_parser

# Create a test file with syntax error
syntax_error_file = 'test_syntax_error.py'
with open(syntax_error_file, 'w') as f:
    f.write('def broken_function(\n')  # Incomplete function - will cause SyntaxError

print("Testing exception logging in py_parser...")

# This should trigger logging of SyntaxError
result = py_parser.getPythonParseObject(syntax_error_file)
print(f"getPythonParseObject returned: {type(result)}")

# This should also trigger logging
is_parsable = py_parser.checkIfParsablePython(syntax_error_file)
print(f"checkIfParsablePython returned: {is_parsable}")

# Clean up
os.remove(syntax_error_file)

print("\nCheck forensics.log for the PARSING_ERROR entries!")
