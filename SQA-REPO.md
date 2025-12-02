# SQA Final Project Report

**Team Name:** MZA0274-FALL2025-SQA
**Members:** Mandeep Andey

## Fuzzing Strategy (Activity 4.a)

Implemented a fuzzer (`fuzz.py`) that targets the following 5 methods in `lint_engine.py`:
1. `getDataLoadCount`
2. `getModelLoadCounta`
3. `getDataDownLoadCount`
4. `getModelLabelCount`
5. `getEnvironmentCount`

**Garbage Inputs Used:**
- **Random Binary Garbage:** A file containing random bytes.
- **Empty File:** A file with 0 bytes.
- **Non-Existent Path:** A string path to a file that does not exist.
- **Incomplete Code:** A python file containing only `import ` (syntax error).

The fuzzer feeds these inputs to the target methods and catches any unhandled exceptions ("CRASH FOUND") or reports if the method handled it gracefully ("PASSED").

## Forensics & Logging (Activity 4.b)

Replaced all `print()` statements with `logging.info()` to ensure proper forensics. Configured the logger to include timestamps as required.

**Logging Configuration Snippet:**
```python
import logging

logging.basicConfig(
    filename='forensics.log', 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)
```

## Continuous Integration (Activity 4.c)

Created a GitHub Actions workflow (`.github/workflows/sqa.yml`) that runs on every `push`.

**Workflow Steps:**
1. **Checkout Code:** Pulls the latest code from the repository.
2. **Set up Python:** Installs Python 3.x.
3. **Install Dependencies:** Installs `pandas`, `numpy`, and `gitpython`.
4. **Run Fuzzer:** Executes `python fuzz.py` to test the target methods with garbage inputs.
5. **Upload Artifact:** Uploads the generated `forensics.log` file for inspection.

## Fuzzing Findings
The fuzzer discovered the following unhandled exceptions (crashes) in the target methods:

1.  **`UnicodeDecodeError`**:
    *   **Cause:** The methods attempt to read files using the default text encoding (UTF-8) without handling binary files.
    *   **Trigger:** Feeding a file containing random binary data (`fuzz_binary.py`).
    *   **Impact:** The application crashes when encountering non-text files.

2.  **`FileNotFoundError`**:
    *   **Cause:** The methods do not check if a file exists before attempting to open or parse it.
    *   **Trigger:** Feeding a path to a non-existent file (`non_existent_file_path_12345.py`).
    *   **Impact:** The application crashes when a specified file path is invalid.

## Lessons Learned
1.  **Input Validation is Critical:** The crashes found by the fuzzer highlight the importance of validating inputs (e.g., checking file existence, verifying file type) before processing them.
2.  **Forensics Requires Structure:** Replacing ad-hoc `print` statements with structured `logging` makes it significantly easier to trace execution flow and debug issues, especially with timestamps.
3.  **Automation Saves Time:** Setting up GitHub Actions for CI ensures that the tests (fuzzing) run automatically on every change, preventing regressions and ensuring that the code remains robust.
