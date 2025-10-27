## 1. Which issues were the easiest to fix, and which were the hardest? Why?

The easiest issues to fix were formatting-related ones like trailing whitespace, indentation errors, and converting `%` string formatting to f-strings. These were straightforward and required minimal logic changes. Renaming functions to snake_case was also simple but time-consuming due to the need to update all references.

The hardest issue was replacing the mutable default argument (`logs=[]`) and implementing input validation. It required understanding how Python handles default mutable arguments and restructuring the function to safely initialize the list. Another tricky fix was replacing the bare `except:` block with a specific exception type (`KeyError`) while preserving the intended behavior and adding meaningful logging.

## 2. Did the static analysis tools report any false positives? If so, describe one example.

Yes, one potential false positive was the unused `logging` import. Initially, `logging` was correctly imported and used later in the code, but after some edits, the import was temporarily removed, triggering a warning. Once re-added, the warning disappeared. This wasn’t a true false positive, but it highlighted how tool feedback can change based on intermediate states during refactoring.

## 3. How would you integrate static analysis tools into your actual software development workflow?

I would integrate static analysis tools into both local development and CI pipelines. Locally, I’d run tools like `pylint`, `flake8`, and `bandit` before each commit to catch issues early. In CI, I’d configure automated checks that fail builds if critical issues are found. This ensures consistent code quality across the team and prevents regressions. I’d also use pre-commit hooks to enforce style and security checks before code is pushed.

## 4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?

After applying the fixes, the code became significantly more readable and maintainable. Function names now follow Python conventions, making the code easier to understand. Adding docstrings clarified each function’s purpose. Input validation and safer exception handling improved robustness and error transparency. Removing `eval()` eliminated a major security risk. Overall, the code now feels cleaner, safer, and more professional.