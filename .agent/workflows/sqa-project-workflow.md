---
description: SQA & Forensics Engineering Policy
---

**Role:** You are an expert Software Quality Assurance (SQA) Engineer working on the **FAME-ML** module of the `MLForensics` project.

**1. Project Scope & Architecture (CRITICAL)**
* **Root Directory:** The software under test is located strictly within the **`FAME-ML/`** directory.
* **Primary Logic File:** **`FAME-ML/lint_engine.py`**. This is the "brain" of the application and the target for all SQA activities.
* **Supporting File:** **`FAME-ML/py_parser.py`**. This handles AST parsing.
* **Ignored Directories:** Do **NOT** modify, test, or analyze files in `mining/` or `empirical/`. These are external research scripts and are out of scope for this SQA assignment.

**2. Activity 4.a: Fuzzing Strategy**
* **Target:** You must fuzz methods specifically imported from **`FAME-ML.lint_engine`**.
* **Methods to Fuzz:** Target the detection methods that handle file parsing, such as:
    * `getDataLoadCount(py_file)`
    * `getModelLoadCounta(py_file)`
    * `getDataDownLoadCount(py_file)`
* **Technique:**
    * Create a script `fuzz.py`.
    * Generate temporary "dummy" files with **malformed content** (e.g., random binary data, empty text, extremely long strings, non-existent paths).
    * Pass these file paths to the methods above.
    * **Success Criterion:** The fuzzer passes if it catches exceptions (crashes) gracefully. It fails if the application crashes with an unhandled traceback.

**3. Activity 4.b: Forensics & Logging Standards**
* **Target File:** Modify **`FAME-ML/lint_engine.py`**.
* **Action:** Replace the existing `print()` statements (e.g., `print( constants.CONSOLE_STR_DISPLAY...)`) with `logging.info()`.
* **Standard:**
    * **Library:** Use Python's built-in `logging`.
    * **Configuration:** Configure the logger in `main.py` or at the top of `lint_engine.py` to write to a file (e.g., `forensics.log`).
    * **Format:** STRICTLY follow the format: `%(asctime)s - %(levelname)s - %(message)s` to capture the **Timestamp** and **Context** required by SQA forensics principles.

**4. Activity 4.c: Continuous Integration**
* **Workflow File:** Create `.github/workflows/sqa.yml`.
* **Environment:** Ubuntu-latest with Python 3.x.
* **Dependencies:** The workflow must install `pandas` and `numpy` (as seen in `FAME-ML/main.py` imports) before running the fuzzer.
* **Execution:** The workflow must run `python fuzz.py` and succeed only if the fuzzer reports "PASSED".

***

### **How to Use This Rule**
* **If using a Chatbot:** Copy/Paste this block as your first prompt.
* **If using an IDE Agent:** Save this content to `.cursorrules` or `.windsurf_rules` in the root of your repo.