"""
Test script to demonstrate forensics logging with actual security patterns.
"""
import sys
import os

# Add FAME-ML to path
sys.path.append(os.path.join(os.getcwd(), 'FAME-ML'))

import lint_engine

print("Testing forensics logging with sample ML code...")
print("=" * 60)

# Analyze the sample file that contains security patterns
file_path = 'sample_ml_code.py'

if os.path.exists(file_path):
    print(f"\nAnalyzing: {file_path}\n")
    
    # Run detection methods
    data_load = lint_engine.getDataLoadCount(file_path)
    model_load = lint_engine.getModelLoadCounta(file_path)
    
    print(f"Results:")
    print(f"  - Data load patterns found: {data_load}")
    print(f"  - Model load patterns found: {model_load}")
    
    print("\n" + "=" * 60)
    print("Forensics log entries have been written to 'forensics.log'")
    print("Each detection includes timestamp and line number.")
else:
    print(f"Error: {file_path} not found")
