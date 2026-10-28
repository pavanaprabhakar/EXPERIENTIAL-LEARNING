 Lab 5: Static Code Analysis
 Museum Artifact Catalog

 1. SQL Injection Risk

Type: Security - Medium severity

Line: 11

Description: The SQL query is created by directly joining user input with the query string. This can allow SQL injection attacks.

Fix Approach:Use parameterized SQL queries with placeholders to safely insert values into the database.

2. Hardcoded Password

Type: Security - Low severity

Line:7

Description: The curator password is directly stored in the Python source code, which is not a secure practice.

Fix Approach: Remove the unused hardcoded password and avoid storing sensitive credentials directly in source code.

3. Unsafe Subprocess Call

Type: Security - Low severity

Line: 37

Description: The backup notice uses `subprocess.call()` with `shell=True`, which can introduce security risks.

Fix Approach: Replace the subprocess call with Python's built-in `print()` function because the program only needs to display a message.

 4. Missing Docstrings

Type: Code quality

Lines:Multiple

Description: The module and several functions do not have docstrings explaining their purpose.

Fix Approach: Add meaningful docstrings to describe the module and each function.

 5. Invalid Function Naming

Type: Code quality

Lines: 10, 15, 24, 31, 36

Description: Functions use camelCase naming instead of the recommended Python snake_case naming convention.

Fix Approach: Rename functions such as `addArtifact()` to `add_artifact()` and update their function calls.

 6. Unused Import

Type: Code quality and style

Line: 2

Description: The `datetime` module is imported but never used in the program.

Fix Approach: Remove the unnecessary import statement.

 7. Unused Function Argument

Type: Code quality

Line:15

Description: The `curator` argument is accepted by the display status function but is never used.

Fix Approach:Remove the argument if it is not required by the program's functionality.

 8. Formatting Violations

Type: Code style

Lines: Multiple

Description:The code contains long lines, extra blank lines and missing whitespace around operators.

Fix Approach: Break long statements into multiple lines, remove unnecessary blank lines and follow PEP 8 formatting guidelines.

Summary

The original Pylint score was 4.85/10. Bandit reported one medium-severity and four low-severity findings. Flake8 reported several formatting issues.

The identified issues will be fixed, and all three static analysis tools will be run again to verify that the corrections have been applied successfully.