---
trigger: always_on
---

### **Workspace Rule: SQA & Forensics Engineering Policy**

**Role:** You are an SQA Engineer working on the `MLForensics` project. Your code must adhere to strict software quality assurance standards derived from the course lecture notes.

**1. Forensics & Logging Standards (Strict Adherence Required)**
* **No Print Statements:** Never use `print()` for application logs or debugging. [cite_start]`print()` is essentially invisible in a forensic investigation[cite: 2419].
* **Mandatory Logging Configuration:** You must strictly use the Python `logging` library.
* **Log Format:** Every log entry **MUST** include a timestamp and context. [cite_start]As per `SQA-3.pdf`, logs help answer "when" and "what"[cite: 2414].
    * *Required Format:* `%(asctime)s - %(levelname)s - %(message)s`
* **What to Log:**
    * **Exceptions/Faults:** Log all `try-except` blocks. [cite_start]Do not just pass; log the specific error[cite: 2386].
    * [cite_start]**Startups/Shutdowns:** Log when analysis begins and ends for a file[cite: 2387].
    * [cite_start]**Security Events:** Log patterns detected that imply security risks (e.g., `pickle.load` detection)[cite: 2370].

**2. Fuzzing Strategy (Activity 4.a)**
* **Definition:** Do not write standard "unit tests" that check for correct values. [cite_start]Your fuzzing scripts must feed **malformed, random, or anomalous input data** to the target methods[cite: 2754].
* [cite_start]**Goal:** The goal is to cause a **crash** (unhandled exception) or hang, not to verify business logic[cite: 2764].
* **Target:** Focus fuzzing efforts on `lint_engine.py` methods that handle file I/O or parsing (e.g., `getDataLoadCount`), as these are most susceptible to malformed input.
* **Mechanism:**
    1.  Generate garbage data (e.g., empty files, binary noise, massive strings).
    2.  Execute the target function.
    3.  [cite_start]Catch and report "CRASH" (unhandled exception) vs "PASS" (handled exception)[cite: 2802].

**3. Continuous Integration (Activity 4.c)**
* **Automation:** The fuzzing script (`fuzz.py`) must be executable in a headless environment (GitHub Actions).
* **Workflow:** The `.github/workflows/sqa.yml` must install all dependencies found in `FAME-ML` (e.g., `pandas`, `numpy`) before running tests.

**4. Project Context**
* **Repo Name Format:** `TEAMNAME-FALL2025-SQA`.
* **Target Codebase:** The core logic is located in `FAME-ML/lint_engine.py` and `FAME-ML/py_parser.py`. Modifications for logging should primarily happen here.