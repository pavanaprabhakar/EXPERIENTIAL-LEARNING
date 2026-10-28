Lab 5: Static Code Analysis — Reflection

1. What is static code analysis?

Static code analysis is the process of checking source code without running the program. It helps identify possible bugs, security vulnerabilities and coding style issues.

 2. What did Pylint, Bandit and Flake8 help identify?

Pylint identified code quality problems such as missing docstrings, incorrect naming conventions and unused imports. Bandit identified security risks such as SQL injection and unsafe subprocess usage. Flake8 identified formatting problems, including long lines and unnecessary blank lines.

 3. What changes were made to improve the program?

I replaced direct SQL string concatenation with parameterized queries, removed the hardcoded password and unsafe subprocess call, improved function names and docstrings, and corrected formatting issues. I also added handling for an artifact ID that does not exist.

4. What did I learn from this lab?

I learned that a program can run correctly and still contain security and code quality problems. Static analysis tools help identify these issues early. After making the changes, the Pylint score increased from 4.85 to 10.00, while Bandit and Flake8 reported no remaining findings.