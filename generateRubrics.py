#!/usr/bin/env python3
"""
generateRubrics.py - Create individual rubric copies for each student.

Usage:
    python generateRubrics.py -inputFile names.txt -fileToCopy rubric.xlsx [--assignment ASMT]

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

    # Split the base filename into name and extension
    base = os.path.basename(args.fileToCopy)   # e.g., Assignment-01-Rubric.csv
    base_name, ext = os.path.splitext(base)    # ("Assignment-01-Rubric", ".csv")

    success_count = 0
    for name in names:
        # Construct new filename: <student> + - + (Assignment-XX-Rubric) + ext
        if args.assignment:
            # Build: Student-Assignment-XX-Rubric.ext
            new_base = f"Assignment-{args.assignment}-Rubric"
            new_filename = f"{name}-{new_base}{ext}"
        else:
            # Prepend student name to original filename
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
