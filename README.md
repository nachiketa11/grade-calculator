# Student Grade Calculator

A command-line Python application that calculates subject-wise percentages, an overall percentage, and a grade/remark for a student.

## Features

- Enter any positive number of subjects.
- Configure the maximum marks per subject.
- Validate marks so they stay within the allowed range.
- Reject blank, non-numeric, non-finite (`nan` / `inf`), negative, and over-limit numeric input.
- Display a result card with subject grades, progress bars, total marks, percentage, and overall grade.
- Calculate results for another student without restarting the program.

## Requirements

- Python 3.9 or newer (the code uses built-in generic type annotations).

No third-party packages are required.

## Run the program

From the repository root:

```bash
python grade_calculator.py
```

On Windows, you can also use:

```powershell
py grade_calculator.py
```

Follow the prompts to enter the number of subjects, maximum marks per subject, subject names, and marks.

## Run tests

The automated tests use Python's standard library:

```bash
python -m unittest discover -s tests -v
```

The tests cover grade boundaries, retrying invalid input, and rejecting non-finite and out-of-range marks.

## Grade scale

| Percentage | Grade | Remark |
| ---: | :---: | --- |
| 90–100 | O | Outstanding |
| 80–89.99 | A+ | Excellent |
| 70–79.99 | A | Very Good |
| 60–69.99 | B+ | Good |
| 50–59.99 | B | Average |
| 40–49.99 | C | Satisfactory |
| Below 40 | F | Fail |

This is a sample grading scale for the project; adjust `GRADE_SCALE` in `grade_calculator.py` if your institution uses different rules.
