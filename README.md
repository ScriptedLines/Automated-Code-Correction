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

## Features

- Uses separate Gemini API keys for each agent to avoid quota exhaustion.
- Implements retry logic with 60-second cooldown on quota errors.
- Uses `ChatPromptTemplate` to enforce consistent LLM output formatting.
- Stores fix history in `fix_log.csv` and bug-fix mappings in `Bugs_Mapping.txt`.

---

## Bug-Fix Mapping

1)Wrong operator: Changed the bitwise operator from `^` (XOR) to `&` (AND) to correctly count set bits.

2)Loop condition logic: Changed the loop condition to check if all incoming nodes of the next node are in the ordered nodes, instead of checking outgoing nodes, to ensure nodes are added in the correct topological order.

3)Variable misuse: Renamed methods `successor`, `successors`, and `predecessors` to `get_successor`, `get_successors`, and `get_predecessors` to avoid naming conflicts with class attributes.

4)Conditional block omission: Added an `equal` list to handle elements equal to the pivot, preventing infinite recursion when the input array contains duplicate elements.

5)Wrong function call: Corrected the recursive call to yield the element directly when it's not a list.

6)Expression modification: Corrected the Floyd-Warshall algorithm by changing `length_by_path[i, k] + length_by_path[j, k]` to `length_by_path[i, k] + length_by_path[k, j]` to correctly calculate shortest path lengths.

7)Incorrect return statement: Reversed the output string to return the correct base conversion.

8)Incorrect function condition: Added a condition to return an empty list if k is greater than the range size or a is greater than b, and changed the return statement when k==0 from `return []` to `return [[]]`.

9)Loop boundary error: Modified the loop to iterate only through the unsorted portion of the array, preventing re-insertion of already-sorted elements.

10)Comparison logic error: Changed condition from '<' to '>' to find the correct element for swapping in the next permutation in the next_permutation function.

11)Incorrect function condition: Changed condition from `len(arr) == 0` to `len(arr) <= 1` to handle the base case when the array has one element in mergesort.

12)Exception handling bug: Added try-except block to handle IndexError and swapped the order of operands to correctly evaluate the RPN expression, handling malformed RPN expressions.

13)Operator omission: Added `lines.append(text)` after the while loop to include the remaining text after the wrapping process.

14)Incorrect function condition: Changed condition from `if n <= 0` to `if n <= 1` to handle the base case when n is 1 in the factorial function.

--- 

# Install dependencies
pip install -r requirements.txt

# Run the main pipeline
python agent.ipynb


