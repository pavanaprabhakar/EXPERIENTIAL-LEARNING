# Lab 5: Static Code Analysis — Museum Artifact Catalog

## Issues Identified and How They Were Addressed

| Issue | Type | Original Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| SQL injection risk | Security — Medium | 11 | SQL query concatenated input values directly into the query string. | Replaced string concatenation with parameterized SQL queries using placeholders. |
| Hardcoded password | Security — Low | 7 | Curator password was stored directly in the source code. | Removed the unused hardcoded password. |
| Unsafe subprocess call | Security — Low | 37 | Used `subprocess.call()` with `shell=True` to print a backup notice. | Replaced the subprocess call with Python's `print()` function. |
| Missing docstrings | Code quality | Multiple | Module and functions lacked documentation. | Added descriptive module and function docstrings. |
| Invalid function names | Code quality | Multiple | Function names used camelCase instead of snake_case. | Renamed functions using snake_case and updated their calls. |
| Unused import | Code quality / Style | 2 | The `datetime` module was imported but never used. | Removed the unused import. |
| Unused argument | Code quality | 15 | The `curator` argument was accepted but never used. | Removed the unnecessary argument from the function and its call. |
| Formatting violations | Style | Multiple | Long lines, extra blank lines and missing whitespace were reported. | Reformatted the code to follow PEP 8 style guidelines. |
| Missing artifact handling | Robustness | Not flagged by the original reports | The original function could fail if an artifact ID did not exist. | Added a check that returns `artifact not found` when no matching artifact exists. |

## Verification Results

- **Pylint:** Improved from 4.85/10 to 10.00/10.
- **Bandit:** No issues identified after the fixes.
- **Flake8:** No violations reported after the fixes.
- **Program test:** The catalog printed the expected display status, total value of 135000, and backup confirmation.

The original line numbers refer to the code before changes. The missing artifact handling was an additional improvement rather than a finding reported by the three tools.