# automating-python-code

Benefits you get:
1. Enforces quality checks.
2. Improve code reviews.
3. The machine has your back.

**Steps to automation**:
1. Tools for improving code quality.
- flake8
- pylint
- coverage
2. Automating for a local environment.
3. Automating for a team/project automation.


**flake8** is going to analyze your source code and going to run these three tools under-the-hood.
- pycodestyle --> It looks for styling issues, especially relates to `PEP8` and `non-pythonic` usage.
- pyflakes --> It looks for code bugs and it only emits issues that have a low probability of `False positives`.
- mccabe --> It is a complexity checker. It checks mccabe complexity which is number of independent code pass a piece of code could have.

To install flake8: `pip install flake8`

You can run it on a single file: `flake8 module.py`
You can run it on a directory: `flake8 mypackage/`

**PyLint**:
- Similar to flake8.
- Checks coding standards.
- Warns for styling issues.
- Checks for potential bugs.
- Generally stricter and more opinionated than flake8.

**PyLint vs Flake8**:

![pylint vs flake8](https://github.com/arjungoel/automating-python-code/blob/main/images/pylint_vs_flake8.png)
