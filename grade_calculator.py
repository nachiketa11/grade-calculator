"""
Student Grade Calculator
Calculates total marks, percentage, and grade for multiple subjects.
"""

import math

GRADE_SCALE = [
    (90, "O",  "Outstanding"),
    (80, "A+", "Excellent"),
    (70, "A",  "Very Good"),
    (60, "B+", "Good"),
    (50, "B",  "Average"),
    (40, "C",  "Satisfactory"),
    ( 0, "F",  "Fail"),
]


def get_grade(percentage: float) -> tuple[str, str]:
    for threshold, grade, remark in GRADE_SCALE:
        if percentage >= threshold:
            return grade, remark
    return "F", "Fail"


def get_marks(subject: str, max_marks: float) -> float:
    while True:
        raw = input(f"  Enter marks for {subject} (out of {max_marks}): ").strip()
        if not raw:
            print("  ✗ Input cannot be empty. Try again.")
            continue
        try:
            marks = float(raw)
        except ValueError:
            print("  ✗ Invalid input. Please enter a number.")
            continue
        if not math.isfinite(marks):
            print("  ✗ Marks must be a finite number.")
            continue
        if marks < 0:
            print("  ✗ Marks cannot be negative.")
            continue
        if marks > max_marks:
            print(f"  ✗ Marks cannot exceed max marks ({max_marks}).")
            continue
        return marks


def get_positive_float(prompt: str) -> float:
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
            if not math.isfinite(value):
                print("  ✗ Value must be a finite number.")
                continue
            if value <= 0:
                print("  ✗ Value must be greater than 0.")
                continue
            return value
        except ValueError:
            print("  ✗ Invalid input. Please enter a number.")


def get_positive_int(prompt: str) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
            if value <= 0:
                print("  ✗ Must be at least 1. Please enter a whole number.")
                continue
            return value
        except ValueError:
            print("  ✗ Invalid input. Please enter a whole number.")


def print_separator(char: str = "─", width: int = 50) -> None:
    print(char * width)


def print_results(subjects: list[dict], max_marks: float) -> None:
    total_obtained = sum(s["marks"] for s in subjects)
    total_max = max_marks * len(subjects)
    percentage = (total_obtained / total_max) * 100
    grade, remark = get_grade(percentage)

    print("\n")
    print_separator("═")
    print("  RESULT CARD")
    print_separator("═")

    print(f"\n  {'Subject':<20} {'Marks':>10}   {'%':>6}   Grade")
    print_separator()

    for s in subjects:
        pct = (s["marks"] / max_marks) * 100
        g, _ = get_grade(pct)
        bar_len = int(pct / 5)
        bar = "█" * bar_len + "░" * (20 - bar_len)
        print(f"  {s['name']:<20} {s['marks']:>4.1f}/{max_marks:<4.0f}   {pct:>5.1f}%   {g}")
        print(f"  {'':20} [{bar}]")

    print_separator()
    print(f"\n  Total Marks   : {total_obtained:.1f} / {total_max:.0f}")
    print(f"  Percentage    : {percentage:.2f}%")
    print(f"  Grade         : {grade}")
    print(f"  Remark        : {remark}")
    print_separator("═")
    print()


def main() -> None:
    print_separator("═")
    print("   STUDENT GRADE CALCULATOR")
    print_separator("═")
    print()

    num_subjects = get_positive_int("Enter number of subjects: ")
    max_marks = get_positive_float("Enter max marks per subject: ")

    print()
    subjects = []
    for i in range(1, num_subjects + 1):
        name = input(f"  Subject {i} name (press Enter for 'Subject {i}'): ").strip()
        if not name:
            name = f"Subject {i}"
        marks = get_marks(name, max_marks)
        subjects.append({"name": name, "marks": marks})
        print()

    print_results(subjects, max_marks)

    again = input("Calculate for another student? (y/n): ").strip().lower()
    if again == "y":
        print("\n")
        main()
    else:
        print("\nGoodbye!")


if __name__ == "__main__":
    main()
