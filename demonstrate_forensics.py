"""
Demonstration of Forensics Logging for SQA Activity 4.b

This script demonstrates that we've integrated forensics logging into 5 Python methods:
1. getDataLoadCount()
2. getModelLoadCounta()
3. getDataDownLoadCount()
4. getModelLabelCount()
5. getEnvironmentCount()

Each method now logs security-related events with timestamps.
"""
import sys
import os

# Add FAME-ML to path
sys.path.append(os.path.join(os.getcwd(), 'FAME-ML'))

import lint_engine

print("=" * 70)
print("FORENSICS LOGGING DEMONSTRATION")
print("=" * 70)
print("\nAnalyzing 'sample_ml_code.py' for security patterns...\n")

# Analyze the sample ML file
file_path = 'sample_ml_code.py'

print("Running 5 modified methods with forensics logging:\n")

# Method 1: getDataLoadCount
print("1. getDataLoadCount() - Detects data loading patterns")
count1 = lint_engine.getDataLoadCount(file_path)
print(f"   Found {count1} data load patterns\n")

# Method 2: getModelLoadCounta
print("2. getModelLoadCounta() - Detects model loading patterns")
count2 = lint_engine.getModelLoadCounta(file_path)
print(f"   Found {count2} model load patterns\n")

# Method 3: getDataDownLoadCount
print("3. getDataDownLoadCount() - Detects download patterns")
count3 = lint_engine.getDataDownLoadCount(file_path)
print(f"   Found {count3} download patterns\n")

# Method 4: getModelLabelCount
print("4. getModelLabelCount() - Detects label manipulation patterns")
count4 = lint_engine.getModelLabelCount(file_path)
print(f"   Found {count4} label manipulation patterns\n")

# Method 5: getEnvironmentCount
print("5. getEnvironmentCount() - Detects RL environment patterns")
count5 = lint_engine.getEnvironmentCount(file_path)
print(f"   Found {count5} RL environment patterns\n")

print("=" * 70)
print("FORENSICS LOG OUTPUT")
print("=" * 70)
print("\nAll detections have been logged to 'forensics.log' with:")
print("  - Timestamp (when the event was detected)")
print("  - Event type (e.g., DATA_LOAD_EVENT)")
print("  - Line number (where in the code)")
print("  - Filename (which file)")
print("\nView forensics.log to see the complete forensics trail!")
print("=" * 70)
