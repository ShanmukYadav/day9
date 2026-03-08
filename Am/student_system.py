# student_system.py
# Day 9 AM - Student Management System
# Part A: Lists Deep Dive Assignment

import copy

# ─────────────────────────────────────────────
# Global student records (list of lists)
# ─────────────────────────────────────────────
records = [
    ["Aman",    "Math",    88],
    ["Priya",   "Physics", 91],
    ["Rahul",   "Math",    76],
    ["Sneha",   "Chemistry", 85],
    ["Vikram",  "Physics", 79],
    ["Divya",   "Math",    94],
    ["Arjun",   "Chemistry", 67],
    ["Meera",   "Physics", 88],
    ["Karan",   "Chemistry", 72],
    ["Nisha",   "Math",    83],
    ["Rohan",   "Physics", 95],
    ["Aisha",   "Chemistry", 90],
]


# ─────────────────────────────────────────────
# 1. add_student
# ─────────────────────────────────────────────
def add_student(name: str, subject: str, marks: int) -> None:
    """Add a student record using append; prevents duplicate name+subject."""
    # Check for duplicate (name + subject combination)
    for record in records:
        if record[0] == name and record[1] == subject:
            print(f"  ⚠️  '{name}' already has a record for '{subject}'. Skipping.")
            return
    records.append([name, subject, marks])
    print(f"  ✅  Added: {name} | {subject} | {marks}")


# ─────────────────────────────────────────────
# 2. get_toppers
# ─────────────────────────────────────────────
def get_toppers(subject: str) -> list:
    """Return top-3 students for a given subject, sorted by marks descending."""
    subject_records = [r for r in records if r[1] == subject]
    if not subject_records:
        print(f"  ⚠️  No records found for subject '{subject}'.")
        return []
    sorted_records = sorted(subject_records, key=lambda x: x[2], reverse=True)
    return sorted_records[:3]   # slicing to get top 3


# ─────────────────────────────────────────────
# 3. class_average
# ─────────────────────────────────────────────
def class_average(subject: str) -> float:
    """Return the average marks for a subject using list comprehension."""
    marks = [m[2] for m in records if m[1] == subject]
    if not marks:
        print(f"  ⚠️  No records found for subject '{subject}'.")
        return 0.0
    return sum(marks) / len(marks)


# ─────────────────────────────────────────────
# 4. above_average_students
# ─────────────────────────────────────────────
def above_average_students() -> list:
    """Return students scoring above the overall class average."""
    if not records:
        return []
    all_marks = [r[2] for r in records]           # list comprehension
    overall_avg = sum(all_marks) / len(all_marks)
    # nested logic: filter using comprehension
    above_avg = [r for r in records if r[2] > overall_avg]
    return above_avg, round(overall_avg, 2)


# ─────────────────────────────────────────────
# 5. remove_student
# ─────────────────────────────────────────────
def remove_student(name: str) -> None:
    """Remove ALL records of a student safely using list comprehension (no remove() in loop)."""
    global records
    original_len = len(records)
    records = [r for r in records if r[0] != name]   # safe filter
    removed = original_len - len(records)
    if removed:
        print(f"  🗑️   Removed {removed} record(s) for '{name}'.")
    else:
        print(f"  ⚠️  No records found for '{name}'.")


# ─────────────────────────────────────────────
# 6. save_to_file
# ─────────────────────────────────────────────
def save_to_file(filename: str = "students.txt") -> None:
    """Save all records to a text file on exit."""
    with open(filename, "w") as f:
        f.write(f"{'Name':<15} {'Subject':<12} {'Marks'}\n")
        f.write("-" * 35 + "\n")
        for r in records:
            f.write(f"{r[0]:<15} {r[1]:<12} {r[2]}\n")
    print(f"  💾  Records saved to '{filename}'.")


# ─────────────────────────────────────────────
# Menu-Driven Interface
# ─────────────────────────────────────────────
def show_menu() -> None:
    print("\n" + "=" * 40)
    print("   🎓  Student Management System")
    print("=" * 40)
    print("  1  Add student")
    print("  2  Show toppers (by subject)")
    print("  3  Show class average (by subject)")
    print("  4  Show above-average students")
    print("  5  Remove student")
    print("  6  Exit")
    print("=" * 40)


def main() -> None:
    while True:
        show_menu()
        choice = input("  Enter choice (1-6): ").strip()

        if choice == "1":
            name    = input("  Student name   : ").strip()
            subject = input("  Subject        : ").strip()
            try:
                marks = int(input("  Marks (0-100)  : ").strip())
            except ValueError:
                print("  ⚠️  Invalid marks. Please enter a number.")
                continue
            add_student(name, subject, marks)

        elif choice == "2":
            subject = input("  Subject (Math / Physics / Chemistry): ").strip()
            toppers = get_toppers(subject)
            if toppers:
                print(f"\n  🏆  Top 3 in {subject}:")
                for i, r in enumerate(toppers, 1):
                    print(f"    {i}. {r[0]:<15} {r[2]}")

        elif choice == "3":
            subject = input("  Subject (Math / Physics / Chemistry): ").strip()
            avg = class_average(subject)
            if avg:
                print(f"\n  📊  Average marks in {subject}: {avg:.2f}")

        elif choice == "4":
            result = above_average_students()
            if result:
                students, avg = result
                print(f"\n  📈  Overall average: {avg}")
                print(f"  Students above average ({len(students)}):")
                for r in students:
                    print(f"    • {r[0]:<15} {r[1]:<12} {r[2]}")

        elif choice == "5":
            name = input("  Student name to remove: ").strip()
            remove_student(name)

        elif choice == "6":
            save_to_file()
            print("  👋  Goodbye!\n")
            break

        else:
            print("  ⚠️  Invalid choice. Please enter 1-6.")


if __name__ == "__main__":
    main()
