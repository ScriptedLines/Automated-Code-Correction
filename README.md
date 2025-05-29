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

## Evaluation

Program,Failures,TimeTakenSeconds
bitcount,0,11.536273
breadth_first_search,0,8.095694
bucketsort,0,8.300029
depth_first_search,0,9.135612
detect_cycle,0,16.972932
find_first_in_sorted,0,8.129862
find_in_sorted,0,9.288519
flatten,0,10.531217
gcd,0,9.732092
get_factors,0,12.875088
hanoi,0,8.723864
is_valid_parenthesization,0,10.840768
kheapsort,0,8.325466
kth,0,8.901849
lcs_length,0,8.396825
levenshtein,0,9.822777
lis,0,12.445656
longest_common_subsequence,0,9.262086
max_sublist_sum,1,17.419396
mergesort,0,8.094324
minimum_spanning_tree,0,24.09882
next_palindrome,7,99.298975
next_permutation,0,8.395218
pascal,0,13.368541
possible_change,0,7.526627
powerset,0,7.474385
quicksort,0,7.692811
reverse_linked_list,0,10.288412
rpn_eval,0,8.887516
shortest_paths,0,8.496715
shortest_path_length,0,10.249704
shortest_path_lengths,0,15.572552
shunting_yard,0,9.506368
sieve,0,9.244037
sqrt,0,7.95758
subsequences,0,8.785693
topological_ordering,2,32.011812
to_base,0,8.431677
wrap,0,9.221016

---

# Install dependencies
pip install -r requirements.txt

# Run the main pipeline
python agent.ipynb


