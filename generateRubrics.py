#!/usr/bin/env python3
"""
generate_rubrics.py - Create individual rubric copies for each student.

Usage:
    python generate_rubrics.py -inputFile names.txt -fileToCopy rubric.xlsx [--assignment ASMT]

Options:
    -inputFile PATH        Text file with one student name per line.
    -fileToCopy PATH       Rubric template file to copy.
    --assignment TEXT      (Optional) Assignment label to insert in filename,
                           e.g., "02" -> JohnDoe-Assignment-02-Rubric.xlsx.
    --outputFolder DIR     Output folder name (default: Rubrics).
    --help                 Show this help.
"""

import os
import shutil
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(
        description="Generate individual rubric files for each student."
    )
    parser.add_argument(
        "-inputFile", required=True,
        help="Path to text file containing student names (one per line)."
    )
    parser.add_argument(
        "-fileToCopy", required=True,
        help="Path to rubric template file to copy."
    )
    parser.add_argument(
        "--assignment", default="",
        help="Assignment number (e.g., '02') to include in the filename."
    )
    parser.add_argument(
        "--outputFolder", default="Rubrics",
        help="Name of the output folder (default: Rubrics)."
    )
    args = parser.parse_args()

    # Read student names
    try:
        with open(args.inputFile, 'r', encoding='utf-8') as f:
            names = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: Input file '{args.inputFile}' not found.")
        sys.exit(1)

    if not names:
        print("Error: No student names found.")
        sys.exit(1)

    # Check template
    if not os.path.isfile(args.fileToCopy):
        print(f"Error: Template file '{args.fileToCopy}' not found.")
        sys.exit(1)

    # Create output folder
    os.makedirs(args.outputFolder, exist_ok=True)

    # Build base part of the new filename
    base = os.path.basename(args.fileToCopy)  # e.g., Assignment-02-Rubric.xlsx
    name_base, ext = os.path.splitext(base)   # ("Assignment-02-Rubric", ".xlsx")

    # If --assignment is given, insert it into the name (e.g., "Assignment-02-Rubric")
    # but the user might already have a filename with the assignment number.
    # We'll simply prefix the student name and, if --assignment is provided,
    # we'll replace or add the assignment part? Let's do a simple approach:
    # If --assignment is given, we'll construct: <name>-Assignment-<assignment>-Rubric.xlsx
    # Otherwise we just prepend the student name to the original filename.
    if args.assignment:
        # Build new name: e.g., JohnDoe-Assignment-02-Rubric.xlsx
        new_base = f"Assignment-{args.assignment}-Rubric"
        # But we need to keep the original extension
        # We'll replace the base name entirely, but keep the extension.
        new_filename = f"{name}-{new_base}{ext}"
    else:
        # Just prepend the student name to the original filename
        new_filename = f"{name}-{base}"

    success_count = 0
    for name in names:
        # If using assignment, we use the new_filename pattern for each
        if args.assignment:
            new_filename = f"{name}-Assignment-{args.assignment}-Rubric{ext}"
        else:
            new_filename = f"{name}-{base}"
        dest_path = os.path.join(args.outputFolder, new_filename)

        try:
            shutil.copy2(args.fileToCopy, dest_path)
            print(f"Created: {dest_path}")
            success_count += 1
        except Exception as e:
            print(f"Error for '{name}': {e}")

    print(f"\nDone. {success_count} of {len(names)} rubrics generated in '{args.outputFolder}'.")

if __name__ == "__main__":
    main()
