import sys
import os
import random
import string
import logging

# Add FAME-ML to path so we can import lint_engine
sys.path.append(os.path.join(os.getcwd(), 'FAME-ML'))

try:
    import lint_engine
except ImportError:
    print("Error: Could not import lint_engine. Make sure FAME-ML directory is in the path.")
    sys.exit(1)

# Configure logging for the fuzzer itself (optional, but good for debugging)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_random_string(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def create_bad_files():
    files = []
    
    # Case 1: Random binary garbage
    f1 = "fuzz_binary.py"
    with open(f1, "wb") as f:
        f.write(os.urandom(1024))
    files.append(f1)
    
    # Case 2: Empty text file
    f2 = "fuzz_empty.py"
    with open(f2, "w") as f:
        pass
    files.append(f2)
    
    # Case 3: Non-existent path
    files.append("non_existent_file_path_12345.py")
    
    # Case 4: Incomplete code
    f4 = "fuzz_incomplete.py"
    with open(f4, "w") as f:
        f.write("import ")
    files.append(f4)
    
    return files

def cleanup_files(files):
    for f in files:
        if os.path.exists(f):
            os.remove(f)

def main():
    target_methods = [
        lint_engine.getDataLoadCount,
        lint_engine.getModelLoadCounta,
        lint_engine.getDataDownLoadCount,
        lint_engine.getModelLabelCount,
        lint_engine.getEnvironmentCount
    ]
    
    bad_files = create_bad_files()
    
    all_passed = True
    
    print("Starting Fuzzing...")
    
    for method in target_methods:
        print(f"\nTesting method: {method.__name__}")
        for file_path in bad_files:
            print(f"  Input: {file_path}")
            try:
                method(file_path)
                print("    PASSED: Handled gracefully (or no error triggered)")
            except Exception as e:
                # We expect the code might crash if it doesn't handle exceptions.
                # The requirement says: "If the method crashes (unhandled exception), print 'CRASH FOUND'"
                # However, since we are calling it inside a try-except block here in the fuzzer, 
                # we are technically "handling" it here. But the *method itself* didn't handle it.
                # So this counts as a crash found in the target method.
                print(f"    CRASH FOUND: {type(e).__name__}: {e}")
                all_passed = False
                
    cleanup_files(bad_files)
    
    if all_passed:
        print("\nFuzzing Completed: All tests passed (gracefully handled).")
        sys.exit(0)
    else:
        print("\nFuzzing Completed: Crashes found.")
        # The requirement says "exit with status code 0 if all tests pass (or handled errors), and status code 1 if the script itself crashes."
        # If we found crashes in the target methods, does that mean the script crashed?
        # Usually a fuzzer finding a crash is a "success" for the fuzzer but a "failure" for the code.
        # The instructions say: "Ensure fuzz.py exits with status code 0 if all tests pass (or handled errors), and status code 1 if the script itself crashes."
        # This is slightly ambiguous. If the target method crashes, we caught it. So the script *itself* didn't crash.
        # So I will exit with 0, but report the crashes.
        # Wait, if I want to fail the CI if crashes are found, I should probably exit 1?
        # "If the method crashes (unhandled exception), print 'CRASH FOUND'."
        # "Ensure fuzz.py exits with status code 0 if all tests pass (or handled errors), and status code 1 if the script itself crashes."
        # This implies if the fuzzer runs to completion, it's exit code 0.
        sys.exit(0)

if __name__ == "__main__":
    main()
