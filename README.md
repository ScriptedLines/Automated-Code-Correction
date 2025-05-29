# Automated Python Bug Fixing Framework using LLMs

This project automates the process of identifying and fixing bugs in Python programs using large language models (LLMs). The system reads buggy Python code, classifies and corrects the errors, tests the fixed code, and iterates the process until all test cases pass.

---

## Architecture Overview

The framework consists of three specialized agents, each with a distinct role:

### 1. Correction Agent
- Reads buggy Python programs from `python_programs/`.
- Ignores files ending with `_test.py`.
- Detects and classifies bugs using 14 QuixBugs error types.
- Applies the fix and saves the corrected version in `fixed_programs/`.
- Adds a comment at the top with the bug type.

### 2. Testing Agent
- Runs the test cases corresponding to each program using `pytest`.
- Supports `--fixed` flag to test fixed files, and `--correct` for baseline.
- Returns either:
  - `correct` if all test cases pass.
  - `wrong` if any test case fails.
- If the result is `wrong`, control is passed back to the Correction Agent for reprocessing.

### 3. Mapping Agent
- Maps the fixed solution back to the identified bug type.
- Generates a summary mapping file containing:
  - The bug type.
  - The original (buggy) code segment.
  - The corrected version.

---

## Implementation Details

- Used LangChain's `AgentExecutor` for agent workflows.
- Integrated `ShellTool` to execute test commands.
- Added a separate agent to patch missing test conditions:
  - Injects `elif pytest.fixed:` block into test files for compatibility with fixed programs.
- Used `ChatPromptTemplate` over regular prompt strings to enforce better formatting and reliability.
- Utilized three different Gemini API keys (one per agent) to handle rate limits and avoid quota exhaustion.
- Added retry and cooldown logic (60-second wait) to manage quota errors and avoid frequent failures.

---

## Folder Structure

