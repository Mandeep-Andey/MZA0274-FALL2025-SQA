# SQA Final Project Report

**Team Name:** MZA0274-FALL2025-SQA
**Members:** Mandeep Andey

## Fuzzing Strategy (Activity 4.a)

We implemented a fuzzer (`fuzz.py`) that targets the following 5 methods in `lint_engine.py`:
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

We replaced all `print()` statements with `logging.info()` to ensure proper forensics. We configured the logger to include timestamps as required.

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

We created a GitHub Actions workflow (`.github/workflows/sqa.yml`) that runs on every `push`.

**Workflow Steps:**
1. **Checkout Code:** Pulls the latest code from the repository.
2. **Set up Python:** Installs Python 3.x.
3. **Install Dependencies:** Installs `pandas`, `numpy`, and `gitpython`.
4. **Run Fuzzer:** Executes `python fuzz.py` to test the target methods with garbage inputs.
5. **Upload Artifact:** Uploads the generated `forensics.log` file for inspection.
